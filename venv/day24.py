def find_port(avail,state,which):

    bool_found = False
    retval = []

    for p in avail:
        if p not in state:
            if p[0] == which:
                bool_found = True
                new_state = state.copy()
                new_state.append(p)
                for s in find_port(avail, new_state, p[1]):
                    retval.append(s)

            if p[1] == which:
                bool_found = True
                new_state = state.copy()
                new_state.append(p)
                for s in find_port(avail, new_state, p[0]):
                    retval.append(s)

    if not bool_found:
        retval.append(state)

    for s in retval:
        yield s

def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    state = []
    available = []

    for l in input_lines:
        (start,end) = l.split("/")
        (start,end) = (int(start),int(end))
        available.append((start,end))


    max_power = 0
    for i in find_port(available,state,0):
        power = 0
        for p in i:
            power = power + p[0] + p[1]
        if power > max_power:
            max_power = power

    return max_power

def part2(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    state = []
    available = []

    for l in input_lines:
        (start,end) = l.split("/")
        (start,end) = (int(start),int(end))
        available.append((start,end))

    max_length = 0
    max_power = 0
    for i in find_port(available,state,0):
        if len(i) > max_length:
            max_length = len(i)
            max_power = 0

        if len(i) >= max_length:
            power = 0
            for p in i:
                power = power + p[0] + p[1]
            if power > max_power:
                max_power = power
            print("length {}, power {}".format(len(i),power))

    # 2002 is too high
    return max_power