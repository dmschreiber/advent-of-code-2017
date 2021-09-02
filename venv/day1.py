def part1(input):
    return generalized(input,1)

def part2(input):
    return generalized(input,int(len(input)/2))

def generalized(input, offset):
    sum = 0
    for i in range(0,len(input)):
        if input[i] == input[(i+offset) % len(input)]:
            sum = sum + int(input[i])

    return(str(sum))
