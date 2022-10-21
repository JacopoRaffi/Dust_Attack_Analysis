from nbformat import write
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt    

def main():
    datiOut = pd.read_csv("../data_csv/outputs_dust.csv.xz", sep=',', header=0, compression='xz')
    datiIn = pd.read_csv("../data_csv/inputs_dust.csv.xz", sep=',', header=0, compression='xz')
    datiOut = datiOut[datiOut['amount'] != 0]
    datiOut = datiOut[datiOut['script'] != 4]
    datiIn = datiIn[datiIn.amount != 0]

    figure, axi = plt.subplots(1, 2)

    datiOut.groupby('TxId').count()['addrId'].plot.hist(bins=200, logy=True, color='green', title='Distribuzione Numero di Output Dust', edgecolor='black', linewidth=0.1, ax=axi[0])   
    datiIn.groupby('TxId').count()['addrId'].plot.hist(bins=200, logy=True, title='Distribuzione Numero di Input Dust', edgecolor='black', linewidth=0.1, ax=axi[1]) 
    plt.show()

if __name__ == "__main__":
    main()

