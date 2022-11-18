import sys
import csv

def isDust(in_out: str) -> bool:
    if (in_out != ''): #check if string is not empty
        for fields in in_out.split(';'):
            values = fields.split(',')
            amount = int(values[1])
            if(amount >= 1 and amount <= 545): #check if is dust
                return True
        return False      
    return False

def write_data(wrt, file):
    max_id = 0
    for line in file:
        fields = line.split(":")
        infos =  fields[0] 
        outputs = fields[2] #check max id in outputs 
        if(isDust(outputs)):
            txId = int(infos.split(",")[2])
            lst = [txId, max_id]
            wrt.writerow(lst)

        for output in outputs.split(";"):
            addr = int(output.split(",")[0])
            if(addr > max_id):
                max_id = addr
        

def main():
    filename = sys.argv[1]
    filename_csv = "../data_csv/TxId_maxId.csv"
    file = open(filename, 'r')
    file_csv = open(filename_csv, 'w+')
    writer = csv.writer(file_csv)
    header = ['TxId', 'prevMaxId']
    writer.writerow(header)

    write_data(writer, file)

if __name__ == '__main__':
    main()
