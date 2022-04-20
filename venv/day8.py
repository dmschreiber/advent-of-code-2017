def part2(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    # init registers
    registers = {}
    for l in input_lines:
        r = l.split()
        if not r[0] in registers.keys():
            registers[r[0]] = 0

    current_max = 0

    for l in input_lines:
        op = l.split(" if ")
        for r in registers.keys():
            if op[1][0:len(r) + 1] == r + " ":
                op[1] = op[1].replace(r, str(registers[r]))

        # print("{} if {}".format(op[0],op[1]))
        # print(eval(op[1]))
        if eval(op[1]):
            (r, instruction, n) = op[0].split()
            if instruction == "inc":
                registers[r] = registers[r] + int(n)
            else:
                registers[r] = registers[r] - int(n)

        if max(registers.values()) > current_max:
            current_max = max(registers.values())

    return current_max

def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    # init registers
    registers = {}
    for l in input_lines:
        r = l.split()
        if not r[0] in registers.keys():
            registers[r[0]] = 0

    for l in input_lines:
        op = l.split(" if ")
        for r in registers.keys():
            if op[1][0:len(r)+1] == r+" ":
                op[1] = op[1].replace(r,str(registers[r]))

        # print("{} if {}".format(op[0],op[1]))
        # print(eval(op[1]))
        if eval(op[1]):
            (r,instruction,n) = op[0].split()
            if instruction == "inc":
                registers[r] = registers[r] + int(n)
            else:
                registers[r] = registers[r] - int(n)

    return max(registers.values())
