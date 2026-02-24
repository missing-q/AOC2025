
def getValidIDCount(ranges): #takes in a list of ranges in array form, returns the count of unique valid IDs in said ranges
    ranges.sort() #sort by lower range in ascending order
    newRanges = []
    newRanges.append(ranges[0])
    for i in range(1, len(ranges)):
        last = newRanges[-1]
        curr = ranges[i]
        if curr[0] <= last[1]: # check if current interval overlaps with the last merged interval
            last[1] = max(last[1], curr[1])
        else:
            newRanges.append(curr)
    count = 0
    for i in newRanges:
        count += (i[1] - i[0]) +1
    return count
                
    


if __name__ == "__main__":
    #file = "day5sample.txt"
    file = "day5input.txt"
    cont = open(f"inputs/{file}").read().split("\n\n")
    rangeInputs = cont[0].split('\n')
    #idInputs = cont[1].split('\n') #all the IDs are irrelevant for part 2

    #formatting each list
    for i, val in enumerate(rangeInputs):
        tmp = val.split('-')
        rangeInputs[i] = [int(tmp[0]), int(tmp[1])] #convert each entry to an array of the range (not tuples, since they are immutable)

    #for i, val in enumerate(idInputs):
        #idInputs[i] = int(val) #convert each entry to int
    #print(rangeInputs)
    #print(idInputs)

    out = getValidIDCount(rangeInputs)
    print(out)