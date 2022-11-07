import pandas as pd

#intialize dict for temporal statistics
categories = {}
for i in range(2010, 2022):
    #year -> [success, fail, special]
    categories[i] = [0, 0, 0]
    
def classification(inputs, spent, tx_sp):
    txs = set(spent['spentTxId'].to_list()) #take all txs in a set(to avoid repetition)
    inputs = inputs[inputs.TxId.isin(txs)] # all tx with at least one dust input not from Satoshi Dice
    inputs = inputs[~inputs.TxId.isin(tx_sp)] #avoid special Tx checked before
    
    for year in range(2010, 2022):
        inp = inputs[inputs.timestamp == year] #all data in one year 
        inp = inp.groupby("TxId").agg({'addrId':'nunique'})
        
        #success of a possible dust attack
        categories[year][0] += len(inp[inp.addrId >= 2]) 
        #fail of a possible dust attack
        categories[year][1] += len(inp[inp.addrId == 1]) 