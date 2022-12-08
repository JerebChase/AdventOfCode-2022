def get_visible_trees(input):
    forest = []
    for line in input:
        forest.append(list(line.strip()))
    visible_trees = (len(forest) * len(forest[0])) - ((len(forest) - 2) * (len(forest[0]) - 2))
    for i in range(len(forest) - 2):
        for j in range(len(forest[i]) - 2):
            tree = forest[i + 1][j + 1]
            left = forest[i + 1][0:j + 1]
            right = forest[i + 1][j + 2:]
            up = []
            for u in range(i + 1):
                up.append(forest[u][j + 1])
            down = []
            for d in range(i + 2, len(forest)):
                down.append(forest[d][j + 1])
            if max(left) < tree or max(right) < tree or max(up) < tree or max(down) < tree:
                visible_trees += 1
    return visible_trees

def get_best_scenic_score(input):
    forest = []
    for line in input:
        forest.append(list(line.strip()))
    scenic_score = 0
    for i in range(len(forest) - 2):
        for j in range(len(forest[i]) - 2):
            tree = forest[i + 1][j + 1]
            left = forest[i + 1][0:j + 1]
            left.reverse()
            left_score = next((x + 1 for x, val in enumerate(left) if val >= tree), len(left))
            right = forest[i + 1][j + 2:]
            right_score = next((x + 1 for x, val in enumerate(right) if val >= tree), len(right))
            up = []
            for u in range(i + 1):
                up.append(forest[u][j + 1])
            up.reverse()
            up_score = next((x + 1 for x, val in enumerate(up) if val >= tree), len(up))
            down = []
            for d in range(i + 2, len(forest)):
                down.append(forest[d][j + 1])
            down_score = next((x + 1 for x, val in enumerate(down) if val >= tree), len(down))
            score = left_score * right_score * up_score * down_score
            if score > scenic_score:
                scenic_score = score
    return scenic_score
