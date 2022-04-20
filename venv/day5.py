def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    offsets = [int(l) for l in input_lines]
    loops = 0
    pointer = 0

    while pointer < len(offsets):
        # print("loops {}, pointer {}, jumps {}".format(loops, pointer, offsets))
        loops = loops + 1
        this_offset = offsets[pointer]
        offsets[pointer] = offsets[pointer] + 1

        pointer = pointer + this_offset
        if pointer >= len(offsets):
            break


    return loops

def part2(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    offsets = [int(l) for l in input_lines]
    loops = 0
    pointer = 0

    while pointer < len(offsets):
        # print("loops {}, pointer {}, jumps {}".format(loops, pointer, offsets))
        loops = loops + 1
        this_offset = offsets[pointer]
        if this_offset >= 3:
            offsets[pointer] = offsets[pointer] -1

        else:
            offsets[pointer] = offsets[pointer] + 1

        pointer = pointer + this_offset
        if pointer >= len(offsets):
            break


    return loops

