import pandas as pd

def classification(spent, unspent):
    #all special TxId
    tx_sp = collect_tx("../tx_special.txt")
    #all spent success TxId
    tx_success = collect_tx("../tx_spent_dust.txt")

    spent_succ = spent[spent.spentTxId.isin(tx_success)] 
    spent_failed = spent[~spent.spentTxId.isin(tx_success)]
    spent_failed = spent_failed[~spent_failed.spentTxId.isin(tx_sp)]
    spent_special = spent[spent.spentTxId.isin(tx_sp)]


    for year in range(2010, 2022):
        unsp = unspent[unspent.timestamp == year]
        years[year][3] += len(unsp) #not-spent

        succ = spent_succ[spent_succ.spentTimestamp == year]
        years[year][0] += len(succ) #success

        failed = spent_failed[spent_failed.spentTimestamp == year]
        years[year][1] += len(failed) #failed

        special = spent_special[spent_special.spentTimestamp == year]
        years[year][2] += len(special) #special