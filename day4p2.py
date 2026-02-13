known = {} # dictionary of known values
dimX = 0
dimY = 0
grid = [] #full grid

#check if given position has less than 4 adjacent rolls of paper, return true if true and false if false
def validate(x,y):
    count = 0
    positions = [-1,0,1]
    for i in positions:
        for j in positions:
            currX = x + j
            currY = y + i
            if j == 0 and i == 0: continue #skip 0,0
            if (currX,currY) in known:
                count += known[(currX,currY)]
            else: #currently checked value is not known
                if currX < 0 or currX > dimX-1 or currY < 0 or currY > dimY-1: #check if oob
                    known[(currX,currY)] = 0 #add value to dict
                else: 
                    if grid[currY][currX] == '@':
                        known[(currX,currY)] = 1 #add value to dict
                        count += 1 #increment count
                    else:
                        known[(currX,currY)] = 0 #add value to dict
    if count < 4:
        return True
    else:
        return False

if __name__ == "__main__":
    grid = []
    #file = "day4sample.txt"
    file = "day4input.txt"
    with open(f"inputs/{file}") as f:
        for i, line in enumerate(f):
            grid.append(list(line.strip('\n')))

    dimY = len(grid)
    dimX = len(grid[0])

    loc = []

    #print(grid)
    # get all paper positions
    for i, line in enumerate(grid):
        indices = [(j,i) for j, x in enumerate(line) if x == "@"]
        loc.extend(indices)

    #print(loc)
    total = 0
    curr = -1 #count of currently removed pieces of paper, set to -1 to initialize
    while curr != 0: #keep looping until no more pieces can be removed
        soln = []
        # iterate over paper positions
        for val in loc:
            if(validate(*val)): #validate if paper has more than
                soln.append(val)

        curr = (len(soln))
        total += curr
        #removal phase
        for val in soln: 
            known[val] = 0 #update entry for coordinate so it's now considered empty
            #grid[val[1]][val[0]] = '.' #update grid just in case
            loc.remove(val) #remove value from list of papers
    
    print(total)
        