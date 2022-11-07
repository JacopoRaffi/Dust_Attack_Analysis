def analyze_success(df):
    df["timestamp"] = df['timestamp'].apply(lambda t : datetime.fromtimestamp(t))
    df["timestamp"] = df['timestamp'].apply(lambda y : y.year)
    for year in range(2010, 2022):
        dft = df.copy()
        dft = dft[dft.timestamp == year]
        dft.groupby("TxId").count()['addrId'].mean()) #mean input
        dft.groupby("TxId").count().mode()['addrId'].iloc[0]) #mode input
        dg = dft.groupby("TxId").count()
        dg['amount'] = df[df.amount <= 545].groupby("TxId").count()['amount'] / dft.groupby("TxId").count()['amount']
        dg['amount'].mean()*100 #mean percentage dust
        dft.groupby("TxId").agg({'addrId':'nunique'})['addrId'].mean() #mean different addresses
        dft.groupby("TxId").agg({'addrId':'nunique'})['addrId'].mode().iloc[0] #mode different addresses