if __name__ == "__main__":
    inputs = []
    #file = "day6sample.txt"
    file = "day6input.txt"
    with open(f"inputs/{file}") as f:
        for i, line in enumerate(f):
            inputs.append(list(line.strip('\n'))) # remove empty spaces

    print(inputs)
    out = []
    # parse inputs into cleaner format
    tmparr = []
    for i in range(len(inputs[0])):
        tmpstr = ""
        for j in range(len(inputs)-1):
            tmpstr += inputs[j][i]
        if tmpstr.isspace():
            out.append(tmparr)
            #reset to blank
            tmparr = []
        elif i == len(inputs[0])-1: #end of input
            tmparr.append(tmpstr.strip(' ')) #finalize input and append
            out.append(tmparr)

        else:
            tmparr.append(tmpstr.strip(' '))

    #add operators
    tmp = [x for x in inputs[-1] if x.strip()]
    for i in range(len(tmp)):
        out[i].append(tmp[i])

    print(out)
    count = 0
    
    for i in out: #loop as many times as there are problems
        op = i[-1]
        evalstring = i[0] #start with the first number to avoid fenceposting!
        for j in range(1, len(i)-1):
            evalstring += op
            evalstring += i[j]
            
        num = eval(evalstring)
        count += num
    print(count)