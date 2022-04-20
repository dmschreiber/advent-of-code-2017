import collections


def redistribute(input):
    banks = input.split()
    banks = [int(i) for i in banks]

    max_mem = max(banks)
    which_bank = -1
    for i in range(0,len(banks)):
        if banks[i] == max_mem:
            which_bank = i
            break

    if which_bank < 0:
        raise NotImplemented

    new_banks = banks.copy()
    new_banks[which_bank] = 0

    # 8 / 4 = 2
    # 7 / 4 = 1.75
    if banks[which_bank]/len(banks) != int(banks[which_bank]/len(banks)):
        how_much_to_add = int(banks[which_bank]/len(banks)) + 1
    else:
        how_much_to_add = int(banks[which_bank]/len(banks))

    count_down = banks[which_bank]
    index = (which_bank + 1) % len(banks)
    for i in range(0,len(banks)):
        how_much_to_add = min(how_much_to_add,count_down)
        new_banks[index] = new_banks[index] + how_much_to_add
        count_down = count_down - how_much_to_add
        index = (index + 1) % len(banks)

    new_banks = [str(i) for i in new_banks]
    return " ".join(new_banks)

def part1(input):
    history = []

    loop_count = 0

    current_state = input
    while not current_state in history:
        history.insert(0,current_state)
        current_state = redistribute(current_state)
        loop_count = loop_count + 1

    return loop_count

def part2(input):
    history = []


    current_state = input
    while not current_state in history:
        history.insert(0,current_state)
        current_state = redistribute(current_state)

    loop_size = 0
    for item in history:
        loop_size = loop_size + 1
        if item == current_state:
            return loop_size

    return loop_size