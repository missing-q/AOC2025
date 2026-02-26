if __name__ == "__main__":
    grid = []
    #file = "day7sample.txt"
    file = "day7input.txt"
    with open(f"inputs/{file}") as f:
        for i, line in enumerate(f):
            grid.append(list(line.strip('\n'))) # remove empty spaces


    curr = []
    count = 0
    rowlen = len(grid[0])
    for i, line in enumerate(grid):
        if i == 0:
            curr.append(grid[0].index('S'))
        else:
            #propagate lines
            update = curr.copy()
            for j in curr:
                if grid[i][j] == '^': #beam is split
                    count += 1 #increment split count
                    update.remove(j) 
                    if j-1 >= 0 and j-1 not in update: #oob check / uniqueness check
                        update.append(j-1)
                    if j+1 < rowlen and j+1 not in update: #oob check / uniqueness check
                        #add new right beam to set
                        update.append(j+1)
            curr = update
    print(count)