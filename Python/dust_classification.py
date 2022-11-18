import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

years = {}

def collect_tx(filename):
    txs = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            tx = int(line)
            txs.append(tx)
    return txs

def classification(spent, unspent):
    #all special TxId
    tx_sp = collect_tx("../tx_special.txt")
    #all spent success TxId
    tx_success = collect_tx("../tx_spent_dust.txt")

    spent_succ = spent[spent.spentTxId.isin(tx_success)] 
    spent_failed = spent[~spent.spentTxId.isin(tx_success)]
    spent_failed = spent_failed[~spent_failed.spentTxId.isin(tx_sp)]
    spent_special = spent[spent.spentTxId.isin(tx_sp)]


    for year in range(2010, 2018):
        unsp = unspent[unspent.timestamp == year]
        years[year][3] += len(unsp) #not-spent

        succ = spent_succ[spent_succ.spentTimestamp == year]
        years[year][0] += len(succ) #success

        failed = spent_failed[spent_failed.spentTimestamp == year]
        years[year][1] += len(failed) #failed

        special = spent_special[spent_special.spentTimestamp == year]
        years[year][2] += len(special) #special

    return 0

# year -> [success, fail, special, unspent]
def main():
    for y in range(2010, 2018):
        years[y] = [0, 0, 0, 0]

    spent = pd.read_csv("../data_csv/spent_dust.csv.xz", sep=',', header=0, compression='xz')
    unspent = pd.read_csv("../data_csv/unspent_dust.csv.xz", sep=',', header=0, compression='xz')

    #change timestamp to year to analyze every year what happens
    spent["spentTimestamp"] = spent['spentTimestamp'].apply(lambda t : datetime.fromtimestamp(t))
    spent["spentTimestamp"] = spent['spentTimestamp'].apply(lambda y : y.year)
    unspent["timestamp"] = unspent['timestamp'].apply(lambda t : datetime.fromtimestamp(t))
    unspent["timestamp"] = unspent['timestamp'].apply(lambda y : y.year)
    
    classification(spent, unspent)
    df = pd.DataFrame.from_dict(years, orient='index')
    df = df.rename(columns={0:'Successo', 1:'Fallimento', 2:'Speciale', 3:'Non Speso'})
    df.plot(use_index=True, y=["Successo", "Fallimento", "Speciale", "Non Speso"], kind="bar", figsize=(9,8), title="Uso del dust nel tempo", logy=True, ylabel="N. di dust")
    plt.savefig("../Grafici/uso_del_dust_new.pdf", format='pdf', bbox_inches='tight')
    plt.show()

if __name__ == '__main__':
    main()
