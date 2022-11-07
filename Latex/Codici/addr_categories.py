def analyze_spent(addresses, spent):
    len(addresses) #toal addresses
    tx_success = collect_tx("../tx_spent_dust.txt")
    tx_sp = collect_tx("../tx_special.txt")
    spent = pd.read_csv("../data_csv/spent_dust.csv.xz", sep=',', header=0, compression='xz')    
    addr_failed = set(spent[~spent.spentTxId.isin(tx_success)]['addrId'].to_list())
    addr_succ = set(spent[spent.spentTxId.isin(tx_success)]['addrId'].to_list())
    addr_spec = set(spent[spent.spentTxId.isin(tx_sp)]['addrId'].to_list())

    only_succ = 0
    only_failed = 0
    only_special = 0
    succ_failed = 0
    succ_special = 0
    failed_special = 0
    for addr in addresses:
        if(addr in addr_succ):
            if(addr in addr_failed): succ_failed += 1
            elif(addr in addr_spec): succ_special += 1
            else: only_succ += 1

        elif(addr in addr_failed):
            if(addr in addr_succ): succ_failed += 1
            elif(addr in addr_spec): failed_special += 1
            else: only_failed += 1

        elif(addr in addr_spec):
            if(addr in addr_failed): failed_special += 1
            elif(addr in addr_succ): succ_special += 1
            else: only_special += 1