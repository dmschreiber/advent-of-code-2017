
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

def part2(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    dance = input_lines[0].split(",")

    g = ProgramGroup(16)
    moves = []
    digest_size = 400
    total_dances = 1000000000

    for j in range(digest_size):
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
    map = {}
    reverse_map = {}
    for i in range(len(start)):
        map[i] = end.find(start[i])
        reverse_map[map[i]] = i

    next = start
    for m in moves:
        if m.type == 3:
            next = next.replace(m.a, "Z")
            next = next.replace(m.b, m.a)
            next = next.replace("Z", m.b)

    partner_map = {}
    for i in range(len(start)):
        partner_map[start[i]] = next[i]
        # print("Swap {} with {}".format(start[i],next[i]))

    next = start
    for each_dance in range(int(total_dances/digest_size)):
        next = "".join(x for x in [next[reverse_map[i]] for i in range(len(next))])
        next = "".join(x for x in [partner_map[c] for c in next])

    return next