#from day1.day1puzzles import *
#from day2.day2puzzles import *
#from day3.day3puzzles import *
#from day4.day4puzzles import *
#from day5.day5puzzles import *
from day6.day6puzzles import *

def read_file(fileName):
    with open(fileName) as f:
        lines = f.readlines()
        f.close()

    return lines

if __name__ == '__main__':
    lines = read_file('day6/input.txt')
    #result = get_max_calories(lines)
    #result = get_top3_calories(lines)
    #result = estimate_score(lines)
    #result = calculate_score(lines)
    #result = get_priority_sum(lines)
    #result = get_common_priority_sum(lines)
    #esult = get_fully_contained_assignments(lines)
    #result = get_overlapping_assignments(lines)
    #result = get_top_crates(lines)
    #result = get_subroutine_marker(lines)
    result = get_message_marker(lines)
    print(result)
