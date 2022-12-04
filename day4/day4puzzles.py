def get_fully_contained_assignments(assignment_pairs):
    fully_contained_assignments = 0
    for i in range(len(assignment_pairs)):
        assignments = assignment_pairs[i].strip().split(',')
        assignment1 = assignments[0].split('-')
        assignment2 = assignments[1].split('-')
        if (int(assignment1[0]) >= int(assignment2[0]) and int(assignment1[1]) <= int(assignment2[1])) or (
                int(assignment2[0]) >= int(assignment1[0]) and int(assignment2[1]) <= int(assignment1[1])):
            fully_contained_assignments += 1

    return fully_contained_assignments

def get_overlapping_assignments(assignment_pairs):
    overlapping_assignments = 0
    for i in range(len(assignment_pairs)):
        assignments = assignment_pairs[i].strip().split(',')
        assignment1 = assignments[0].split('-')
        assignment2 = assignments[1].split('-')
        if (int(assignment1[0]) <= int(assignment2[0]) <= int(assignment1[1])) or (
                int(assignment1[0]) <= int(assignment2[1]) <= int(assignment1[1])) or (
                int(assignment2[0]) <= int(assignment1[0]) <= int(assignment2[1])) or (
                int(assignment2[0]) <= int(assignment1[1]) <= int(assignment2[1])):
            overlapping_assignments += 1

    return overlapping_assignments