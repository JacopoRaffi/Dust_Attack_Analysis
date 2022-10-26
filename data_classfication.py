import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

categories = {}
# key = year, value = [success, failed, special]
# 0->sucess; 1->failed; 2->special(dust collecting or other) 

# tx where all input become fee
def special_tx(file):
    sp_tx = []
    for line in file:
        fields = line.split(":")
        txid = int(fields[0].split(",")[2])
        inputs = fields[1]
        fee = int(fields[0].split(",")[4])
        if(len(inputs.split(";")) > 1):
            tot_amount = 0
            for input in inputs.split(";"):
                tot_amount += int(input.split(",")[1])
            
            if(tot_amount == fee):
                sp_tx.append(txid)
    
    return sp_tx 

def classification(inputs, spent, tx_sp=[]):
    #file_txs = open("../tx_spent_dust.txt", 'w+')
    txs = set(spent['spentTxId'].to_list()) #take all txs in a set(to avoid repetition)
    inputs = inputs[inputs.TxId.isin(txs)] # all tx with at least one dust input not from Satoshi Dice
    inputs = inputs[~inputs.TxId.isin(tx_sp)] #avoid special Tx checked before
    
    for year in range(2010, 2022):
        inp = inputs[inputs.timestamp == year] #all data in one year 
        inp = inp.groupby("TxId").agg({'addrId':'nunique'})
        
        categories[year][0] += len(inp[inp.addrId >= 2]) #success
        categories[year][1] += len(inp[inp.addrId == 1]) #failed
        #for tx_spent in inp[inp.addrId >= 2].index.to_list(): #save in a file all tx with at least two inputs(for future analysis)
         #   file_txs.write("%s\n" %tx_spent)

    #file_txs.close()

def main():
    #intialize dict for temporal statistics
    for i in range(2010, 2022):
        categories[i] = [0, 0, 0]
    
    inputs = pd.read_csv("../data_csv/inputs.csv.xz", sep=',', header=0, compression='xz')
    spent = pd.read_csv("../data_csv/spent_dust.csv.xz", sep=',', header=0, compression='xz')
    file = open("../txDust.txt", 'r')
    tx_sp = special_tx(file)
    
    #change timestamp to year to analyze every year what happens
    spent["spentTimestamp"] = spent['spentTimestamp'].apply(lambda t : datetime.fromtimestamp(t))
    spent["spentTimestamp"] = spent['spentTimestamp'].apply(lambda y : y.year)
    inputs["timestamp"] = inputs['timestamp'].apply(lambda t : datetime.fromtimestamp(t))
    inputs["timestamp"] = inputs['timestamp'].apply(lambda y : y.year)

    txs = set(spent['spentTxId'].to_list())
    df = inputs[inputs.TxId.isin(txs)].groupby("TxId").count()
    print("Transazioni, con almeno 2 input, in cui viene speso il dust: ", len(df))
    classification(inputs, spent, tx_sp)

    for tx in tx_sp:
        year = spent[spent.spentTxId == tx]['spentTimestamp'].values[0]
        categories[year][2] += 1
    
    print(categories)
    datafr = pd.DataFrame.from_dict(categories, orient='index')
    datafr = datafr.rename(columns={0:'Almeno due indirizzi', 1:'Un indirizzo', 2:'speciale'})
    datafr.plot(use_index=True, y=["Almeno due indirizzi", "Un indirizzo", "speciale"], kind="bar",figsize=(9,8), title="Uso del dust nel tempo", logy=True)
    plt.show()

    return 0

if __name__ == "__main__":
    main()