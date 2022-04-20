
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

    for d in discs.keys():
        found = False
        for child in discs.keys():
            if d in discs[child]:
                found = True

        if not found:
            return d


    return ""

