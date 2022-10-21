import sys

counter = 0
counter_sd = 0
counter_notSD = 0

#inputs := 0 or more input semicolon';' separated where input := addrId','amount','prevTxSpending',' position_of_output_in_prevTxSpending
#outputs := 1 or more output semicolon';' separated where output := addrId','amount',' scriptType
def isDust(in_out: str) -> bool:
    if (in_out != ''): #check if string is not empty
        for input in in_out.split(';'):
            values = input.split(',')
            amount = int(values[1])
            if(amount >= 1 and amount <= 545): #check if is dust
                return True
        return False      
    return False

def is_SD(in_out, ids:list) -> bool:
    if (in_out != ''): #check if string is not empty
        for input in in_out.split(';'):
            values = input.split(',')
            addrID = int(values[0])
            if(addrID in ids): #check if is SD
                return True
        return False      
    return False

def filter(fileSource, fileDestination):
    #line = infos':'inputs':'outputs
    for line in fileSource:
        tx = line.split(':')
        if(isDust(tx[1]) or isDust(tx[2])):
            global counter
            counter = counter + 1
            fileDestination.write(line)

def filter_SD(src, dst, dstSD, ids):
    #line = infos':'inputs':'outputs
    for line in src:
        tx = line.split(':')
        if((not is_SD(tx[1], ids)) and (not is_SD(tx[2], ids))):
            dst.write(line)
            global counter_notSD
            counter_notSD += 1
        else:
            dstSD.write(line)
            global counter_sd
            counter_sd += 1

def ID_SD(file_src) -> list:
    id = []
    for line in file_src:
        fields = line.split(",")
        id.append(int(fields[1]))
    
    return id        

def main():
    source = None
    txDust = open("../txDust.txt", 'w+')

    try:    
        source = open(sys.argv[1], 'r') #file to filter
    except FileNotFoundError as not_found:
        print(not_found.filename + " doesn't exist")

    filter(source, txDust)
    source.close()
    txDust.close()
    print("Total txDust = %d" %counter)

    txDust = open("../txDust.txt", 'r')
    sd_file = open("../dust_SD.txt", 'w+')
    notSD_file = open("../dust_notSD.txt", 'w+')
    fileMap = open("../SDtoID.txt", 'r')
    identifiers_SD = ID_SD(fileMap)

    filter_SD(txDust, notSD_file, sd_file, identifiers_SD)

if __name__ == "__main__":
    main()



