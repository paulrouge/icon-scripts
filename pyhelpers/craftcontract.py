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

def setInternalUri(icon_service, nid, score_address, wallet, tokenId, uri):
    params = {
        "_tokenId": hex(tokenId),
        "_uri": uri
    }

    makeTransaction(icon_service, nid, score_address, "setInternalUri", params, 0, wallet)

def revealTokenUris(icon_service, nid, score_address, wallet):
    makeTransaction(icon_service, nid, score_address, "revealTokenUris", {}, 0, wallet)

def setNewTokenUri(icon_service, nid, score_address, wallet, tokenId, uri):
    params = {
        "_tokenId": hex(tokenId),
        "_uri": uri
    }

    makeTransaction(icon_service, nid, score_address, "setTokenUri", params, 0, wallet)

def enableWhitelist(icon_service, nid, score_address, wallet):
    makeTransaction(icon_service, nid, score_address, "enableWhitelist", {}, 0, wallet)

def disableWhitelist(icon_service, nid, score_address, wallet):
    makeTransaction(icon_service, nid, score_address, "disableWhitelist", {}, 0, wallet)

def setPostReveal(icon_service, nid, score_address, wallet):
    makeTransaction(icon_service, nid, score_address, "setPostReveal", {}, 0, wallet)

def freeMint(icon_service, nid, score_address, wallet, amount, receiver):
    params = {
        "_amount" : hex(amount),
        "_address": receiver
    }

    makeTransaction(icon_service, nid, score_address, "freeMint", params, 0, wallet)

# def setCraftEscrow(icon_service, nid, score_address, wallet, craftEscrow):
#     params = {
#         "_address": craftEscrow
#     }

#     makeTransaction(icon_service, nid, score_address, "setCraftEscrow", {"_address": "cx9c4698411c6d9a780f605685153431dcda04609f"}, 0, wallet)

def editUnrevealURI(icon_service, nid, score_address, wallet, uri):
    params = {
        "_uri": uri
    }

    makeTransaction(icon_service, nid, score_address, "setUnreaveldURI", params, 0, wallet)