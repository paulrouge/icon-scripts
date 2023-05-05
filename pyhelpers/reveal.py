import os
from .pad import pad
from .craftcontract import setInternalUri

def setInternalUris(icon_service, nid, score_address, wallet, amount_of_nfts):
    # first verify that user wants to run this script

    userInput = input(f"""
    Are you sure you want to set all the internal uris? 

    This will do {amount_of_nfts} transactions. 
    So be sure to have enough ICX in your wallet!

    (y/n)

    """) 
    
    if userInput != "y":
        print("\nexiting...\n")
        exit()

    # count amount of files in /metadata_files folder
    path, dirs, files = next(os.walk("metadata_files/"))
    file_count = len(files)

    if file_count < amount_of_nfts:
        print("not enough metadata files")
        exit()

    base_uri = "bafybeihc7sfoe5vqzvwf5v7srt2qdpfwcfeeips5bk5x7x7nhf3r3x4iqi/"

    for i in range(amount_of_nfts):
        i = i + 1
        padded_id = pad(i, 4)
        
        # get the complete file name of the file that starts with padded_id
        file_name = [file for file in files if file.startswith(padded_id)][0]
        # get the complete uri
        uri = base_uri + file_name

        setInternalUri(icon_service, nid, score_address, wallet, i, uri)
