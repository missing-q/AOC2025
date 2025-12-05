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
        num1 = 0
        num2 = 0
        for i in range(len(row)):
            curr = row[i]
            if (curr > num1) and (i != len(row)-1): #highest first digit will always be higher, can't be setting the first digit on the last digit of the row...
                num1 = curr
                num2 = 0
            elif int(str(num1)+str(num2)) < int(str(num1)+str(curr)):
                    num2 = curr
        total += int(str(num1)+str(num2))
    print(total)