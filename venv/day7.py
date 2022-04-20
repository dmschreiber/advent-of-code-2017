def part2(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    discs = {}
    disc_weight = {}
    for l in input_lines:
        disc = l.split(" -> ")
        if len(disc) > 1:
            discs[disc[0].split(" ")[0]] = disc[1]
        else:
            discs[disc[0].split(" ")[0]] = ""
        weight = disc[0].split(" ")[1]
        disc_weight[disc[0].split(" ")[0]] = int(weight[1:len(weight)-1])

    base = find_base_program(discs)

    find_off_balance_program(base, disc_weight, discs)
    return 0


def find_off_balance_program(base, disc_weight, discs):
    children = {}
    for child in discs[base].split(", "):
        w = calculate_weight(discs, disc_weight, child)
        # print("child {} weighs {}".format(child, w))
        if w in children.keys():
            children[w] = children[w] + 1
        else:
            children[w] = 1
    off_balance = ""
    wrong_weight = 0
    right_weight = 0

    for w in children.keys():
        if children[w] == 1:
            wrong_weight = w
            for child in discs[base].split(", "):
                if calculate_weight(discs, disc_weight, child) == w:
                    off_balance = child
        else:
            right_weight = w

    if off_balance == "":
        # print("all in balance")
        return False
    else:
        # print("off balance child is {}".format(off_balance))
        if not find_off_balance_program(off_balance, disc_weight, discs):
            # print("need to fix up {} by {}".format(off_balance, right_weight-wrong_weight))
            print("Day 7 part 2: disc {} should be {}".format(off_balance, disc_weight[off_balance] + right_weight - wrong_weight))
        return True


def calculate_weight(discs, weights, program):
    weight = weights[program]
    if discs[program] != "":
        for n in discs[program].split(", "):
            weight = weight + calculate_weight(discs, weights, n)
    return weight

def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    discs = {}
    for l in input_lines:
        disc = l.split(" -> ")
        if len(disc) > 1:
            discs[disc[0].split(" ")[0]] = disc[1]
        else:
            discs[disc[0].split(" ")[0]] = ""

    base_node = find_base_program(discs)

    return base_node


def find_base_program(discs):
    base_node = ""
    for d in discs.keys():
        found = False
        for child in discs.keys():
            if d in discs[child]:
                found = True

        if not found:
            base_node = d
    return base_node

