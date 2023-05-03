#!bin/bash

# mainnet = "https://ctz.solidwallet.io/api/v3"
# lisbon = "https://lisbon.net.solidwallet.ioi/api/v3"
# sejong = "https://sejong.net.solidwallet.ioi/api/v3"

# nid lisbon 0x2, sejong 0x53
printf "\n"

TX="../goloop/bin/goloop rpc sendtx deploy /Users/paul/Desktop/Projects/Icon/multitoken-presale/app/build/libs/app-0.1.0-optimized.jar\
    --uri https://lisbon.net.solidwallet.io/api/v3 \
    --key_store "/Users/paul/Desktop/Projects/Icon/wallets/test_keystore_01" --key_password password \
    --nid 0x2 --step_limit 7000000000 \
    --param TOBEREVEALED_URI=testuri --param MAX_SALES=5000\
    --content_type application/java"

$TX 
printf "\n"