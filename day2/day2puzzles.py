def estimate_score(game_input):
    score = 0
    for i in range(len(game_input)):
        inputs = game_input[i].strip().split()
        if inputs[0] == 'A':
            if inputs[1] == 'X':
                score = score + 1 + 3
            elif inputs[1] == 'Y':
                score = score + 2 + 6
            elif inputs[1] == 'Z':
                score = score + 3 + 0
            else:
                score = score
        elif inputs[0] == 'B':
            if inputs[1] == 'X':
                score = score + 1 + 0
            elif inputs[1] == 'Y':
                score = score + 2 + 3
            elif inputs[1] == 'Z':
                score = score + 3 + 6
            else:
                score = score
        elif inputs[0] == 'C':
            if inputs[1] == 'X':
                score = score + 1 + 6
            elif inputs[1] == 'Y':
                score = score + 2 + 0
            elif inputs[1] == 'Z':
                score = score + 3 + 3
            else:
                score = score
        else:
            score = score

    return score

def calculate_score(game_input):
    score = 0
    for i in range(len(game_input)):
        inputs = game_input[i].strip().split()
        if inputs[0] == 'A':
            if inputs[1] == 'X':
                score = score + 3 + 0
            elif inputs[1] == 'Y':
                score = score + 1 + 3
            elif inputs[1] == 'Z':
                score = score + 2 + 6
            else:
                score = score
        elif inputs[0] == 'B':
            if inputs[1] == 'X':
                score = score + 1 + 0
            elif inputs[1] == 'Y':
                score = score + 2 + 3
            elif inputs[1] == 'Z':
                score = score + 3 + 6
            else:
                score = score
        elif inputs[0] == 'C':
            if inputs[1] == 'X':
                score = score + 2 + 0
            elif inputs[1] == 'Y':
                score = score + 3 + 3
            elif inputs[1] == 'Z':
                score = score + 1 + 6
            else:
                score = score
        else:
            score = score

    return score
