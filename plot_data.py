import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    df = pd.read_csv("../data_csv/input_composition.csv", sep=',', header=0)
    df2 = pd.read_csv("../data_csv/output_composition.csv", sep=',', header=0)
    out = pd.read_csv("../data_csv/outputs.csv.xz", sep=',', header=0, compression='xz')
    inp = pd.read_csv("../data_csv/inputs.csv.xz", sep=',', header=0, compression='xz')
    
    dati_in = inp[inp.amount <= 545].groupby("TxId").count()
    dati_out = out[out.amount <= 545].groupby("TxId").count()
    hist_bins = np.arange(0, 4400, 50)
    hist_out = np.arange(0, 13150, 200)
    hist_dust = np.arange(0, 1500, 60)
    hist_dustOut = np.arange(0, 3500, 200)
    fig = plt.figure(figsize=(18,4))
    fig2 = plt.figure(figsize=(18,4))

    ax1 = fig.add_subplot(1, 2, 1) #input dust histogram
    ax1.set_title('Distribuzione Input') 
    ax1.set_xlabel('N. di Input')
    ax1.set_yscale('log')
    ax1.set_ylabel("N. di Transazioni")
    ax1.margins(0,0)
    ax1.hist(dati_in['addrId'].to_list(), bins=hist_dust, edgecolor='black', linewidth=0.1)
    
    ax2 = fig.add_subplot(1, 2, 2)
    df['perc_dust'] = df['count_dust'] / df['count_tot']
    df['bins'] = pd.cut(df['count_tot'], bins=hist_bins)
    df = df.groupby("bins").mean()
    df['perc_nonDust'] = 1-df['perc_dust']
    dg = pd.DataFrame({'dust':df['perc_dust'].to_list(),'nondust':df['perc_nonDust'].to_list()})
    dg.index = dg.index * 50
    dg.plot.bar(stacked=True, color=['#648fff','#dc267f'], ax=ax2)
    ax2.set_title('Percentuale input nelle transazioni che consumano dust')
    ax2.set_xlabel('N. di input')
    ax2.set_ylabel('Media %')
    ax2.margins(0,0)
    ax2.legend(loc='upper left')

    ax3 = fig2.add_subplot(1, 2, 1) #output dust hstogram
    ax3.set_title('Distribuzione Output') 
    ax3.set_ylabel("N. di Transazioni")
    ax3.set_xlabel('N. di Output')
    ax3.set_yscale('log')
    ax3.hist(dati_out['addrId'].to_list(), bins=hist_dustOut, color='green', edgecolor='black', linewidth=0.1)

    ax4 = fig2.add_subplot(1, 2, 2)
    df2['perc_dust'] = df2['count_dust'] / df2['count_tot']
    df2['bins'] = pd.cut(df2['count_tot'], bins=hist_out)
    df2 = df2.groupby("bins").mean()
    df2['perc_nonDust'] = 1-df2['perc_dust']
    dg2 = pd.DataFrame({'dust':df2['perc_dust'].to_list(),'nondust':df2['perc_nonDust'].to_list()})
    dg2.plot.bar(stacked=True, color=['#648fff','#dc267f'], ax=ax4)
    ax4.set_title('Percentuale output nelle transazioni che creano dust')
    ax4.set_xlabel('N. di output')
    ax4.set_ylabel('Media %')
    ax4.margins(0,0)
    ax4.legend(loc='upper left')
    
    plt.setp(ax4.get_xticklabels(), visible=False)
    plt.setp(ax2.get_xticklabels(), visible=False)
    fig.savefig("distribuzione_input.pdf", format='pdf', bbox_inches='tight')
    fig2.savefig("distribuzione_output.pdf", format='pdf', bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    main()