import requests, json

# make a map with int 1 to 5000 as key and bool as value
id_map = {}
for i in range(1, 5001):
    id_map[i] = False
    
def check_txs():
    limit = 100
    skip = 0
    get_count = "https://tracker.icon.community/api/v1/transactions/address/cx546ee1958a1daa64f914c328081e2285ed9973ff?addr=cx546ee1958a1daa64f914c328081e2285ed9973ff&limit=100&skip=100"
    #  check base
    r = requests.get(get_count)
    # check header for x-count
    x_count = int(r.headers["x-total-count"])
    # x_count = 1

    total_pages = int(x_count / limit) + 2
    print(f"total_pages: {total_pages}")

    for i in range(total_pages):
        skip = i * 100
        print(f"skip: {skip} i: {i}")
        getData(skip)
        
        
    missed_ids = []
    #  get amount of False values in id_map
    false_count = 0
    for key in id_map:
        if id_map[key] == False:
            missed_ids.append(key)
            false_count = false_count + 1

    print(f"false_count: {false_count}")
    print(missed_ids)
        
    
    
def getData(skip):
    get_data = f"https://tracker.icon.community/api/v1/transactions/address/cx546ee1958a1daa64f914c328081e2285ed9973ff?addr=cx546ee1958a1daa64f914c328081e2285ed9973ff&limit=100&skip={skip}"
    # print()
    r = requests.get(get_data)
    data = r.json()

    for tx in data:
    
        call_data = tx["data"]
        if call_data == None:
            continue
        
        # call_data to json
        call_data = json.loads(call_data)

        try:
            method = call_data["method"]
            # print("method" , method)
            if method == "setInternalUri":
                params = call_data["params"]
                token_id = params["_tokenId"]

                # token_id is now a hexstring, convert to int
                token_id = int(token_id, 16)
                # if token_id == 262:
                #     print(tx)
                # set the value of the token_id key to True
                id_map[token_id] = True

        except Exception as e:
            print("\n-----------------------------------\n")
            # print(call_data, e)
            continue




check_txs()