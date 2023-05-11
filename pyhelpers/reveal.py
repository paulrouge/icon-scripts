import os
from .pad import pad
from .craftcontract import setInternalUri
import time

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

        try:
            setInternalUri(icon_service, nid, score_address, wallet, i, uri)
        except Exception as e:
            print(f"error with {i}")
            print(e)
            continue

def setIndividualInternalUri(icon_service, nid, score_address, wallet, token_id):
    base_uri = "bafybeihc7sfoe5vqzvwf5v7srt2qdpfwcfeeips5bk5x7x7nhf3r3x4iqi/"
    # loop through all the files in the metadata_files folder and find the file name that matches the token_id
    path, dirs, files = next(os.walk("metadata_files/"))
    file_name = [file for file in files if file.startswith(str(token_id))][0]
    # get the complete uri
    uri = base_uri + file_name
    setInternalUri(icon_service, nid, score_address, wallet, id, uri)


def handleMissedTokenids(icon_service, nid, score_address, wallet):
    missed_ids = [491, 493, 513, 619, 632, 655, 656, 662, 667, 679, 714, 717, 725, 732, 770, 776, 802, 819, 831, 878, 881, 891, 896, 898, 899, 908, 909, 924, 936, 938, 947, 951, 956, 960, 1031, 1078, 1088, 1092, 1113, 1238, 1258, 1286, 1332, 1357, 1380, 1414, 1470, 1471, 1534, 1606, 1724, 1728, 1792, 1793, 1830, 2111, 2112, 2230, 2249, 2253, 2291, 2293, 2295, 2298, 2299, 2300, 2317, 2318, 2319, 2320, 2321, 2325, 2327, 2337, 2342, 2349, 2358, 2360, 2378, 2382, 2383, 2385, 2387, 2391, 2394, 2395, 2396, 2402, 2422, 2425, 2427, 2428, 2620, 2766, 2786, 2893, 2901, 2950, 2987, 2989, 2996, 3099, 3116, 3125, 3130, 3187, 3228, 3261, 3262, 3263, 3272, 3311, 3312, 3314, 3318, 3321, 3327, 3430, 3440, 3527, 3542, 3579, 3619, 3644, 3648, 3663, 3702, 3718, 3732, 3734, 3735, 3768, 3772, 3823, 3824, 3871, 3904, 3940, 3953, 3962, 3973, 3978, 3979, 3999, 4013, 4124, 4142, 4192, 4194, 4195, 4201, 4210, 4337, 4396, 4424, 4425, 4437, 4454, 4462, 4554, 4591, 4659, 4712, 4746, 4775, 4822, 4830, 4833]
    # missed_ids = [263, 483]  
    
    for i in missed_ids:
        padded_id = pad(i, 4)
        
        setIndividualInternalUri(icon_service, nid, score_address, wallet, padded_id, i)
        time.sleep(1)



