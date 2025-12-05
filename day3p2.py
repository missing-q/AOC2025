import heapq
if __name__ == "__main__":
    inputs = []
    total = 0
    #file = "day3sample.txt"
    file = "day3input.txt"
    with open(f"inputs/{file}") as f:
        for i, line in enumerate(f):
            l = [int(i) for i in line.strip("\n")]
            inputs.append(l)
    for row in inputs:
        out = []
        tmp = row
        for i in range(12,0,-1):
            select = tmp[:len(tmp)-i+1]
            res = max(select)
            out.append(res)
            tmp = tmp[tmp.index(res)+1:]
        total += int(''.join(map(str,out)))
    
    print(total)

#    234234234234278
#       234234234278
#         4234234278 