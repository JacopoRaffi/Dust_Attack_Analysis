def categories(sp, unsp):
    addr_sp = set(sp['addrId'].to_list())
    addr_unsp = set(unsp['addrId'].to_list())
    addr_both = set([])
    addr_os = addr_sp.copy() #os only spent
    addr_ou = addr_unsp.copy() #ou only unspent
    addr_tot = addr_sp.union(addr_unsp)
    print("INDIRIZZI TOTALI: ", len(addr_tot))
    only_sp = len(addr_sp)
    only_unsp = len(addr_unsp)
    both_set = 0
    for addr in addr_sp:
        if(addr in addr_unsp): #it means it is in both set
            only_sp -= 1
            only_unsp -= 1
            both_set += 1 
            addr_both.add(addr)
            addr_os.remove(addr)
            addr_ou.remove(addr)