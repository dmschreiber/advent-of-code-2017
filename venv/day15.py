def part1(A,B,how_many):
    A_multiplier = 16807
    B_multiplier = 48271
    mod_number = 2147483647
    new_A = A
    new_B = B
    matches = 0

    for i in range(how_many):
        new_A = (new_A * A_multiplier) % mod_number
        new_B = (new_B * B_multiplier) % mod_number

        if "{0:32b}".format(new_A)[16:] == "{0:32b}".format(new_B)[16:]:
            # print("Found match")
            matches = matches + 1

        # print("{0:32b}".format(new_A))
        # print("{0:32b}".format(new_B))

    return matches

def get_next_number(num, multiplier, mod_number, criteria):
    n = num

    while True:
        n = (n * multiplier) % mod_number
        if n % criteria == 0:
            return n


def part2(A,B,how_many):
    A_multiplier = 16807
    B_multiplier = 48271
    mod_number = 2147483647
    new_A = A
    new_B = B
    matches = 0
    which = 0

    for i in range(how_many):
        which = which + 1
        new_A = get_next_number(new_A, A_multiplier, mod_number, 4)
        new_B = get_next_number(new_B, B_multiplier, mod_number, 8)

        if "{0:32b}".format(new_A)[16:] == "{0:32b}".format(new_B)[16:]:
            # print("Found match on {}th".format(which))
            matches = matches + 1

            # print("{0:32b}".format(new_A))
            # print("{0:32b}".format(new_B))

    return matches