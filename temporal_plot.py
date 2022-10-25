import pandas as pd
import datetime
import matplotlib.pyplot as plt  
import matplotlib.dates as mdates


#TODO fare istogramma(sovrapposto al primo istogramma) dei dust bruciati(non spesi)
      # nel secondo pezzo mettici istogramma output spesi
def main():
    outputs = pd.read_csv("../data_csv/outputs_dust.csv.xz", sep=',', header=0, compression='xz')
    inputs = pd.read_csv("../data_csv/inputs_dust.csv.xz", sep=',', header=0, compression='xz')
    spent = pd.read_csv("../data_csv/spent_dust.csv.xz", sep=',', header=0, compression='xz')
    unspent = pd.read_csv("../data_csv/unspent_dust.csv.xz", sep=',', header=0, compression='xz')
    
    outputs = outputs[outputs['amount'] != 0]
    outputs = outputs[outputs['script'] != 4]
    inputs = inputs[inputs.amount != 0]

    #grafico dust generati nel tempo(dust spendibile)
    outputs['timestamp'] = outputs['timestamp'].apply(lambda t : datetime.datetime.fromtimestamp(t))
    spent['timestamp'] = spent['timestamp'].apply(lambda t : datetime.datetime.fromtimestamp(t))
    out = mdates.date2num(outputs['timestamp'].values)
    sp = mdates.date2num(spent['timestamp'].values)

    years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
    months = [i for i in range(1, 12+1, 3)]
    bins = []
    for y in years:
        for m in months:
            bins.append(datetime.date(y, m, 1))
    hist_bins = mdates.date2num(bins)

    fig = plt.figure()
    ax1 = fig.add_subplot()
    ax1.set_title('Creazione dust')
    ax1.set_xlabel('Anno')
    ax1.set_ylabel('N. of outputs')
    ax1.set_yscale('log')
    ax1.xaxis.set_major_locator(mdates.YearLocator())
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax1.hist(out, bins=hist_bins, color='green', label='Dust Generato', edgecolor='black', linewidth=0.1)
    ax1.legend(loc='upper left')
    
    plt.show()
    return 0

if __name__ == "__main__":
    main()