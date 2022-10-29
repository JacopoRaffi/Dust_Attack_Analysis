import pandas as pd

#TODO
"""
- attacchi di successo: considera percentuale di address destinatari di dust che NON compaiono per la prima volta on chain per quella transazione
- Nelle transazioni che generano output dust gurda, per ogni transazione, %speso e dello speso guarda %successo e %fallito 
- Contare addresses totali, calcolare %vittime successo, %fallimento, %speciale
"""

def collect_tx(filename):
    txs = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            tx = int(line)
            txs.append(tx)
    return txs

def analyze_spent(addresses):
    print("TOT ADDR: ", len(addresses))
    inputs = pd.read_csv("../data_csv/inputs.csv.xz", sep=',', header=0, compression='xz')
    tx_success = collect_tx("../tx_spent_dust.txt")
    tx_sp = collect_tx("../tx_special.txt")
    spent = pd.read_csv("../data_csv/spent_dust.csv.xz", sep=',', header=0, compression='xz')
    sp = spent[~spent.spentTxId.isin(tx_success)]
    sp = sp[~sp.spentTxId.isin(tx_sp)]

    addr_failed = set(inputs[inputs.TxId.isin(sp['spentTxId'].to_list())]['addrId'].to_list())
    addr_succ = set(inputs[inputs.TxId.isin(tx_success)]['addrId'].to_list())
    addr_spec = set(inputs[inputs.TxId.isin(tx_sp)]['addrId'].to_list())

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
    analyze_spent(addr_os)

    print("NOT ONLY SPENT ADDRESSES: ")
    analyze_spent(addr_both)


def main():
    spent = pd.read_csv("../data_csv/spent_dust.csv.xz", sep=',', header=0, compression='xz')
    unspent = pd.read_csv("../data_csv/unspent_dust.csv.xz", sep=',', header=0, compression='xz')

    categories(spent, unspent)
    return 0



if __name__ == '__main__':
    main()