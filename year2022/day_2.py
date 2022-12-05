from year2022 import read_input

STONE = 'X'
PAPER = 'Y'
SCISSORS = 'Z'

DRAW = 'draw'
WIN = 'win'
LOST = 'lost'

choices_map = {
    'A': STONE,
    'B': PAPER,
    'C': SCISSORS,
}

points = {
    STONE: 1,
    PAPER: 2,
    SCISSORS: 3,
}

result_points = {
    LOST: 0,
    DRAW: 3,
    WIN: 6,
}

whom_defeat = {
    STONE: SCISSORS,
    PAPER: STONE,
    SCISSORS: PAPER
}

need_to = {
    'X': LOST,
    'Y': DRAW,
    'Z': WIN
}


def calculate_score(my_choice, opp_choice):
    score = points[my_choice]
    if choices_map[opp_choice] == my_choice:  # is it draw?
        score += result_points[DRAW]
    else:
        if whom_defeat[my_choice] == choices_map[opp_choice]:  # is it win?
            score += result_points[WIN]
    return score


def day_2(test_data=None):
    data = test_data or read_input()
    my_score_v1, my_score_v2 = 0, 0
    for line in data:
        opp, my = line.split(' ')
        my_score_v1 += calculate_score(my, opp)
    for line in data:
        opp, need = line.split(' ')
        my = choices_map[opp]
        if need_to[need] == LOST:
            my = whom_defeat[choices_map[opp]]
        if need_to[need] == WIN:
            my = list(whom_defeat.keys())[list(whom_defeat.values()).index(choices_map[opp])]
        my_score_v2 += calculate_score(my, opp)
    return my_score_v1, my_score_v2
