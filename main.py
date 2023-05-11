from iconsdk.icon_service import IconService
from iconsdk.providers.http_provider import HTTPProvider
from iconsdk.wallet.wallet import KeyWallet
from pyhelpers.call import deployContract
from pyhelpers.reveal import setInternalUris, handleMissedTokenids
from pyhelpers.craftcontract import (
    setPresalePrice,
    openPresale,
    closePresale,
    addWhitelist,
    presaleMint,
    setNewTokenUri,
    enableWhitelist,
    disableWhitelist,
    setPostReveal,
    revealTokenUris,
    freeMint

)

"""
First we set up some configs to connect to the ICON network.
"""

mainnet = "https://ctz.solidwallet.io" # the mainnet endpoint
lisbon = "https://lisbon.net.solidwallet.io" # the testnet endpoint

# Creates an IconService instance using the HTTP provider and set a provider.
icon_service = IconService(HTTPProvider(lisbon, 3))

nid = 2 # 1 for mainnet, 2 for testnet

# Load a wallet
wallet = KeyWallet.load("../wallets/test_keystore_01", "password")

# set max sales
max_sales = 3

# DEPLOY CONTRACT AT 'JAR' FOLDER
filename = 'app-0.1.0-optimized.jar'
params = {
    "TOBEREVEALED_URI": "bafybeigtiqkndavdgjzu4ud6hhkdb4mj3k5lwfqx4snx53etu4xpwhf5ve/unrevealed.json",
    "MAX_SALES": max_sales,
}

# deployContract(icon_service, nid, wallet, filename, params)

# address to call -> the deployed nft contract
score_address = "cx0caaa524bcc79358fe24303a9251bf8d47546413"

"""
From here on out, we can call functions from the contract. 
They are set up in pyhelpers/craftcontract.py.

Go through them step by step, 
if you're not sure what to do please reach out to me on discord.
"""

"""
------------------------------------------------------------------------------------------------------------------------
*   *   *   *   *   *   *   *   *   *   *   *   PRE-SALE SET UP   *   *   *   *   *   *   *   *   *   *   *   *   *   *
------------------------------------------------------------------------------------------------------------------------
"""


""" 1. Set internal uris. We are using this to prevent people from seeing the token uri before reveal. """
# setInternalUris(icon_service, nid, score_address, wallet, max_sales)

""" 2. Enable whitelisting ( on default it's disabled. Also wl'ing can only be applied on the presale, not the regular sale ) """
# enableWhitelist(icon_service, nid, score_address, wallet)

""" 3. set presale price """
price = 5 # 5 ICX
# setPresalePrice(icon_service, nid, score_address, wallet, price)

""" 4. open presale """
# openPresale(icon_service, nid, score_address, wallet)

"""
add to whitelist - last param is list of addresses.
- example adding multiple addresses at once ["hx_adr1", "hx_adr2", "hx_adr3"] 
- example adding one address ["hx_adr1"] 
"""
# addWhitelist(icon_service, nid, score_address, wallet, ["hx0bed8daee97f616eea33d1344e682e013cc8523d"])

"""
-------------------------------------------------------------------------------------------------------------------------
*   *   *   *   *   *   ON REVEAL - be sure to run any of these only after reveal!!!    *   *   *   *   *   *   *   *   *
-------------------------------------------------------------------------------------------------------------------------
"""

""" 1. set postReveal to true ( will fail if 'setInternalUris' is not called first ) """
# setPostReveal(icon_service, nid, score_address, wallet)

""" 2. link the internal uris to existing tokenids """
# revealTokenUris(icon_service, nid, score_address, wallet)

""" 3. close the presale """
# closePresale(icon_service, nid, score_address, wallet)

""" 4. Disable whitelisting """
# disableWhitelist(icon_service, nid, score_address, wallet)

""" 5. set new presale price """
price = 5 # 5 ICX
# setPresalePrice(icon_service, nid, score_address, wallet, price)

""" 6. open presale again """
# openPresale(icon_service, nid, score_address, wallet)

"""
-------------------------------------------------------------------------------------------------------------------------
*   *   *   *   *   *   *   DONE - presale is now open to all with new price and whitelisting   *   *   *   *   *   *   *
-------------------------------------------------------------------------------------------------------------------------
"""


"""
-------------------------------------------------------------------------------------------------------------------------
*   *   *   *   *   *  *    *   *   *   *   EXTRAS - some extra utilities   *   *   *   *   *   *   *   *   *   *   *   *
-------------------------------------------------------------------------------------------------------------------------
"""

""" free mint - give an address an amount of free mints """
amount = 2
address = "hx0bed8daee97f616eea33d1344e682e013cc8523d"
# freeMint(icon_service, nid, score_address, wallet, amount, address)

""" set new token uri - last param is the new uri """
tokenid = 1
new_uri = "bafybeihc7sfoe5vqzvwf5v7srt2qdpfwcfeeips5bk5x7x7nhf3r3x4iqi/example_uri.json"
# setNewTokenUri(icon_service, nid, score_address, wallet, tokenid, new_uri)

""" mint nft - last param is amount - just for testing purposes, mint can be done on website """
amount = 1
price = 5
value = (amount*price) * 10**18
# presaleMint(icon_service, nid, score_address, value, wallet, amount)

handleMissedTokenids(icon_service, nid, score_address, wallet)