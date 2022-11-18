import pandas as pd

def ID_SD(file_src) -> list:
    id = []
    for line in file_src:
        fields = line.split(",")
        id.append(int(fields[1]))
    
    return id 

def main():
    fileMap = open("../SDtoID.txt", 'r')
    identifiers_SD = ID_SD(fileMap)
    sd = pd.read_csv("../data_csv/inputs_SD.csv.xz", sep=',', header=0, compression='xz')
    sd = sd[sd.addrId.isin(identifiers_SD)]
    sd_txs = sd['TxId'].to_list()#all TxId with SD as input

    spent = pd.read_csv("spent_dust.csv.xz", sep=',', header=0, compression='xz')
    unsp = pd.read_csv("unspent_dust.csv.xz", sep=',', header=0, compression='xz')   

    unsp = unsp.rename(columns={'spentId':'spentTxId', 'txId':'TxId', 'address':'addrId'})
    spent = spent.rename(columns={'spentId':'spentTxId', 'txId':'TxId', 'address':'addrId'})
    
    unsp = unsp[~unsp.addrId.isin(identifiers_SD)]
    unsp = unsp[unsp.scriptType != 4]
    unsp = unsp[~unsp.TxId.isin(sd_txs)]

    spent = spent[~spent.TxId.isin(sd_txs)]
    spent = spent[~spent.addrId.isin(identifiers_SD)]

    spent.to_csv("../data_csv/spent_dust.csv", index=False)
    unsp.to_csv("../data_csv/unspent_dust.csv", index=False)


if __name__ == "__main__":
    main()

"""
code to use with all dataset
inputs_mod = inputs[['txId', 'blockId', 'timestamp', 'prevTxId', 'address', 'amount', 'prevTxOffset']]
inputs_mod = inputs_mod.rename(columns = {'TxId':'spentTxId', 'blockId':'spentBlock', 'timestamp':'spentTimestamp', 'prevTxId':'TxId', 'prevTxOffset':'offset'})
inputs_mod.head()
result = pd.merge(outputs, inputs_mod, on=['TxId', 'addrId', 'amount', 'offset'], how='left', indicator=False)
result['spentTxId']=result['spentTxId'].fillna(-1).astype(int)
result['spentBlock']=result['spentBlock'].fillna(-1).astype(int)
result['spentTimestamp']=result['spentTimestamp'].fillna(-1).astype(int)
result.head()
spent = result[result.spentTxId != -1]
unspent = result[result.spentTxId == -1]
unspent.to_csv('dust/unspent_dust.csv', index=False)
unspent.head()
"""
