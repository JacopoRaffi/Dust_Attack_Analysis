for tx in tx_dust:
    maxId = tx_MaxId[TxId == tx]['prevMaxAddrId']
    out = outputs_dust[TxId == tx]
    tot_addr = len(out['addrId'].to_set()) 
    new_addr = len(out[addrId > maxId]['addrId'].to_set())
    old_addr = tot_addr - new_addr
    
    if(new_addr == 0):
        tx_notNew_addr += 1
        tx_Id_notNew.append(tx)
    else:
        tx_newAddr += 1
        perc_sum += (old_addr/tot_addr)*100

perc_mean = perc_sum / tot_tx
