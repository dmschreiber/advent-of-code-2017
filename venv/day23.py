registers = "abcdefgh"

def reset_registers():
    register_map = {}
    for c in registers:
        register_map[c] = 0
    return register_map


def exec(line,map):
    args = line.split()
    if args[0] == "set":
        if args[2] in registers:
            map[args[1]] = map[args[2]]
        else:
            map[args[1]] = int(args[2])

    if args[0] == "sub":
        if args[2] in registers:
            map[args[1]] = map[args[1]] - map[args[2]]
        else:
            map[args[1]] = map[args[1]] - int(args[2])

    if args[0] == "mul":
        if args[2] in registers:
            map[args[1]] = map[args[1]] * map[args[2]]
        else:
            map[args[1]] = map[args[1]] * int(args[2])

    if args[0] == "jnz":
        if args[1] in registers:
            test = map[args[1]]
        else:
            test = int(args[1])

        if test != 0:
            if args[2] in registers:
                return map[args[2]]
            else:
                return int(args[2])

    return 1

def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    map = reset_registers()

    index = 0
    count_mul = 0

    while index < len(input_lines):
    # for i in range(10):
        if "mul" in input_lines[index]:
            count_mul = count_mul + 1
        # print("index {}, ({}), map {}".format(index,input_lines[index],map))
        index = index + exec(input_lines[index],map)

    return count_mul

def check_it(b):
    for d in range(2, b):
        if b % d == 0:
            # print("{} is {} x {}".format(b,d,b/d))
            return 1

    return 0


def routine(map):
    h = 0
    for b in range(105700,122701,17):
        h = h + check_it(b)

    return h

def part2():
    map = reset_registers()

    map["b"] = 57 * 100 + 100000 # 105,700
    map["c"] = map["b"] + 17000 #  122,700

    return routine(map)


# set b 57
# set c b
# jnz a 2
# jnz 1 5
# mul b 100
# sub b -100000
# set c b
# sub c -17000
# set f 1
# set d 2
# set e 2
# set g d
# mul g e
# sub g b
# jnz g 2
# set f 0
# sub e -1
# set g e
# sub g b
# jnz g -8
# sub d -1
# set g d
# sub g b
# jnz g -13
# jnz f 2
# sub h -1
# set g b
# sub g c
# jnz g 2
# jnz 1 3
# sub b -17
# jnz 1 -23
