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
            grid[0][grid[0].index('S')] = 1
        else:
            for j, tile in enumerate(line):
                #propagate lines
                above = grid[i-1][j]
                if above != '^' and above != '.': #splits and empty spaces will not propagate
                    if tile == '^': #splitter case
                        if j-1 >= 0: #oob check
                            if grid[i][j-1] == '.': #empty space case
                                grid[i][j-1] = above
                            else: #add numbers case
                                grid[i][j-1] += above
                        if j+1 < rowlen:
                            if grid[i][j+1] == '.': #empty space case
                                grid[i][j+1] = above
                            else: #add numbers case
                                grid[i][j+1] += above

                    
                    elif tile == '.': #empty space case
                        grid[i][j] = above

                    else: #add numbers case
                        grid[i][j] += above
    #print(count)

    result = grid[-1] #get last row of grid
    result = [i for i in result if i != '.'] #remove all blanks
    print(sum(result))