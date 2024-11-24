import * as anchor from "@project-serum/anchor";
import { Program } from "@project-serum/anchor";
import { GptarsLimit } from "../target/types/gptars_limit";
import { expect } from "chai";

describe("gptars_limit", () => {
  const provider = anchor.AnchorProvider.env();
  anchor.setProvider(provider);
  const program = anchor.workspace.GptarsLimit as Program<GptarsLimit>;

  let stateAccount = anchor.web3.Keypair.generate();
  let mint = anchor.web3.Keypair.generate();
  let tokenAccount = anchor.web3.Keypair.generate();
  let destination = anchor.web3.Keypair.generate();
  const monthlyLimit = 280_000;

  it("Initializes the state", async () => {
    await program.rpc.initialize(new anchor.BN(monthlyLimit), {
      accounts: {
        state: stateAccount.publicKey,
        mint: mint.publicKey,
        payer: provider.wallet.publicKey,
        systemProgram: anchor.web3.SystemProgram.programId,
      },
      signers: [stateAccount],
    });

    const state = await program.account.tokenLimitState.fetch(stateAccount.publicKey);
    expect(state.monthlyLimit.toNumber()).to.equal(monthlyLimit);
    expect(state.soldThisMonth.toNumber()).to.equal(0);
  });

  it("Allows token sales within the monthly limit", async () => {
    const amountToSell = 100_000;
    await program.rpc.sellTokens(new anchor.BN(amountToSell), {
      accounts: {
        state: stateAccount.publicKey,
        mint: mint.publicKey,
        tokenAccount: tokenAccount.publicKey,
        destination: destination.publicKey,
        authority: provider.wallet.publicKey,
        tokenProgram: anchor.utils.token.TOKEN_PROGRAM_ID,
      },
    });

    const state = await program.account.tokenLimitState.fetch(stateAccount.publicKey);
    expect(state.soldThisMonth.toNumber()).to.equal(amountToSell);
  });

  it("Prevents token sales exceeding the monthly limit", async () => {
    const amountToSell = 200_000; // Exceeds remaining limit
    try {
      await program.rpc.sellTokens(new anchor.BN(amountToSell), {
        accounts: {
          state: stateAccount.publicKey,
          mint: mint.publicKey,
          tokenAccount: tokenAccount.publicKey,
          destination: destination.publicKey,
          authority: provider.wallet.publicKey,
          tokenProgram: anchor.utils.token.TOKEN_PROGRAM_ID,
        },
      });
      throw new Error("This should have failed");
    } catch (err) {
      expect(err.message).to.include("Monthly token sale limit exceeded.");
    }
  });
});
