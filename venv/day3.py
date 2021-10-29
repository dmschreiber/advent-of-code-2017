import math

def part1(input):
    distance = 0

    closest = int(math.sqrt(input))
    if int(closest/2) == closest/2 :
        closest = closest - 1

    anchor = closest*closest
    anchor_x = (closest-1)/2
    anchor_y = (closest-1)/2

    diff = input - anchor

    if diff == 0:
        return abs(anchor_x) + abs(anchor_y)

    sides = int(diff/(closest+1))

    if sides == 0:
        spot_x = anchor_x + 1
        spot_y = anchor_y - diff + 1

    if sides == 1:
        spot_x = anchor_x - (diff - (closest +1) - 1)
        spot_y = anchor_y - closest

    if sides == 2:
        spot_x = anchor_x - closest
        spot_y = anchor_y + closest - (diff - (closest+1)*2)

    if sides == 3:
        spot_x = anchor_x + (diff - (closest+1)*3) - closest
        spot_y = anchor_y + 1

    distance = int(abs(spot_x) + abs(spot_y))

    return distance


def sum_neighbors(grid, pos):
    row, col = pos
    sum = 0

    for i in [-1,0,1] :
        for j in [-1, 0, 1] :
            if grid.keys().__contains__((row+i,col+j)) :
                if i != 0 or j != 0 :
                    # print("checking {},{} is {}".format(row+i, col+j, grid[(row+i,col+j)]))
                    sum = sum + grid[(row+i,col+j)]

    return sum

def part2(input):
     # grid [(row,col)]
    grid = {}
    grid [(0,0)] = 1
    grid [(0,1)] = 1
    grid [(1,1)] = 2
    grid [(1,0)] = 4
    grid [(1,-1)] = 5
    grid [(0,-1)] = 10
    grid [(-1,-1)] = 11
    grid [(-1,0)] = 23
    grid [(-1,1)] = 25

    size = 4
    pos = (-1,2)
    while True:
        print("Beginning pos is {}".format(pos))

        # Right side
        for i in range(0,size-1) :
            grid[pos] = sum_neighbors(grid, pos)
            if grid[pos] > input :
                return grid[pos]
            pos = (pos[0] + 1, pos[1])
            print("New pos is {} - {}".format(pos, sum_neighbors(grid,pos)))

        # Top
        for i in range(0,size) :
            grid[pos] = sum_neighbors(grid, pos)
            if grid[pos] > input :
                return grid[pos]
            pos = (pos[0],pos[1]-1)
            print("New pos is {} - {}".format(pos, sum_neighbors(grid,pos)))

        # Left
        for i in range(0,size) :
            grid[pos] = sum_neighbors(grid, pos)
            if grid[pos] > input :
                return grid[pos]
            pos = (pos[0]-1,pos[1])
            print("New pos is {} - {}".format(pos, sum_neighbors(grid,pos)))

        # Bottom
        for i in range(0,size) :
            grid[pos] = sum_neighbors(grid, pos)
            if grid[pos] > input :
                return grid[pos]
            pos = (pos[0],pos[1]+1)
            print("New pos is {} - {}".format(pos, sum_neighbors(grid,pos)))

        grid[pos] = sum_neighbors(grid, pos)
        if grid[pos] > input:
            return grid[pos]
        pos = (pos[0],pos[1]+1)
        size = size + 2

    # Too high - 522596
    # Too high - 451619
