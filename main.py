#from day1.day1puzzles import *
#from day2.day2puzzles import *
#from day3.day3puzzles import *
#from day4.day4puzzles import *
#from day5.day5puzzles import *
#from day6.day6puzzles import *
#from day7.day7puzzles import *
from day8.day8puzzles import *

def read_file(fileName):
    with open(fileName) as f:
        lines = f.readlines()
        f.close()

    return lines

if __name__ == '__main__':
    lines = read_file('day8/input.txt')
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
    #result = get_message_marker(lines)
    #result = get_delete_dir_size(lines)
    #result = get_dir_to_delete(lines)
    #result = get_visible_trees(lines)
    result = get_best_scenic_score(lines)
    print(result)
