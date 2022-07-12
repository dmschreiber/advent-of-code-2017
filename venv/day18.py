class SoundState:
    def __init__(self, instructions, p):
        self.registers = {}
        self.letters = "abcdefghijklmnopqrstuvwxyz"
        for register in self.letters:
            self.registers[register] = 0

        self.registers["p"] = p

        self.instructions = instructions
        self.index = 0
        self.last_sound_played = -1

    def step(self):
        instruction = self.instructions[self.index]
        instruction = instruction.split(" ")

        if len(instruction) > 2:
            if instruction[2] in self.letters:
                arg2 = self.registers[instruction[2]]
            else:
                arg2 =int(instruction[2])
        else:
            arg2 = -1

        if instruction[0] == "set":
            self.index = self.index + 1
            self.registers[instruction[1]] = arg2
        elif instruction[0] == "mul":
            self.index = self.index + 1
            self.registers[instruction[1]] = self.registers[instruction[1]]* arg2
        elif instruction[0] == "add":
            self.index = self.index + 1
            self.registers[instruction[1]] = self.registers[instruction[1]] + arg2
        elif instruction[0] == "mod":
            self.index = self.index + 1
            self.registers[instruction[1]] = self.registers[instruction[1]] % arg2
        elif instruction[0] == "snd":
            self.index = self.index + 1
            self.last_sound_played = int(self.registers[instruction[1]])
        elif instruction[0] == "rcv":
            self.index = self.index + 1
            if int(self.registers[instruction[1]]) != 0:
                return True
        elif instruction[0] == "jgz":
            if self.registers[instruction[1]] > 0:
               self.index = self.index + arg2
            else:
                self.index = self.index + 1

        else:
            raise Exception("invalid instruction")

        return False

def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    machine = SoundState(input_lines,0)

    recovered = False
    while not recovered:
        recovered = machine.step()


    print("Recovered {}".format(machine.last_sound_played))
    return machine.last_sound_played


class SendRcvState:
    def __init__(self, instructions, p):
        self.registers = {}
        self.letters = "abcdfip"
        for register in self.letters:
            self.registers[register] = 0

        self.registers["p"] = p

        self.instructions = instructions
        self.index = 0

        self.sent = []
        self.partner = None
        self.send_count = 0
        self.machine = p
        self.instruction_count = 0


    def step(self):
        instruction = self.instructions[self.index]
        instruction = instruction.split(" ")
        if len(instruction) > 2:
            if instruction[2] in self.letters:
                arg2 = self.registers[instruction[2]]
            else:
                arg2 = int(instruction[2])
        else:
            arg2 = -1

        if instruction[1] in self.letters:
            arg1 = self.registers[instruction[1]]
        else:
            arg1 = int(instruction[1])

        if instruction[0] == "set":
            self.index = self.index + 1
            self.registers[instruction[1]] = arg2
            self.instruction_count = self.instruction_count + 1

        elif instruction[0] == "mul":
            self.index = self.index + 1
            self.registers[instruction[1]] = self.registers[instruction[1]] * arg2
            self.instruction_count = self.instruction_count + 1

        elif instruction[0] == "add":
            self.index = self.index + 1
            self.registers[instruction[1]] = self.registers[instruction[1]] + arg2
            self.instruction_count = self.instruction_count + 1

        elif instruction[0] == "mod":
            self.index = self.index + 1
            self.registers[instruction[1]] = self.registers[instruction[1]] % arg2
            self.instruction_count = self.instruction_count + 1

        elif instruction[0] == "snd":
            # print("machine {} - {} - {}".format(self.machine, self.index, instruction))

            self.index = self.index + 1
            self.send_count = self.send_count + 1
            self.sent.append(arg1)
            self.instruction_count = self.instruction_count + 1

        elif instruction[0] == "rcv":
            # print("machine {} - {} - {}".format(self.machine, self.index, instruction))

            if len(self.partner.sent) > 0:
                self.index = self.index + 1
                self.registers[instruction[1]] = self.partner.sent[0]
                self.partner.sent.pop(0)
                self.instruction_count = self.instruction_count + 1

            else:
                return True

        elif instruction[0] == "jgz":
            self.instruction_count = self.instruction_count + 1
            if arg1 > 0:
                self.index = self.index + arg2
            else:
                self.index = self.index + 1

        else:
            raise Exception("invalid instruction")

        return False

def part2(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    machine1 = SendRcvState(input_lines,0)
    machine2 = SendRcvState(input_lines,1)
    machine1.partner = machine2
    machine2.partner = machine1

    wait1 = False
    wait2 = False
    last_index1 = -1
    last_index2 = -1
    progress1 = True
    progress2 = True

    while progress1 or progress2:
        last_index1 = machine1.instruction_count
        while not wait1:
            wait1 = machine1.step()
        progress1 = (last_index1 != machine1.instruction_count) or len(machine1.sent) > 0
        # print("{} {} {}".format(last_index1, machine1.instruction_count, len(machine1.sent)))
        # print("machine1 {}[{}], machine2 {}[{}]".format(machine1.instruction_count,len(machine1.sent),machine2.instruction_count,len(machine2.sent)))
        # print("progress1 {}".format(progress1))

        last_index2 = machine2.instruction_count
        while not wait2:
            wait2 = machine2.step()
        progress2 = (last_index2 != machine2.instruction_count) or len(machine2.sent) > 0

        wait1 = False
        wait2 = False

        # print("machine1 {}[{}], machine2 {}[{}]".format(machine1.instruction_count,len(machine1.sent),machine2.instruction_count,len(machine2.sent)))
        # print("machine 1: {}".format(machine1.registers))
        # print("machine 2: {}".format(machine2.registers))
    return machine2.send_count
