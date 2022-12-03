#from day1.day1puzzles import *
#from day2.day2puzzles import *
from day3.day3puzzles import *

def read_file(fileName):
    with open(fileName) as f:
        lines = f.readlines()
        f.close()

    return lines

if __name__ == '__main__':
    lines = read_file('day3/input.txt')
    #result = get_max_calories(lines)
    #result = get_top3_calories(lines)
    #result = estimate_score(lines)
    #result = calculate_score(lines)
    result = get_common_priority_sum(lines)
    print(result)
