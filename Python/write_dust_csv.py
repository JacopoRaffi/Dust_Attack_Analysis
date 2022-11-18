import pandas as pd

def ID_SD(file_src) -> list:
    id = []
    for line in file_src:
        fields = line.split(",")
        id.append(int(fields[1]))

    return id

def main(): #also some simple data
    datiIn = pd.read_csv("../data_csv/inputs.csv.xz", sep=',', header=0, compression='xz')
    datiOut = pd.read_csv("../data_csv/outputs.csv.xz", sep=',', header=0, compression='xz')
    fileMap = open("../SDtoID.txt", 'r')
    identifiers_SD = ID_SD(fileMap)

    outputs = datiOut[~datiOut.addrId.isin(identifiers_SD)]
    print("Totale Input: ", len(datiIn))
    print("Totale Output: ", len(outputs))
    
    #delete dust from SD
    sd = pd.read_csv("../data_csv/inputs_SD.csv.xz", sep=',', header=0, compression='xz')
    sd = sd[sd.addrId.isin(identifiers_SD)]
    sd_txs = sd['TxId'].to_list()#all TxId with SD as input
    
    inputs = datiIn[datiIn.amount <= 545]
    inputs = inputs[inputs.amount != 0]
    outputs = datiOut[datiOut.amount <= 545]
    outputs = outputs[outputs.amount != 0]

    inputs = inputs[~inputs.prevTxId.isin(sd_txs)]
    outputs = outputs[~outputs.addrId.isin(identifiers_SD)]
    outputs = outputs[outputs.script != 4]

    print("Totale Input dust: ", len(inputs))
    print("Totale Output dust spendibile: ", len(outputs))

    #write dust data in csv file
    inputs.to_csv("../data_csv/inputs_dust.csv", index=False)
    outputs.to_csv("../data_csv/outputs_dust.csv", index=False)


if __name__ == "__main__":
    main()
