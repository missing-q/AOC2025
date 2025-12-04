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
            first, second = tmp[:len(tmp)//2], tmp[len(tmp)//2:]
            if first == second:
                total += num
                print(f"invalid id {num}")
    print(total)