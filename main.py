from iconsdk.icon_service import IconService
from iconsdk.providers.http_provider import HTTPProvider
from iconsdk.wallet.wallet import KeyWallet
from pyhelpers.call import deployContract
from pyhelpers.reveal import reveal
from pyhelpers.craftcontract import (
    setPresalePrice,
    openPresale,
    closePresale,
    addWhitelist,
    presaleMint,
    openRegularSale,
    closeRegularSale,
    setNewTokenUri,
    enableWhitelist,
    disableWhitelist
)

"""
First we set up some configs to connect to the ICON network.
mainnet is the mainnet endpoint, and lisbon is the testnet endpoint.
"""

mainnet = "https://ctz.solidwallet.io"
lisbon = "https://lisbon.net.solidwallet.io"

# Creates an IconService instance using the HTTP provider and set a provider.
icon_service = IconService(HTTPProvider(lisbon, 3))

nid = 2 # 1 for mainnet, 2 for testnet

# Load a wallet
wallet = KeyWallet.load("../wallets/test_keystore_01", "password")

# DEPLOY CONTRACT AT 'JAR' FOLDER
filename = 'app-0.1.0-optimized.jar'
params = {
    "TOBEREVEALED_URI": "bafybeigtiqkndavdgjzu4ud6hhkdb4mj3k5lwfqx4snx53etu4xpwhf5ve/unrevealed.json",
    "MAX_SALES": 5000,
}

# deployContract(icon_service, nid, wallet, filename, params) 

# address to call -> the deployed nft contract
score_address = "cxd5a002cea3110f6f843f6bd0e8781981c0aca377"

"""
From here on out, we can call functions from the contract. 
They are set up in pyhelpers/craftcontract.py

Go through them step by step, 
if you're not sure what to do please reach out to me on discord.
"""

""" Enable whitelisting ( on default it's disabled. Also wl'ing can only be applied on the presale, not the regular sale ) """
# enableWhitelist(icon_service, nid, score_address, wallet)

""" Disable whitelisting (if you want) """
# disableWhitelist(icon_service, nid, score_address, wallet)

""" Frist set presale price """
price = 5 # 5 ICX
# setPresalePrice(icon_service, nid, score_address, wallet, price)

""" open presale """
# openPresale(icon_service, nid, score_address, wallet)

""" close presale """
# closePresale(icon_service, nid, score_address, wallet)

"""
add to whitelist - last param is list of addresses.
- example adding multiple addresses at once ["hx_adr1", "hx_adr2", "hx_adr3"] 
- example adding one address ["hx_adr1"] 
"""
# addWhitelist(icon_service, nid, score_address, wallet, ["hx0bed8daee97f616eea33d1344e682e013cc8523d"])

"""
ON REVEAL
"""
amount_of_nfts = 3
# reveal(icon_service, nid, score_address, wallet, amount_of_nfts)

""" set price for regular sale """
price = 10 # 10 ICX
# setRegularPrice(icon_service, nid, score_address, wallet, price)

""" open regular sale """
# openRegularSale(icon_service, nid, score_address, wallet)






""" mint nft - last param is amount - just for testing purposes, mint can be done on website """
amount = 4
price = 5
value = (amount*price) * 10**18
# presaleMint(icon_service, nid, score_address, value, wallet, amount)