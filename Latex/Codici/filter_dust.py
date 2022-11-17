for line in source:
    tx = line.split(':')
    inputs = tx[1]
    outputs = tx[2]
    if(isDust(inputs) or isDust(outputs)):
        destination.write(line)