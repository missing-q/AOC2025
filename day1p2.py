if __name__ == "__main__":
    dial = 50
    count = 0
    inputs = []
    #file = "day1sample.txt"
    file = "day1input.txt"
    with open(f"inputs/{file}") as f:
        for i, line in enumerate(f):
            str = line.strip("\n")
            dir = str[0]
            num = int(str[1:])
            if dir == 'L':
                num *= -1
            inputs.append(num)

    #print(inputs)
    for i in inputs:
        dial += i
        # handle looparound cases
        if dial < 0:
            while dial < 0:
                dial += 100
                count += 1
        elif dial > 100:
            while dial > 100:
                dial -= 100
                count += 1
        #print(f"dial is now at {dial}")
        if dial == 0:
            count += 1
    print(count)
            