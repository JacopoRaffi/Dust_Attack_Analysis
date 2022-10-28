"""
usoDustNelTempo: aggiungi grafico simile 
ma con numero di outputs invece che numero di txs 
(così possiamo anche vedere quanti rimangono non spesi). 
Per ogni anno/trimestre avrai 
numDustOutputsNonSpesi, numDustOutputsSpesiInTxSuccesso, numDustOutputsSpesiInTxFallimento,  numDustOutputsSpesiInTxSpeciale
"""

import pandas as pd

years = {}
# year -> [success, fail, special, unspent]
def main():
    for y in range(2010, 2022):
        years[y] = [0, 0, 0, 0]

    
    datafr = pd.DataFrame.from_dict(years, orient='index')
    datafr = datafr.rename(columns={0:'Successo', 1:'Fallimento', 2:'Speciale', 3:'Non Speso'})
    print(datafr)

if __name__ == '__main__':
    main()