from iconsdk.builder.call_builder import CallBuilder
from iconsdk.builder.transaction_builder import CallTransactionBuilder
from iconsdk.signed_transaction import SignedTransaction

def makeCall(icon_service, score_address, method, params, wallet):
    call = CallBuilder().from_(wallet.get_address()) \
        .to(score_address) \
        .method(method) \
        .params(params) \
        .build()

    result = icon_service.call(call)
    print(result)

def makeTransaction(icon_service,nid, score_address, method, params, value, wallet):
    txObj = CallTransactionBuilder() \
        .from_(wallet.get_address()) \
        .to(score_address) \
        .step_limit(100000000) \
        .nid(nid) \
        .nonce(100) \
        .version(3) \
        .value(value) \
        .method(method) \
        .params(params) \
        .build()
    
    signed_transaction = SignedTransaction(txObj, wallet)
    tx_hash = icon_service.send_transaction(signed_transaction)
    print(tx_hash)

