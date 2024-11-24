const { Connection, Keypair, PublicKey, Transaction, sendAndConfirmTransaction } = require('@solana/web3.js');
const { Token, TOKEN_PROGRAM_ID } = require('@solana/spl-token');
require('dotenv').config();
const fs = require('fs');

// Load the Dev Wallet Keypair
const walletKeypair = Keypair.fromSecretKey(
  Uint8Array.from(JSON.parse(fs.readFileSync(process.env.DEV_WALLET_KEYPAIR_PATH, 'utf8')))
);

// Constants
const RPC_URL = "https://api.mainnet-beta.solana.com"; // Replace with your Solana RPC URL
const connection = new Connection(RPC_URL, 'confirmed');
const GPTARS_MINT_ADDRESS = new PublicKey('GPTARS_Mint_Address_Here'); // Replace with your $GPTARS Mint Address
const GPTARS_PROGRAM_ID = new PublicKey('GPTARS_Program_Address_Here'); // Replace with the program ID
const DEV_WALLET_PUBLIC_KEY = walletKeypair.publicKey;

// Monthly Token Selling Function
async function sellTokens(destinationAddress, amountToSell) {
  try {
    // Load the GPTARS token account
    const tokenAccountInfo = await connection.getParsedTokenAccountsByOwner(DEV_WALLET_PUBLIC_KEY, {
      mint: GPTARS_MINT_ADDRESS,
    });

    const tokenAccount = tokenAccountInfo.value[0].pubkey; // Dev wallet's token account

    // Destination token account
    const destinationTokenAccount = new PublicKey(destinationAddress);

    // Create a transaction
    const transaction = new Transaction();

    // Token transfer instruction
    transaction.add(
      Token.createTransferInstruction(
        TOKEN_PROGRAM_ID,
        tokenAccount,
        destinationTokenAccount,
        DEV_WALLET_PUBLIC_KEY,
        [],
        amountToSell
      )
    );

    // Sign and send the transaction
    const signature = await sendAndConfirmTransaction(connection, transaction, [walletKeypair]);
    console.log(`Tokens sold successfully! Transaction Signature: ${signature}`);
  } catch (error) {
    console.error(`Error selling tokens: ${error}`);
  }
}

// Example Usage
(async () => {
  const destinationAddress = 'Destination_Token_Account_Address'; // Replace with the buyer's token account
  const amountToSell = 280_000; // Amount of tokens to sell (must be within the limit)

  await sellTokens(destinationAddress, amountToSell);
})();
