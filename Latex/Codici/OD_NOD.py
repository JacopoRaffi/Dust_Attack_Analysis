def classify(df): #df is dataframe with inputs(failed or success)
    df_t = df[df.amount > 545]
    txs_nod = set(df_t['TxId'].to_list()) #all TxId with at least one input non-dust
    tot = len(set(df['TxId'].to_list()))
    len(txs_nod) #NOD
    len(set(df['TxId'].to_list())) - len(txs_nod) #OD = TOTAL - NOD