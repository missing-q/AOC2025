def validate(ranges, ids): #takes in a list of ranges in tuple form and a list of IDs, returns the number of valid IDs
    count = 0
    for i in ids:
        for j in ranges:
            if i in range(j[0], j[1]+1):
                count += 1
                break
    return count

if __name__ == "__main__":
    #file = "day5sample.txt"
    file = "day5input.txt"
    cont = open(f"inputs/{file}").read().split("\n\n")
    rangeInputs = cont[0].split('\n')
    idInputs = cont[1].split('\n')

    #formatting each list
    for i, val in enumerate(rangeInputs):
        tmp = val.split('-')
        rangeInputs[i] = (int(tmp[0]), int(tmp[1])) #convert each entry to a tuple of the range

    for i, val in enumerate(idInputs):
        idInputs[i] = int(val) #convert each entry to int
    #print(rangeInputs)
    #print(idInputs)

    out = validate(rangeInputs, idInputs)
    print(out)