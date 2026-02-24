if __name__ == "__main__":
    inputs = []
    #file = "day6sample.txt"
    file = "day6input.txt"
    with open(f"inputs/{file}") as f:
        for i, line in enumerate(f):
            tmp = line.strip('\n').split(' ')
            inputs.append([x for x in tmp if x.strip()]) # remove empty spaces

    #print(inputs)
    count = 0

    for i in range(len(inputs[0])): #loop as many times as there are problems
        op = inputs[-1][i]
        evalstring = inputs[0][i] #start with the first number to avoid fenceposting!
        for j in range(1, len(inputs)-1):
            evalstring += op
            evalstring += inputs[j][i]
            
        num = eval(evalstring)
        count += num
    print(count)