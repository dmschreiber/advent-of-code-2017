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

def neighbors(point, map):
    if point[0]>0 and map[point[0]-1][point[1]] > 0:
        yield (point[0]-1,point[1])
    if point[0]<127 and map[point[0]+1][point[1]] > 0:
        yield (point[0]+1,point[1])
    if point[1]>0 and map[point[0]][point[1]-1] > 0:
        yield (point[0],point[1]-1)
    if point[1]<127 and map[point[0]][point[1]+1] > 0:
        yield (point[0],point[1]+1)


def define_region(starting_point, region_points, map):
    for n in neighbors(starting_point, map):
        if n not in region_points:
            region_points.append(n)
            define_region(n, region_points, map)
    return region_points

def mapped(point, regions):
    for r in regions:
        if point in r:
            return True

    return False


def part2(input):
    nums = {}
    for row in range(128):
        key = input + "-" + str(row)
        hex_output = int(day10.part2(key,256),16)
        bin_output = format(hex_output,"0>128b")
        nums[row] = [int(l) for l in list(bin_output)]

    regions = []

    for r in range(128):
        for c in range(128):
            if nums[r][c] > 0 and not mapped((r,c), regions):
                points = []
                points = define_region((r,c),points,nums)
                regions.append(points)
                # print("{} starting point for a region".format((r,c)))

    return len(regions)