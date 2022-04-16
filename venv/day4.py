from collections import Counter

def part1_validate(passphrase):
    words = passphrase.split()
    counts = Counter(words)
    if max(counts.values()) == 1:
        return True
    else:
        return False


def part2_validate(passphrase):
    words = passphrase.split()
    for word in words:
        for other in words:
            if word != other and sorted(word) == sorted(other):
                return False

    return True

def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    valid_passwords = 0

    for l in input_lines:
        if part1_validate(l):
            valid_passwords += 1

    return valid_passwords

def part2(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    valid_passwords = 0

    for l in input_lines:
        if part1_validate(l) & part2_validate(l):
            # print("Valid passphrase: {}".format(l))
            valid_passwords += 1

    return valid_passwords
