import csv

def writeData(dstI, dstO, src):
    for line in src:
        fields = line.split(":")
        infos = fields[0].split(",")
        info = [infos[0]] + [infos[1]] + [infos[2]]
        inputs = fields[1].split(";")
        outputs = fields[2].split(";")

        if('' not in inputs):
            for input in inputs:
                ins = input.split(",")
                dstI.writerow(info + ins)
        
        for output in outputs:
            out = output.split(",")
            out[2] = out[2].strip()
            dstO.writerow(info + out)


def main():
    csv_in = open("../data_csv/inputs.csv", 'w+')
    csv_out = open("../data_csv/outputs.csv", 'w+')
    fileInput = open("../dust_notSD.txt", 'r')

    writerIn = csv.writer(csv_in)
    writerOut = csv.writer(csv_out)

    headerIn = ['timestamp', 'blockId', 'TxId', 'addrId', 'amount', 'prevTxId', 'offset']
    headerOut = ['timestamp', 'blockId', 'TxId', 'addrId', 'amount', 'script']

    writerIn.writerow(headerIn)
    writerOut.writerow(headerOut)
    writeData(writerIn, writerOut, fileInput)

if __name__ == "__main__":
    main()
