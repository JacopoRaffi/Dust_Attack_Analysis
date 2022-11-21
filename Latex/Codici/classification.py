tx_special = collect_tx("TxId_special.txt")
inputs = inputs[~inputs.TxId.isin(tx_special)]

for year in range(2010, 2018):
    inp = inputs[inputs.timestamp == year] 
    inp = inp.groupby("TxId").agg({'addrId':'nunique'})
    
    categories[year][0] += len(inp[addrId >= 2])   
    categories[year][1] += len(inp[addrId == 1])