item_rankings = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def get_priority_sum(rucksack_contents):
    score = 0
    for i in range(len(rucksack_contents)):
        duplicated_item = ''
        for j in range(len(rucksack_contents[i].strip()) // 2):
            current_item = rucksack_contents[i].strip()[j]
            for k in range(len(rucksack_contents[i].strip()) // 2):
                halfway = len(rucksack_contents[i].strip()) // 2
                if rucksack_contents[i].strip()[halfway + k] == current_item:
                    duplicated_item = current_item
                    break
        score = score + item_rankings.index(duplicated_item) + 1

    return score

def get_common_priority_sum(rucksack_contents):
    score = 0
    for i in range(len(rucksack_contents) // 3):
        duplicated_item = ''
        duplicate_list = []
        group = [rucksack_contents[i * 3].strip(), rucksack_contents[i * 3 + 1].strip(), rucksack_contents[i * 3 + 2].strip()]
        group.sort()
        for j in range(len(group[0])):
            current_item = group[0][j]
            for k in range(len(group[1])):
                if group[1][k] == current_item and current_item not in duplicate_list:
                    duplicate_list.append(current_item)
            for k in range(len(group[2])):
                if group[2][k] in duplicate_list:
                    duplicated_item = group[2][k]
                    break
        score = score + item_rankings.index(duplicated_item) + 1

    return score