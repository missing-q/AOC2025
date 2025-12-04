if __name__ == "__main__":
    total = 0
    #file = "day2sample.txt"
    file = "day2input.txt"
    with open(f"inputs/{file}") as f:
        ranges = f.readline().split(',') #input is only on one line
        for i, val in enumerate(ranges):
            tmp = val.split('-')
            ranges[i] = (int(tmp[0]),int(tmp[1])) #store range as tuple
    for val in ranges:
        for num in range(val[0],val[1]+1):
            tmp = str(num)
            if (len(tmp) // (tmp+tmp).find(tmp, 1)) >= 2:
                total += num
                print(f"invalid id {num}")
    print(total)