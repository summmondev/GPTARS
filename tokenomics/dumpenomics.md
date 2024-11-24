$GPTARS Tokenomics
Total Token Supply: 800,000,000 $GPTARS

![image](https://github.com/user-attachments/assets/caef9bbe-a0b7-4c05-9be6-2018bb2c648b)

1. Robot Reserve (100,000,000 $GPTARS)
This allocation will cover the robot's operational expenses and upgrades. It ensures GPTARS can operate sustainably for 10+ years without relying on external funding.

![image](https://github.com/user-attachments/assets/d13a867b-6be9-4792-9776-4b7b6dd85e9f)

-Total Monthly Cost: $2,800
-Total Annual Cost: $33,600

How the Robot Reserve Will Be Spent
  Token Price Assumption: $0.01 (initial average price of $GPTARS).
  Monthly Token Spend: 280,000 $GPTARS (at $0.01 per token).
  Sustainability: At this rate, the Robot Reserve can sustain GPTARS for ~30 years, even without external funding.

----
# Wallet Management for $GPTARS

This directory contains the code for managing the developer wallet and enforcing token sale limits.

## **Files**
- `sell_tokens_ai.js`: A Node.js script for the AI to interact with the Solana blockchain and sell $GPTARS tokens programmatically.
- `smart_contract/`: Contains the Solana smart contract for enforcing the monthly token sale limit (280,000 $GPTARS).

## **How It Works**
1. **AI Automation**: The `sell_tokens_ai.js` script:
   - Manages the developer wallet.
   - Executes token transfers within the monthly limit.
   - Schedules automated token sales every month.

2. **Smart Contract**:
   - Enforces the 280,000 $GPTARS/month cap.
   - Resets counters automatically at the beginning of each month.

## **Getting Started**
### Prerequisites
- Install Solana CLI: `https://docs.solana.com/cli/install-solana-cli-tools`
- Install Node.js and dependencies:
  ```bash
  npm install @solana/web3.js @solana/spl-token dotenv
