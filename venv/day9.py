def score(input, part1=True):
    score = 0
    depth = 0
    skip = False
    garbage = False
    log = False
    garbage_count = 0

    if log: print("Trying {}".format(input))

    for c in input:
        if c == '<' and not skip and not garbage:
            if log: print("turn on garbage")
            garbage = True

        elif skip:
            if log: print("skip {}".format(c))
            skip = False

        elif c == '>' and garbage:
            if log: print("turn off garbage")
            garbage = False

        elif c == '!':
            if log: print("skip next")
            skip = True

        elif garbage:
            garbage_count += 1
            if log: print("garbage {}".format(c))
            pass


        elif c == '{':
            if log: print("increase depth")
            depth += 1
        elif c == '}':
            if log: print("decrease depth")
            score += depth
            depth -= 1

        if log: print(c, score, depth)
    if log: print("Final score {}".format(score))
    if part1:
        return score
    else:
        return garbage_count


def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    return score(input_lines[0])

def part2(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    return score(input_lines[0], False)
