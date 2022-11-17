def analyze_success(df):
        dft = df.copy()
        dft = dft[dft.timestamp == year]
        dft.groupby("TxId").count()['addrId'].mean()) #mean input
        dg = dft.groupby("TxId").count()
        dg['amount'] = df[df.amount <= 545].groupby("TxId").count()['amount'] / dft.groupby("TxI").count()['amount']
        dg['amount'].mean()*100 #mean percentage dust
        dft.groupby("TxId").agg({'addrId':'nunique'})['addrId'].mean() #mean different addresses