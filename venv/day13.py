def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    scan = {}
    for l in input_lines:
        (k,v) = l.split(": ")
        # print(k,v)
        scan[int(k)] = int(v)


    damage = 0
    for second in range(max(scan.keys())+1):
        # print_state(second,scan)

        if second in scan.keys():
            if (second) % (2 * scan[second] - 2) == 0 :
                # print("Second {} caught".format(second))
                damage = damage + second * scan[second]

    return damage

def get_damage(offset, scan):
    damage = 0
    for pos in range(max(scan.keys())+1):
        # print_state(second,scan)
        second = pos + offset

        if pos in scan.keys():
            if (second) % (2 * scan[pos] - 2) == 0 :
                damage = damage + second * scan[pos]
                if damage > 0:
                    break

    return damage

def part2(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    scan = {}
    for l in input_lines:
        (k,v) = l.split(": ")
        # print(k,v)
        scan[int(k)] = int(v)

    offset = 0
    while get_damage(offset,scan) > 0:
        # print("offset {} damage {}".format(offset,get_damage(offset,scan)))
        offset = offset + 1

    # print_state(offset+1,scan)
    return offset

def print_state(second, scan):
    print("Picosecond {}".format(second))

    for s in range(max(scan.keys())+1):
        if s % 10 == 0:
            print("  {}                                               ".format(int(s/10)),end="")
    print()
    for s in range(max(scan.keys())+1):
        print("  {}  ".format(s % 10),end="")
    print()

    for s in range(max(scan.keys())+1):
        if s in scan.keys():
            if (second) % (2 * scan[s] - 2) == 0:
                print(" [S] ", end="")
            else:
                print(" [ ] ", end="")
        else:
            print(" ... ", end="")
    print()