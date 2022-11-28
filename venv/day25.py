import re

def get_value(map,pos):
    if pos in map.keys():
        return map[pos]
    else:
        return 0


def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    instructions = {}

    begin_state = input_lines[0][15]
    print("Begin state {}".format(begin_state))

    result = re.search(r"\d+",input_lines[1])
    iterations = int(result.group())
    print("Iterations {}".format(iterations))

    for i in range(int((len(input_lines)-2)/10)):
        state = input_lines[i*10+3][9]
        read_value = 0
        result = re.search(r"\d+",input_lines[i*10+5])
        write_value = int(result.group())

        result = re.search(r"    - Move one slot to the (right|left).",input_lines[i*10+6])
        if result.group(1) == "right":
            move_value = 1
        elif result.group(1) == "left":
            move_value = -1
        else:
            raise Exception

        result = re.search(r"    - Continue with state ([A-Z]).",input_lines[i*10+7])
        next_state = result.group(1)

        print("State {}, if {} write {} move {} continue with {}".format(state, read_value, write_value, move_value, next_state))
        instructions[state + str(read_value)] = (write_value, move_value, next_state)

        read_value = 1
        result = re.search(r"\d+",input_lines[i*10+9])
        write_value = int(result.group())

        result = re.search(r"    - Move one slot to the (right|left).",input_lines[i*10+10])
        if result.group(1) == "right":
            move_value = 1
        elif result.group(1) == "left":
            move_value = -1
        else:
            raise Exception

        result = re.search(r"    - Continue with state ([A-Z]).",input_lines[i*10+11])
        next_state = result.group(1)

        print("State {}, if {} write {} move {} continue with {}".format(state, read_value, write_value, move_value, next_state))
        instructions[state + str(read_value)] = (write_value, move_value, next_state)

    state = begin_state
    index = 0
    map = {}

    for iteration in range(iterations):
        # print("index {}, map {}, about to run state{}".format(index,map,state))
        which = state + str(get_value(map,index))
        (write_value,move_value,next_state) = instructions[which]
        map[index] = write_value
        index = index + move_value
        state = next_state


    return sum(map.values())

