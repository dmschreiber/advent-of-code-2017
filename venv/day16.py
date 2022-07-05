
class Move:
    def __init__(self, type, a, b, amount=0):
        self.type = type
        self.a = a
        self.b = b
        self.amount = amount


class ProgramGroup:
    def __init__(self, size):
        self.index = 0

        self.programs = "abcdefghijklmnopqrstuvwxyz"[:size]

    def list(self):
        return "{}{}".format(self.programs[self.index:],self.programs[:self.index])

    def spin(self, how_many):
        if (how_many >= len(self.programs)):
            raise "Trying to sping {}".format(how_many)
        temp = len(self.programs)-how_many
        self.index=(self.index + temp ) % len(self.programs)

    def exchange(self,a,b):
        if b + self.index >= len(self.programs):
            b_i = (b + self.index) % len(self.programs)
        else:
            b_i = b + self.index

        if a + self.index >= len(self.programs):
            a_i = (a + self.index) % len(self.programs)
        else:
            a_i = a + self.index

        temp = self.programs[b_i]
        self.programs = self.programs[:b_i] + self.programs[a_i] + self.programs[b_i+1:]
        self.programs = self.programs[:a_i] + temp + self.programs[a_i+1:]

    def partner(self,a,b):
        a_i = self.programs.find(a)
        b_i = self.programs.find(b)
        temp = self.programs[b_i]
        self.programs = self.programs[:b_i] + self.programs[a_i] + self.programs[b_i+1:]
        self.programs = self.programs[:a_i] + temp + self.programs[a_i+1:]


def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    dance = input_lines[0].split(",")

    g = ProgramGroup(16)
    moves = []

    for d in dance:
        # print("List {}".format(g.list()))
        if d[0]=="s":
            # print("Spin {}".format(d[1:]))
            g.spin(int(d[1:]))
            moves.append(Move(1,0,0,int(d[1:])))

        elif d[0]=="x":
            (a,b) = d[1:].split("/")
            # print("Exchange {} and {}".format(a,b))
            g.exchange(int(a),int(b))
            moves.append(Move(2,int(a),int(b)))

        elif d[0]=="p":
            (a, b) = d[1:].split("/")
            # print("Partner {} and {}".format(a,b))
            g.partner(a, b)
            moves.append(Move(3,a,b))

        else:
            raise "What the heck? {}".format(d)

    return g.list()

def create_reverse_map(start,end):
    reverse_map = {}
    for i in range(len(start)):
        reverse_map[end.find(start[i])] = i

    return reverse_map

def create_partner_map(start,end):
    partner_map = {}
    for i in range(len(start)):
        partner_map[start[i]] = end[i]

    return partner_map

def part2(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    dance = input_lines[0].split(",")

    g = ProgramGroup(16)
    moves = []

    for d in dance:
        if d[0]=="s":
            g.spin(int(d[1:]))
            moves.append(Move(1,0,0,int(d[1:])))

        elif d[0]=="x":
            (a,b) = d[1:].split("/")
            g.exchange(int(a),int(b))
            moves.append(Move(2,int(a),int(b)))

        elif d[0]=="p":
            (a, b) = d[1:].split("/")
            # print("Partner {} and {}".format(a,b))
            moves.append(Move(3,a,b))

    start = "abcdefghijklmnop"
    end = g.list()

    reverse_map = create_reverse_map(start,end)

    next = start
    for m in moves:
        if m.type == 3:
            next = next.replace(m.a, "Z")
            next = next.replace(m.b, m.a)
            next = next.replace("Z", m.b)

    partner_map = create_partner_map(start,next)

    times = 10
    for i in range(6): # a billion times 10^6
        end = run_position_dance(start, reverse_map, times)
        reverse_map = create_reverse_map(start,end)
        end = run_partner_dance(start, partner_map, times)
        partner_map = create_partner_map(start, end)

    result = run_dance(start, reverse_map, partner_map, 1)

    return result


def run_dance(start, reverse_map, partner_map, times):
    next = start
    next = run_position_dance(start, reverse_map, times)
    next = run_partner_dance(next, partner_map, times)

    return next

def run_position_dance(start, reverse_map, times):
    next = start
    for each_dance in range(int(times)):
        next = "".join(x for x in [next[reverse_map[i]] for i in range(len(next))])

    return next

def run_partner_dance(start, partner_map, times):
    next = start
    for each_dance in range(int(times)):
        next = "".join(x for x in [partner_map[c] for c in next])

    return next
