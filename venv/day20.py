def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    smallest_a = 1000000000
    which = 0
    which_smallest = 0

    for l in input_lines:
        p = l.split(", ")
        pos = p[0][3:-1].split(",")
        v = p[1][3:-1].split(",")
        a = p[2][3:-1].split(",")

        net_a = abs(int(a[0])) + abs(int(a[1])) + abs(int(a[2]))
        if net_a < smallest_a:
            print("which {} is {} smaller than {}".format(which, net_a, smallest_a))
            which_smallest = which
            smallest_a = net_a

        which = which + 1

    return which_smallest

def part2(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    particles = []

    for l in input_lines:
        p = l.split(", ")
        pos = [int(c) for c in p[0][3:-1].split(",")]
        v = [int(c) for c in p[1][3:-1].split(",")]
        a = [int(c) for c in p[2][3:-1].split(",")]
        particles.append([pos,v,a])

    for t in range(100):
        # print("time {} particle count {}".format(t,len(particles)))
        for p in particles:
            p[1][0] = p[1][0] + p[2][0]
            p[1][1] = p[1][1] + p[2][1]
            p[1][2] = p[1][2] + p[2][2]

            p[0][0] = p[0][0] + p[1][0]
            p[0][1] = p[0][1] + p[1][1]
            p[0][2] = p[0][2] + p[1][2]

        remove_list = []
        p_index = 0
        for p in particles:
            q_index = 0
            for q in particles:
                if p[0][0] == q[0][0] and p[0][1] == q[0][1] and p[0][2] == q[0][2] and p_index != q_index:
                    remove_list.append(p_index)
                    remove_list.append(q_index)
                q_index = q_index + 1
            p_index = p_index + 1

        # if len(remove_list) > 0:
        #     print("Collisions time {} - {}".format(t,remove_list))
        #     print(particles)

        new_particles = []
        for i in range(len(particles)):
            if i not in remove_list:
                new_particles.append((particles[i]))

        particles = new_particles

    return len(particles)

