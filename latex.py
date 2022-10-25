import pandas as pd

datiIn = pd.read_csv("../data_csv/inputs.csv.xz", sep=',', header=0, compression='xz')
datiOut = pd.read_csv("../data_csv/outputs.csv.xz", sep=',', header=0, compression='xz')
print(datiIn.head().to_latex(index=False))
print(datiOut.head().to_latex(index=False))