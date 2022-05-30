def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    map = {}
    for l in input_lines:
        k = l.split(" <-> ")[0]
        children = l.split(" <-> ")[1].split(", ")
        map[k] = children


    programs = ['0']
    last_length = 0

    while last_length < len(programs):
        last_length = len(programs)
        for k in map.keys():
            for child in map[k]:
                if child in programs and k not in programs:
                    programs.append(k)
                    break

    return len(programs)

def find_programs(map, seed):
    programs = [seed]
    last_length = 0

    while last_length < len(programs):
        last_length = len(programs)
        for k in map.keys():
            for child in map[k]:
                if child in programs and k not in programs:
                    programs.append(k)
                    break
    return programs

def not_found(k,programs):
    # print("Not found {}".format(programs))

    for k1 in programs.keys():
        for k2 in programs[k1]:
            if k == k2:
                return False

    return True

def part2(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    map = {}
    for l in input_lines:
        k = l.split(" <-> ")[0]
        children = l.split(" <-> ")[1].split(", ")
        map[k] = children

    programs = {}
    programs['0'] = find_programs(map, '0')

    for k in map.keys():
        if not_found(k,programs):
            programs[k] = find_programs(map,k)


    return len(programs.keys())