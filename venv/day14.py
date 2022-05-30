import day10

def part1(input):

    s = 0

    for i in range(128):
        key = input + "-" + str(i)
        hex_output = int(day10.part2(key,256),16)
        bin_output = format(hex_output,"0>128b")
        nums = [int(l) for l in list(bin_output)]
        s = s+ sum(nums)

    return s
