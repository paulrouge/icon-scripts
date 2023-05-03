from iconsdk.icon_service import IconService
from iconsdk.providers.http_provider import HTTPProvider
from iconsdk.wallet.wallet import KeyWallet
from pyhelpers.craftcontract import (
    setPresalePrice, openPresale, closePresale, addWhitelist, presaleMint)

"""
First we set up some configs to connect to the ICON network.
mainnet is the mainnet endpoint, and lisbon is the testnet endpoint.
"""

mainnet = "https://ctz.solidwallet.io"
lisbon = "https://lisbon.net.solidwallet.io"

# Creates an IconService instance using the HTTP provider and set a provider.
icon_service = IconService(HTTPProvider(lisbon, 3))

# Load a wallet
wallet = KeyWallet.load("../wallets/test_keystore_01", "password")

# address to call - deployed nft contract
score_address = "cxd5a002cea3110f6f843f6bd0e8781981c0aca377"

"""
From here on out, we can call functions from the contract. They are set up in pyhelpers/craftcontract.py

Go through them step by step, if you're not sure what to do please reach out to me on discord.
"""


""" Frist set presale price - last param is price in ICX """
# setPresalePrice(icon_service, 2, score_address, wallet, 5)

""" open presale """
# openPresale(icon_service, 2, score_address, wallet)

""" close presale """
# closePresale(icon_service, 2, score_address, wallet)

"""
add whitelist - last param is list of addresses.
- example adding multiple addresses at once ["hx_adr1", "hx_adr2", "hx_adr3"]
- example adding one address ["hx_adr1"]
"""
# addWhitelist(icon_service, 2, score_address, wallet, ["hx0bed8daee97f616eea33d1344e682e013cc8523d"])

""" mint nft - last param is amount """
amount = 4
price = 5
value = (amount*price) * 10**18
# presaleMint(icon_service, 2, score_address, value, wallet, amount)