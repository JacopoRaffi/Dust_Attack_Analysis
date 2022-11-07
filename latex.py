import pandas as pd

spent = pd.read_csv("../data_csv/spent_dust.csv.xz", sep=',', header=0, compression='xz')
unspent = pd.read_csv("../data_csv/unspent_dust.csv.xz", sep=',', header=0, compression='xz')

print(spent.head())
print(unspent.head())