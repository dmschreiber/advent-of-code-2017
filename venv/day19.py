def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    map = []
    for l in input_lines:
        map.append([c for c in l])

    # print_map(map)
    start_col = find_start_col(map)
    # print("starting column {} - {}".format(start_col, map[0][start_col]))

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    position = (0,start_col)
    direction = (1,0)
    pathway = []

    while direction != (0,0):
        # print("position = {}".format(position))
        if can_step(map, position, direction):
            position = (position[0] + direction[0], position[1] + direction[1])
            if get_map_char(map,position) in letters:
                pathway.append(get_map_char(map,position))
        else:
            direction = find_new_direction(map, position, direction)

    return "".join(pathway)
    # if next step is blank, find a new direction
    #   if no new direction, end
    # else position = position + step
    # collect letter

def part2(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    map = []
    for l in input_lines:
        map.append([c for c in l])

    # print_map(map)
    start_col = find_start_col(map)
    # print("starting column {} - {}".format(start_col, map[0][start_col]))

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    position = (0,start_col)
    direction = (1,0)
    steps = 0

    while direction != (0,0):
        # print("position = {}".format(position))
        if can_step(map, position, direction):
            position = (position[0] + direction[0], position[1] + direction[1])
            steps = steps + 1
        else:
            direction = find_new_direction(map, position, direction)

    return steps + 1

def find_new_direction(map, position, direction):
    if direction == (1,0) or direction == (-1,0):
        if can_step(map, position, (0,1)):
            new_direction = (0,1)
        elif can_step(map, position, (0,-1)):
            new_direction = (0,-1)
        else:
            new_direction = (0,0)
    if direction == (0,1) or direction == (0,-1):
        if can_step(map, position, (1,0)):
            new_direction = (1,0)
        elif can_step(map, position, (-1,0)):
            new_direction = (-1,0)
        else:
            new_direction = (0,0)

    return new_direction

def get_map_char(map, pos):
    if pos[0] < 0 or pos[0] >= len(map):
        return " "
    if pos[1] < 0 or pos[1] >= len(map[pos[0]]):
        return " "

    return map[pos[0]][pos[1]]

def can_step(map, pos, dir):
    possible_pos = (pos[0]+dir[0], pos[1] + dir[1])
    if get_map_char(map, possible_pos) != " ":
        return True
    else:
        return False

def find_start_col(map):
    for col in range(len(map[0])):
        if map[0][col] != " ":
            return col

def print_map(map):
    for row in range(len(map)):
        print("{}:".format(row), end="")
        for col in range(len(map[row])):
            print("{}".format(map[row][col]), end="")
        print()
