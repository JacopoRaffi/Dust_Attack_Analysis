import pandas as pd
import matplotlib.pyplot as plt
import sys

def main():
    inputs_file = sys.argv[1]
    outputs_file = sys.argv[2]

    inputs = pd.read_csv(inputs_file, sep=',', header=0, compression='xz')
    outputs = pd.read_csv(outputs_file, sep=',', header=0, compression='xz')
    
    figure, axi = plt.subplots(1, 2)

    ax = inputs.groupby('TxId').count()['addrId'].plot.hist(bins=100, logy=True, ax=axi[0], title='Distribuzione Numero di Input Dust', edgecolor='black', linewidth=0.2)
    ax1 = outputs.groupby('TxId').count()['addrId'].plot.hist(bins=100, logy=True, color='green', ax=axi[1], title='Distribuzione Numero di Output Dust', edgecolor='black', linewidth=0.2)

    ax.set_ylabel("N. di Transazioni")
    ax1.set_ylabel("N. di Transazioni")

    plt.show()

if __name__ == "__main__":
    main()