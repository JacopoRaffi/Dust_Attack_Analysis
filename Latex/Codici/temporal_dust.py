tx_failed = collect_tx("TxId_success.txt")
tx_special = collect_tx("TxId_failed.txt")
tx_success = collect_tx("TxId_special.txt")

success_dust = spent[spentTxId.isin(tx_success)]
failed_dust = spent[spentTxId.isin(tx_failed)]
special_dust = spent[spentTxId.isin(tx_special)]

for year in range(2010, 2018):
    unsp = unspent[unspent.timestamp == year]
    years[year][3] += len(unsp) 
    
    succ = spent_succ[spentTimestamp == year]
    years[year][0] += len(success_dust) 

    failed = spent_failed[spentTimestamp == year]
    years[year][1] += len(failed_dust) 

    special = spent_special[spentTimestamp == year]
    years[year][2] += len(special_dust) 