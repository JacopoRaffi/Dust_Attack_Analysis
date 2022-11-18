import csv

def howManyDust(in_out: str) -> int:
    count_dust = 0
    count = 0
    if (in_out != ''): #check if string is not empty
        for fields in in_out.split(';'):
            values = fields.split(',')
            amount = int(values[1])
            if(amount >= 1 and amount <= 545): #check if is dust
                count_dust += 1    
            count += 1  
    return count,count_dust

def write_composition(wrtI, wrtO, src):
    for line in src:
        fields = line.split(":")
        infos = fields[0].split(",")
        txid = int(infos[2])

        tot_inp,tot_dustIn = howManyDust(fields[1])
        tot_out,tot_dustOut = howManyDust(fields[2])
        wrtI.writerow([txid, tot_inp, tot_dustIn])
        wrtO.writerow([txid, tot_out, tot_dustOut])

def main():
    fileIn = open("../data_csv/input_composition.csv", 'w+')
    fileOut = open("../data_csv/output_composition.csv", 'w+')
    file_src = open("../dust_notSD.txt", 'r')

    writerIn = csv.writer(fileIn)
    writerOut = csv.writer(fileOut)
    header = ['TxId', 'count_tot', 'count_dust']
    writerIn.writerow(header)
    writerOut.writerow(header)

    write_composition(writerIn, writerOut, file_src)

    file_src.close()
    fileIn.close()
    fileOut.close()
    return 0

if __name__ == '__main__':
    main()
