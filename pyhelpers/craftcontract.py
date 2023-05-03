from .call import makeTransaction

def setPresalePrice(icon_service, nid, score_address, wallet, price):
    params = {
        "_price": hex(price*10**18)
    }

    makeTransaction(icon_service, nid, score_address, "setPresalePrice", params, 0, wallet)

def openPresale(icon_service, nid, score_address, wallet):
    makeTransaction(icon_service, nid, score_address, "openPresale", {}, 0, wallet)

def closePresale(icon_service, nid, score_address, wallet):
    makeTransaction(icon_service, nid, score_address, "closePresale", {}, 0, wallet)

# @notice - _address is a list of addresses
def addWhitelist(icon_service, nid, score_address, wallet, addresses):
    params = {
        "_adr": addresses
    }

    makeTransaction(icon_service, nid, score_address, "addWhitelist", params, 0, wallet)

def presaleMint(icon_service, nid, score_address, value, wallet, amount):
    params = {
        "_amount" : hex(amount),
    }

    makeTransaction(icon_service, nid, score_address, "presaleMint", params, value, wallet)

def openRegularSale(icon_service, nid, score_address, wallet):
    makeTransaction(icon_service, nid, score_address, "openRegularSale", {}, 0, wallet)

def closeRegularSale(icon_service, nid, score_address, wallet):
    makeTransaction(icon_service, nid, score_address, "closeRegularSale", {}, 0, wallet)

def setNewTokenUri(icon_service, nid, score_address, wallet, tokenId_hex, uri):
    params = {
        "_id": tokenId_hex,
        "_uri": uri
    }

    makeTransaction(icon_service, nid, score_address, "nftReveal", params, 0, wallet)