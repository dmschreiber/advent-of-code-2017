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
    x, y = pos

    
    return grid[(x-1,y)] + grid[(x,y)] + grid[(x+1,y)] + grid[(x-1,y-1)] + grid[(x,y-1)] + grid[(x+1,y-1)] + grid[(x-1,y+1)] + grid[(x,y+1)] + grid[(x+1,y+1)]

def part2(input):
    grid = {}
    grid [(0,0)] = 1
    grid [(0,1)] = sum_neighbors(grid,(0,1))

    return grid[0,1]
