import time

def part1(how_many,ending_number,input):
    state = [0]
    # print("{}".format(state))
    pos = 0
    size = 1
    start_time = time.perf_counter()


    for i in range(how_many):
        pos = (pos + input) % size
        state.insert(pos+1,i+1)
        size = size + 1
        pos = pos + 1
        if (i % 100000) == 0:
            end_time = time.perf_counter()
            print(f"{pos} - {i} ({end_time - start_time:0.6f}s)")

    for i in range(len(state)):
        if state[i] == ending_number:
            return state[i+1]

    return -1

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

def do_insert(node, value):

    next = node.nextval

    new_node = Node(value)
    new_node.nextval = next

    node.nextval = new_node

    return new_node

def debug_print(node, how_many):
    next = node

    for i in range(how_many):
        print("{}".format(next.dataval),end=",")
        next = next.nextval

    print()

def find_neighbor(head, which, how_many):
    next = head
    first_value = head.dataval

    # print("looking for {}".format(which))
    # debug_print(head, how_many)
    for i in range(how_many):
        # print("{}".format(next.dataval))
        if next.dataval == which:
            return next.nextval.dataval
        next = next.nextval

    return -1

def part2(how_many,ending_number,input):
    head = Node(0)
    head.nextval = head
    head.prevval = head

    pos = 0
    size = 1
    start_time = time.perf_counter()


    for i in range(how_many):
        next = head
        pos = (pos + input) % size
        for j in range(input):
            next = next.nextval

        head = do_insert(next, i+1)

        size = size + 1
        pos = pos + 1

        # if i < 10:
        #     debug_print(head,size)
            # print("{} at {}".format(ending_number,find_neighbor(head,ending_number,size)))

        if (i % 100000) == 0:
            end_time = time.perf_counter()
            print(f"{pos} - {i} ({end_time - start_time:0.6f}s)")
            start_time = time.perf_counter()

    return find_neighbor(head, ending_number, size)

def others_answer():
    from collections import deque

    start_time = time.perf_counter()
    puzzle = 335
    spinlock = deque([0])

    for i in range(1, 50000001):
        spinlock.rotate(-puzzle)
        spinlock.append(i)

    print(spinlock[spinlock.index(0) + 1])
    end_time = time.perf_counter()
    print(f"Day 17 part 2 execution Time : {end_time - start_time:0.6f}s")
