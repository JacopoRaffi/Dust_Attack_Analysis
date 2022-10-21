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