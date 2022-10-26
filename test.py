import pandas as pd
outputs = pd.read_csv("../data_csv/spent_dust.csv.xz", sep=',', header=0, compression='xz')
print(outputs.head(n=1))