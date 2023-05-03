from iconsdk.wallet.wallet import KeyWallet

# create a wallet instance
wallet = KeyWallet.create() 
wallet.store("./test_keystore_01", "password")