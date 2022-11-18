import pandas as pd

def collect_tx(filename):
    txs = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            tx = int(line)
            txs.append(tx)
    return txs

def main():
    tx_notNew = collect_tx("../tx_notNew.txt")
    maxId = pd.read_csv("../data_csv/TxId_maxId.csv.xz", sep=',', header=0, compression='xz')

if __name__ == '__main__':
    main()
