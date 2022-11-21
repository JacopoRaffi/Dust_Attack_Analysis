for tx in tx_dust:
    maxId = tx_MaxId[tx_maxId.TxId == tx]['prevMaxAddrId']
    out = outputs_dust[outputs_dust.TxId == tx]
    tot_addr = len(out['addrId'].to_list()) 
    new_addr = len(out[out.addrId > maxId]['addrId'].to_list())
    old_addr = tot_addr - new_addr
    
    if(not new_addr):
        tx_notNew_addr += 1
        tx_Id_notNew.append(tx)
    else:
        tx_newAddr += 1
        perc_sum += (old_addr/tot_addr)*100

perc_mean = perc_sum / tot_tx
