import pandas as pd

inputs_rename = inputs.rename(columns = {'TxId':'spentTxId', 
        'blockId':'spentBlock', 
        'timestamp' :'spentTimestamp', 
        'prevTxId':'TxId', 
        'prevTxOffset':'offset'})
result = pd.merge(outputs, inputs_rename, 
         on=['TxId', 'addrId', 'amount', 'offset'],
         how='left', indicator=False)
result['spentTxId'] = result['spentTxId'].fillna(-1)
.astype(int)
result['spentBlock'] = result['spentBlock'].fillna(-1)
.astype(int)
result['spentTimestamp'] = result['spentTimestamp']
.fillna(-1).astype(int)
spent = result[result.spentTxId != -1]
unspent = result[result.spentTxId == -1]