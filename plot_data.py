import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    inputs = pd.read_csv("../data_csv/input_composition.csv", sep=',', header=0)
    outputs = pd.read_csv("../data_csv/output_composition.csv", sep=',', header=0)
    dust_out = pd.read_csv("../data_csv/outputs_dust.csv.xz", sep=',', header=0, compression='xz')
    dust_in = pd.read_csv("../data_csv/inputs_dust.csv.xz", sep=',', header=0, compression='xz')
    
    dati_in = dust_in.groupby("TxId").count()
    dati_out = dust_out.groupby("TxId").count()
    hist_bins = np.arange(0, 3100, 50)
    
    print(outputs.head())
    print(inputs.head())

    fig = plt.figure(figsize=(10,10))
    ax1 = fig.add_subplot(1, 4, 1) #input dust histogram
    ax1.set_title('Distribuzione Input Dust') 
    ax1.set_xlabel('N. di Input Dust')
    ax1.set_yscale('log')
    ax1.set_ylabel("N. di Transazioni")
    ax1.hist(dati_in['addrId'].to_list(), bins=hist_bins, edgecolor='black', linewidth=0.1)

    ax2 = fig.add_subplot(1, 4, 2, sharey=ax1) #output dust hstogram
    ax2.set_title('Distribuzione Output Dust') 
    ax2.set_xlabel('N. di Output Dust')
    ax2.set_yscale('log')
    ax2.hist(dati_out['addrId'].to_list(), bins=hist_bins, color='green', edgecolor='black', linewidth=0.1)
    
    ax3 = fig.add_subplot(1, 4, 3) #perc inputs
    ax3.margins(0, 0)
    sd = inputs.groupby('count_tot').mean()['count_dust']
    print(sd)
    sn = (sd.index.to_series())-sd
    data = pd.DataFrame({'dust':sd,'not-dust':sn})
    data_perc = data.divide(data.sum(axis=1), axis=0)
    
    plt.setp(ax2.get_yticklabels(), visible=False)
    #plt.show()

if __name__ == "__main__":
    main()