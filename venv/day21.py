
# - start is     .#.
#                ..#
#                ###
starting_pattern = [[False,True,False],[False,False,True],[True,True,True]]

def compare(tile1,tile2):

    # for i in range(len(tile1)):
    #     for j in range(len(tile1[i])):
    #         if tile1[i][j]:
    #             print("#",end="")
    #         else:
    #             print(".",end="")
    #
    #     print("   ",end="")
    #
    #     for j in range(len(tile1[i])):
    #         if tile2[i][j]:
    #             print("#",end="")
    #         else:
    #             print(".",end="")
    #     print()
    # print("=====")
    for i in range(len(tile1)):
        for j in range(len(tile2)):
            if tile1[i][j] != tile2[i][j]:
                return False

    return True

def print_tile(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j]:
                print("#",end="")
            else:
                print(".",end="")
        print()


def extract_tile(state,size,i,j):
    start_row = i * size
    start_col = j * size

    return_tile = []
    for row in range(size):
        return_tile.append([])
        for col in range(size):
            return_tile[row].append(state[row+start_row][start_col+col])

    return return_tile

def flip(tile):
    new_tile = []
    size = len(tile)

    for i in range(size):
        new_tile.append([])
        for j in range(size):
            new_tile[i].append(tile[i][size-j-1])

    return new_tile

def flip2(tile):
    new_tile = []
    size = len(tile)

    for i in range(size):
        new_tile.append([])
        for j in range(size):
            new_tile[i].append(tile[size-i-1][j])

    return new_tile

def rotate(tile):
    new_tile = []
    size = len(tile)


    for i in range(size):
        new_tile.append([])
        for j in range(size):
            new_tile[i].append(tile[size-i-1][size-j-1])

    return new_tile

def rotate2(tile):
    size = len(tile)
    if len(tile) == 2:
        new_tile = [[False,False],[False,False]]
    elif len(tile) == 3:
        new_tile = [[False,False,False],[False,False,False],[False,False,False]]

    for i in range(size):
        for j in range(size):
            new_tile[i][j] = tile[size-j-1][i]

    return new_tile

def total_on(tile):
    count = 0
    for i in range(len(tile)):
        for j in range(len(tile)):
            if tile[i][j]:
                count = count + 1
    return count

def match_rule(tile,map):
    ret_val = []

    index = 0
    for m in map:
        index = index + 1
        if len(m[0]) == len(tile) and total_on(m[0]) == total_on(tile):
            possible_tile = tile

            for angles in range(4):
                if compare(m[0],possible_tile):
                    match_output = m[1]
                    # print("match rotated {}!".format(angles))
                    # print_tile(possible_tile)
                    if len(ret_val) == 0:
                        ret_val.append(match_output)

                    # else:
                    #     print("already added")

                elif compare(m[0],flip(possible_tile)):
                    match_output = m[1]
                    # print("match flip rotated {}!".format(angles))
                    # print_tile(flip(possible_tile))
                    if len(ret_val) == 0:
                        ret_val.append(match_output)
                    # else:
                    #     print("already added")

                elif compare(m[0],flip2(possible_tile)):
                    match_output =m[1]
                    # print("match flip2 rotated {}!".format(angles))
                    # print_tile(flip2(possible_tile))
                    if len(ret_val) == 0:
                        ret_val.append(match_output)
                    # else:
                    #     print("already added")

                possible_tile = rotate2(possible_tile)

    if len(ret_val) == 0:
        raise Exception("No Match")
    elif len(ret_val) > 1:
        raise Exception("Multiple Matches {}".format(ret_val))
    else:
        return ret_val[0]

def perform_mapping(state,map):

    size = 3
    if len(state)/2 == int(len(state)/2):
        size = 2
    else:
        size = 3

    print("Size {}".format(size))

    units = int(len(state)/size)
    output_tile = []
    # print("state")
    # print_tile(state)

    for i in range(units):
        output_tile.append([])
        for j in range (units):
            tile = extract_tile(state,size,i,j)
            # print("tile {},{}".format(i,j))
            # print_tile(tile)
            output_tile[i].append(match_rule(tile, map))

    # print("output tile {}".format(output_tile))

    output = []

    for i in range(units):
        for j in range(units):
            for inner_i in range(size+1):
                for inner_j in range(size+1):
                    if len(output) <= i*(size+1)+inner_i:
                        output.append([])

                    output[i*(size+1)+inner_i].append(output_tile[i][j][inner_i][inner_j])

    # print_tile(output)
    return output

def part1(input, iterations):
    with open(input) as f:
        input_lines = f.read().splitlines()

    state = starting_pattern
    maps = []

    for l in input_lines:
        (start,end) = l.split(" => ")
        start = [[c=="#" for c in r] for r in start.split("/")]
        end = [[c=="#" for c in r] for r in end.split("/")]
        # print(start,end)
        maps.append((start,end))

    print_tile(state)
    for i in range(iterations):
        print("Iteration {}".format(i))
        state = perform_mapping(state, maps)

    return total_on(state)

# 131 is too low (out of 256)