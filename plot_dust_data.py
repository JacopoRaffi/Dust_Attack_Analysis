import pandas as pd
import matplotlib.pyplot as plt    

def main():
    datiOut = pd.read_csv("../data_csv/outputs_dust.csv.xz", sep=',', header=0, compression='xz')
    datiIn = pd.read_csv("../data_csv/inputs_dust.csv.xz", sep=',', header=0, compression='xz')

    figure, axi = plt.subplots(1, 2)

    ax1 = datiOut.groupby('TxId').count()['addrId'].plot.hist(bins=100, logy=True, color='green', title='Distribuzione Numero di Output Dust', edgecolor='black', linewidth=0.1, ax=axi[1])   
    ax = datiIn.groupby('TxId').count()['addrId'].plot.hist(bins=100, logy=True, title='Distribuzione Numero di Input Dust', edgecolor='black', linewidth=0.1, ax=axi[0]) 
    
    ax.set_ylabel("N. of inputs")
    ax1.set_ylabel("N. of outputs")
    
    plt.show()

if __name__ == "__main__":
    main()

