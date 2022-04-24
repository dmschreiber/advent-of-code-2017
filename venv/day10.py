class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
        self.prevval = None

class SLinkedList:
    def __init__(self):
        self.headval = None


def part1(input, size):
    log = False
    list1 = SLinkedList()
    list1.headval = Node(0)
    last_val = list1.headval

    for i in range(1,size):
        e = Node(i)
        e.prevval = last_val
        last_val.nextval = e
        last_val = e
        if i == size-1:
            e.nextval = list1.headval
            list1.headval.prevval = e

    if log:
        print("Starting list:")
        e = list1.headval
        for i in range(0,size+1):
            print(e.dataval, end=" ")
            e = e.nextval
        print()

    # setup done
    lengths = input.split(",")
    lengths = [int(x) for x in lengths]
    skip_size = 0
    current = list1.headval

    for length in lengths:
        if log: print("length {}".format(length))
        nums = []
        for i in range(length):
            nums.append(current.dataval)
            current = current.nextval

        for n in nums:
            current = current.prevval
            current.dataval = n

        for i in range(length+skip_size):
            current = current.nextval

        skip_size += 1

        if log:
            e = list1.headval
            for i in range(0,size):
                print(e.dataval, end=" ")
                e = e.nextval
            print()

    return list1.headval.dataval * list1.headval.nextval.dataval

def get_part2_lengths(input):

    lengths = [ord(x) for x in input]
    lengths = lengths + [17, 31, 73, 47, 23]
    return lengths

def sparce_hash(nums):
    output = nums[0]
    for n in range(1,len(nums)):
        output = output ^ nums[n]
    return output



def part2(input, size):
    log = False
    list1 = SLinkedList()
    list1.headval = Node(0)
    last_val = list1.headval

    for i in range(1,size):
        e = Node(i)
        e.prevval = last_val
        last_val.nextval = e
        last_val = e
        if i == size-1:
            e.nextval = list1.headval
            list1.headval.prevval = e

    if log:
        print("Starting list:")
        e = list1.headval
        for i in range(0,size+1):
            print(e.dataval, end=" ")
            e = e.nextval
        print()

    # setup done
    lengths = get_part2_lengths(input)

    skip_size = 0
    current = list1.headval

    for round in range(64):
        for length in lengths:
            if log: print("length {}".format(length))
            nums = []
            for i in range(length):
                nums.append(current.dataval)
                current = current.nextval

            for n in nums:
                current = current.prevval
                current.dataval = n

            for i in range(length+skip_size):
                current = current.nextval

            skip_size += 1

    e = list1.headval
    output = ""
    output_nums = []
    if size == 256:
        for i in range(16):
            nums = []
            for j in range(16):
                nums.append(e.dataval)
                e = e.nextval
            output_nums += [sparce_hash(nums)]

        output = "".join("{:02x}".format(x) for x in output_nums)


    return output
