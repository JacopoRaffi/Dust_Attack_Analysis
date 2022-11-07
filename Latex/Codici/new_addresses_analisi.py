for tx in tx_dust:
        maxId = tx_MaxId[tx_MaxId.TxId == tx]['prevMaxId'].iloc[0] #prevMaxId
        out = outputs[outputs.TxId == tx]
        tot_addr = len(set(out['addrId'].to_list())) #tot addr in a tx
        new_addr = len(set(out[out.addrId > maxId]['addrId'].to_list())) #tot new addresses in a tx
        old_addr = tot_addr - new_addr
        if(new_addr == 0):
            tx_notNew_addr += 1
            tx_Id_notNew.append(tx)
        else:
            tx_newAddr += 1
            perc_sum += float(old_addr/tot_addr)*100
float(perc_sum/tot_tx)
