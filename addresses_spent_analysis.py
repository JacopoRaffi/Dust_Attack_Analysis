import pandas as pd
import sys
#TODO
"""
- attacchi di successo: considera percentuale di address destinatari di dust che NON compaiono per la prima volta on chain per quella transazione
"""

def collect_tx(filename):
    txs = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            tx = int(line)
            txs.append(tx)
    return txs

def analyze_spent(addresses, spent):
    print("TOT ADDR: ", len(addresses))
    tx_success = collect_tx("../tx_spent_dust.txt")
    tx_sp = collect_tx("../tx_special.txt")
    spent = pd.read_csv("../data_csv/spent_dust.csv.xz", sep=',', header=0, compression='xz')
    sp = spent[~spent.spentTxId.isin(tx_success)]
    sp = sp[~sp.spentTxId.isin(tx_sp)]

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
            if(addr in addr_failed):
                succ_failed += 1
            elif(addr in addr_spec):
                succ_special += 1
            else:
                only_succ += 1

        elif(addr in addr_failed):
            if(addr in addr_succ):
                succ_failed += 1
            elif(addr in addr_spec):
                failed_special += 1
            else:
                only_failed += 1

        elif(addr in addr_spec):
            if(addr in addr_failed):
                failed_special += 1
            elif(addr in addr_succ):
                succ_special += 1
            else:
                only_special += 1
        else:
            print(addr)

    print("TOTALE: ", len(set(addresses)))
    print("ONLY SUCCESS: ", only_succ)
    print("ONLY FAILED: ", only_failed)
    print("ONLY SPECIAL: ", only_special)
    print("SUCCESS FAILED: ", succ_failed)
    print("SUCCESS SPECIAL: ", succ_special)
    print("FAILED SPECIAL: ", failed_special)

def categories(sp, unsp):
    addr_sp = set(sp['addrId'].to_list())
    addr_unsp = set(unsp['addrId'].to_list())
    addr_both = set([])
    addr_os = addr_sp.copy()
    addr_ou = addr_unsp.copy()
    addr_tot = addr_sp.union(addr_unsp)
    print("INDIRIZZI TOTALI: ", len(addr_tot))
    only_sp = len(addr_sp)
    only_unsp = len(addr_unsp)
    both_set = 0
    for addr in addr_sp:
        if(addr in addr_unsp): #it means it is in both set
            only_sp -= 1
            only_unsp -= 1
            both_set += 1 
            addr_both.add(addr)
            addr_os.remove(addr)
            addr_ou.remove(addr)
    
    print("ONLY SPENT: ", only_sp)
    print("ONLY UNSPENT: ", only_unsp)
    print("BOTH CASES: ", both_set)

    print("ONLY SPENT ADDRESSES: ")
    analyze_spent(addr_os, sp)

    print("NOT ONLY SPENT ADDRESSES: ")
    analyze_spent(addr_both, sp)

def new_addresses(spent, unspent):
    tx_success = collect_tx("../tx_spent_dust.txt")
    sp = spent[spent.spentTxId.isin(tx_success)] 
    outputs = pd.read_csv("../data_csv/outputs_dust.csv.xz", sep=',', header=0, compression='xz')
    outputs = outputs[outputs.TxId.isin(sp['TxId'].to_list())]
    tx_MaxId = pd.read_csv("../data_csv/TxId_maxId.csv.xz", sep=',', header=0, compression='xz')
    perc_sum = 0
    tx_notNew_addr = 0
    tx_newAddr = 0
    tx_dust = set(outputs['TxId'].to_list())
    tot_tx = len(outputs.groupby("TxId").count()) #number of transaction where there is success dust
    i = 0
    tx_Id_notNew = []
    for tx in tx_dust:
        maxId = tx_MaxId[tx_MaxId.TxId == tx]['prevMaxId'].iloc[0]
        out = outputs[outputs.TxId == tx]
        tot_addr = len(set(out['addrId'].to_list())) #tot addr in a tx
        new_addr = len(set(out[out.addrId > maxId]['addrId'].to_list()))
        old_addr = tot_addr - new_addr
        if(new_addr == 0):
            tx_notNew_addr += 1
            tx_Id_notNew.append(tx)
        else:
            tx_newAddr += 1
            perc_sum += float(old_addr/tot_addr)*100
        print(i)
        i += 1

    print("PERCENTUALE MEDIA DI INDIRIZZI NON NUOVI PER TX: ", float(perc_sum/tot_tx))
    print("TOTALE TX: ", tot_tx)
    print("TX CON NUOVI INDIRIZZI: ", tx_newAddr)
    print("TX SENZA NUOVI INDIRIZZI: ", tx_notNew_addr)

    with open("../tx_notNew.txt", 'w+') as file:
        for tx in tx_Id_notNew:
            file.write("%d\n" %tx)

def main():
    spent = pd.read_csv("../data_csv/spent_dust.csv.xz", sep=',', header=0, compression='xz')
    unspent = pd.read_csv("../data_csv/unspent_dust.csv.xz", sep=',', header=0, compression='xz')
    categories(spent, unspent)
    new_addresses(spent, unspent)
    return 0



if __name__ == '__main__':
    main()