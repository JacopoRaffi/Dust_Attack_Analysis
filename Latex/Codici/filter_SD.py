for line in source:
    tx = line.split(':')
    inputs = tx[1]
    if((not is_SD(inputs, SD_ids))):
        destination.write(line)
