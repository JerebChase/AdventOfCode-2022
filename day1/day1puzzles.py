def get_max_calories(calories):
    max_calories = 0
    current_calories = 0
    elf_calories = []
    for i in range(len(calories)):
        if calories[i].strip() == '':
            elf_calories.append(current_calories)
            if current_calories > max_calories:
                max_calories = current_calories
            current_calories = 0
        else:
            current_calories = current_calories + int(calories[i].strip())

    return max_calories

def get_top3_calories(calories):
    max_calories = 0
    current_calories = 0
    elf_calories = []
    for i in range(len(calories)):
        if calories[i].strip() == '':
            elf_calories.append(current_calories)
            if current_calories > max_calories:
                max_calories = current_calories
            current_calories = 0
        else:
            current_calories = current_calories + int(calories[i].strip())

    elf_calories.sort(reverse=True)
    return elf_calories[0] + elf_calories[1] + elf_calories[2]