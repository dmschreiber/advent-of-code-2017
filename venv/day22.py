def turn_right(direction):
    return (direction + 90) % 360

def turn_left(direction):
    ret_val = direction - 90
    if ret_val < 0:
        ret_val = ret_val + 360

    return ret_val

def move(pos,direction):
    if direction == 0:
        return (pos[0] - 1,pos[1])

    if direction == 90:
        return (pos[0],pos[1]+1)

    if direction == 180:
        return (pos[0]+1,pos[1])

    if direction == 270:
        return (pos[0],pos[1]-1)

def print_map(map,width):
    for row in range(-width,width+1):
        for col in range(-width,width+1):
            if (row,col) in map.keys() and map[(row,col)]:
                print("#",end="")
            else:
                print(".",end="")
        print()

def part1(input, iterations):
    with open(input) as f:
        input_lines = f.read().splitlines()

    map = {}

    width = int(len(input_lines[0]) / 2)

    row = -1 * width
    for l in input_lines:
        col = -1 * width
        for c in l:
            if c == '.':
                map[(row,col)] = False
            else:
                map[(row, col)] = True

            col = col + 1
        row = row + 1


    position = (0,0)
    direction = 0
    infected = 0

    for iteration in range(iterations):
        if position in map.keys() and map[position]:
            direction = turn_right(direction)
        else:
            direction = turn_left(direction)

        if position in map.keys() and map[position]:
            map[position] = False
        else:
            map[position] = True
            infected = infected + 1

        position = move(position,direction)
        # print_map(map,9)

    return infected

def get_map_result(map,pos):
    if pos in map.keys():
        return map[pos]
    else:
        return '.'

def part2(input, iterations):
    with open(input) as f:
        input_lines = f.read().splitlines()

    map = {}

    width = int(len(input_lines[0]) / 2)

    row = -1 * width
    for l in input_lines:
        col = -1 * width
        for c in l:
            if c == '.':
                map[(row,col)] = '.'
            else:
                map[(row, col)] = '#'

            col = col + 1
        row = row + 1


    position = (0,0)
    direction = 0
    infected = 0

    for iteration in range(iterations):
        if get_map_result(map,position) == '#':
            direction = turn_right(direction)
        elif get_map_result(map,position) == '.':
            direction = turn_left(direction)
        elif get_map_result(map,position) == 'F':
            direction = turn_right(direction)
            direction = turn_right(direction)


        if get_map_result(map,position) == '.':
            map[position] = 'W'
        elif get_map_result(map,position) == 'W':
            map[position] = '#'
            infected = infected + 1
        elif get_map_result(map,position) == '#':
            map[position] = 'F'
        elif get_map_result(map,position) == 'F':
            map[position] = '.'

        position = move(position,direction)
        # print_map(map,9)

    return infected