
def win():
    return 6

def loss():
    return 0

def draw():
    return 3

def det_outcome(move):
    match move:
        case "AX":
            return draw()
        case "BY":
            return draw()
        case "CZ":
            return draw()
        case "AY":
            return win()
        case "AZ":
            return loss()
        case "BX":
            return loss()
        case "BZ":
            return win()
        case "CY":
            return loss()
        case "CX":
            return win()

    raise Exception("This should not be reaced")

def translate_match(opp, outcome):
    
    match opp:
        case "A":
            match outcome:
                case "X":
                    return "Z"
                case "Y":
                    return "X"
                case "Z":
                    return "Y"
        case "B":
            match outcome:
                case "X":
                    return "X"
                case "Y":
                    return "Y"
                case "Z":
                    return "Z"
        case "C":
            match outcome:
                case "X":
                    return "Y"
                case "Y":
                    return "Z"
                case "Z":
                    return "X"
        

    raise Exception("This should not be reaced")

with open("input.txt", "r") as file:
    tot_score = 0
    for line in file:
        opp_move, my_move = line.split()
        score = {"X": 1, "Y": 2, "Z": 3}
        tot_score += score[my_move] + det_outcome("".join([opp_move, my_move]))
    
    print(f"Part1: {tot_score}")

with open("input.txt", "r") as file:
    tot_score = 0
    for line in file:
        opp_move, outcome = line.split()
        score = {"X": 1, "Y": 2, "Z": 3}
        my_move =  translate_match(opp_move, outcome)
        tot_score += score[my_move] + det_outcome("".join([opp_move, my_move]))
    
    print(f"Part2: {tot_score}")   