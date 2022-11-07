def is_SD(in_out, ids:list) -> bool:
    if (in_out != ''): #check if string is not empty
        for fields in in_out.split(';'):
            values = fields.split(',')
            addrID = int(values[0])
            if(addrID in ids): #check if is SD
                return True
        return False      
    return False

def filter_SD(src, dst, dstSD, ids):
    #line = infos':'inputs':'outputs
    for line in src:
        tx = line.split(':')
        #filter Tx with Satoshi Dice as Input
        if((not is_SD(tx[1], ids))):
            dst.write(line)
        else:
            dstSD.write(line)
