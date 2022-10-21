import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    datiIn = pd.read_csv("../data_csv/inputs.csv.xz", sep=',', header=0, compression='xz')
    datiOut = pd.read_csv("../data_csv/outputs.csv.xz", sep=',', header=0, compression='xz')
    
    figure, axi = plt.subplots(1, 2)

    datiIn.groupby('TxId').count()['addrId'].plot.hist(bins=100, logy=True, ax=axi[0], title='Distribuzione Numero di Input', edgecolor='black', linewidth=0.2)
    datiOut.groupby('TxId').count()['addrId'].plot.hist(bins=100, logy=True, color='green', ax=axi[1], title='Distribuzione Numero di Output', edgecolor='black', linewidth=0.2)

    plt.show()

if __name__ == "__main__":
    main()