import re

def get_top_crates(input):
    top_crates = ""
    raw_stacks = []
    stacks = []
    for i in range(len(input)):
        if "[" in input[i]:
            # reading in the crate info
            crates = re.findall("[A-Z]|\s{4}", input[i])
            print(crates)
            raw_stacks.append(crates)
        elif "move" in input[i]:
            # for every line of instruction - move the crates
            instructions = re.findall("\d{1,}", input[i])
            crate_mover_9001(instructions, stacks)
        else:
            # after we've read in all the crates, put them in the right stacks
            if input[i].strip() == '':
                number_of_stacks = len(raw_stacks[0])
                for j in reversed(range(len(raw_stacks))):
                    for k in range(number_of_stacks):
                        if bool(re.search("[A-Z]", raw_stacks[j][k])):
                            if (len(stacks) < number_of_stacks):
                                stacks.append([])
                            stacks[k].append(raw_stacks[j][k])
    for stack in stacks:
        top_crates = top_crates + stack.pop()

    return top_crates

def crate_mover_9000(instructions, stacks):
    for _ in range(int(instructions[0])):
        crate = stacks[int(instructions[1]) - 1].pop()
        stacks[int(instructions[2]) - 1].append(crate)

def crate_mover_9001(instructions, stacks):
    create_holder = []
    for _ in range(int(instructions[0])):
        crate = stacks[int(instructions[1]) - 1].pop()
        create_holder.append(crate)
    for _ in range(len(create_holder)):
        crate = create_holder.pop()
        stacks[int(instructions[2]) - 1].append(crate)