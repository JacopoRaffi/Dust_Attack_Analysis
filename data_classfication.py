import pandas as pd
from datetime import datetime

classes = {}
# key = year, value = [success, failed, burned, special]

def isDust(in_out: str) -> bool:
    if (in_out != ''): #check if string is not empty
        for input in in_out.split(';'):
            values = input.split(',')
            amount = int(values[1])
            if(amount >= 1 and amount <= 545): #check if is dust
                return True
        return False      
    return False

# 0->sucess; 1->failed; 2->burned; 3->special(dust collecting or other)
def tx_category(infos, inputs, outputs):



def classification(file):
    for line in file:
        fields = line.split(":")
        infos = fields[0].split(",")
        timestamp = int(infos[0])
        year = datetime.fromtimestamp(timestamp).year
        outputs = fields[2]
        inputs = fields[1]
        if(len(inputs.split(";")) > 1 and isDust(inputs)):
            index = tx_category(infos, inputs, outputs)
            classes[year][index] += 1
    


def main():
    #intialize dict for temporal statistics
    for i in range(2010, 2022):
        classes[i] = [0, 0, 0, 0]

    file = open("../dust_notSD.txt", 'r')
    classification(file)
    return 0

if __name__ == "__main__":
    main()