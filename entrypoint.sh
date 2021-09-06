#! /bin/bash
set -me

ganache-cli \
  -h 0.0.0.0 \
  --accounts 10 \
  --hardfork istanbul \
	--defaultBalanceEther 1000 \
	--db ./yearn-database \
  --fork https://eth-mainnet.alchemyapi.io/v2/${WEB3_ALCHEMY_PROJECT_ID} \
  --gasLimit 12000000 \
  --mnemonic yearn-mainnet-fork \
  --port 8545 &
sleep 5
brownie run /app/yearn-mainnet-fork/supply_tokens.py --network mainnet-fork
fg
