use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, Token, TokenAccount, Transfer};

declare_id!("YourProgramIDHere");

#[program]
pub mod gptars_limit {
    use super::*;

    pub fn initialize(ctx: Context<Initialize>, monthly_limit: u64) -> Result<()> {
        let state = &mut ctx.accounts.state;
        state.monthly_limit = monthly_limit;
        state.sold_this_month = 0;
        state.last_reset_timestamp = Clock::get()?.unix_timestamp;
        Ok(())
    }

    pub fn sell_tokens(ctx: Context<SellTokens>, amount: u64) -> Result<()> {
        let state = &mut ctx.accounts.state;
        let current_timestamp = Clock::get()?.unix_timestamp;

        // Reset the monthly limit if a new month has started
        let one_month_seconds = 30 * 24 * 60 * 60; // Approx. 30 days
        if current_timestamp > state.last_reset_timestamp + one_month_seconds {
            state.sold_this_month = 0;
            state.last_reset_timestamp = current_timestamp;
        }

        // Ensure the amount being sold doesn't exceed the limit
        require!(
            state.sold_this_month + amount <= state.monthly_limit,
            TokenError::MonthlyLimitExceeded
        );

        // Perform the token transfer
        let cpi_accounts = Transfer {
            from: ctx.accounts.token_account.to_account_info(),
            to: ctx.accounts.destination.to_account_info(),
            authority: ctx.accounts.authority.to_account_info(),
        };

        let cpi_program = ctx.accounts.token_program.to_account_info();
        let cpi_ctx = CpiContext::new(cpi_program, cpi_accounts);
        token::transfer(cpi_ctx, amount)?;

        // Update the amount sold this month
        state.sold_this_month += amount;

        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = payer, space = 8 + 8 + 8 + 8)]
    pub state: Account<'info, TokenLimitState>,
    #[account(mut)]
    pub mint: Account<'info, Mint>,
    #[account(mut)]
    pub payer: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct SellTokens<'info> {
    #[account(mut, has_one = mint)]
    pub state: Account<'info, TokenLimitState>,
    pub mint: Account<'info, Mint>,
    #[account(mut)]
    pub token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub destination: Account<'info, TokenAccount>,
    pub authority: Signer<'info>,
    pub token_program: Program<'info, Token>,
}

#[account]
pub struct TokenLimitState {
    pub monthly_limit: u64,         // Maximum tokens that can be sold in a month
    pub sold_this_month: u64,       // Tokens sold so far in the current month
    pub last_reset_timestamp: i64, // Timestamp of the last reset
}

#[error_code]
pub enum TokenError {
    #[msg("Monthly token sale limit exceeded.")]
    MonthlyLimitExceeded,
}
