def isDust(in_out: str) -> bool:
    #check if string is not empty
    if (in_out != ''): 
        for fields in in_out.split(';'):
            values = fields.split(',')
            amount = int(values[1])
            #check if is dust
            if(amount >= 1 and amount <= 545): return True
        return False      
    return False

def filter(fileSource, fileDestination):
    #line = infos':'inputs':'outputs
    for line in fileSource:
        tx = line.split(':')
        if(isDust(tx[1]) or isDust(tx[2])):
            fileDestination.write(line)