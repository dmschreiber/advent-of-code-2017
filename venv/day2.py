def part1(input):
    checksum = 0

    for l in input:
        min = 999
        max = 0
        for i in l.split():
            if int(i) < min:
                min = int(i)
            if int(i) > max:
                max = int(i)

        checksum += max-min

    return str(checksum)

def part2(input):
    checksum = 0

    for l in input:
        for i in l.split():
            for j in l.split():
                if i != j and ((int(i) % int(j)) == 0):
                    checksum += int(int(i) / int(j))

    return str(checksum)
