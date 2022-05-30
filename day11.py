
import copy

class PointHex:
    def __init__(self, my_x, my_y):
        self.x = my_x
        self.y = my_y

    def move(self, direction):
        if direction == "ne":
            self.y = self.y + 1
            self.x = self.x + 1
        if direction == "nw":
            self.x = self.x - 1
            self.y = self.y + 1
        if direction == "s":
            self.y = self.y - 2
        if direction == "n":
            self.y = self.y + 2
        if direction == "se":
            self.x = self.x + 1
            self.y = self.y - 1
        if direction == "sw":
            self.x = self.x - 1
            self.y = self.y - 1
        return self

    def neighbors(self):
        return [PointHex(self.x, self.y).move(d) for d in ["ne", "nw", "n", "s", "se", "sw"]]

    def print(self):
        print((self.x, self.y))

    def distance(self, p):
        d = 0
        d = d + abs(p.x-self.x)
        d = d + (abs(p.y)-abs(p.x-self.x)-abs(self.y))/2
        return d


def part1(input):
    directions = input.split(",")
    start = PointHex(0,0)
    next = copy.copy(start)
    # print("moving {}".format(input))
    for d in directions:
        next.move(d)

    return start.distance(next)

def part2(input):
    max_distance = 0
    directions = input.split(",")
    start = PointHex(0,0)
    next = copy.copy(start)
    # print("moving {}".format(input))
    for d in directions:
        next.move(d)
        if start.distance(next) > max_distance:
            max_distance = start.distance(next)

    return max_distance