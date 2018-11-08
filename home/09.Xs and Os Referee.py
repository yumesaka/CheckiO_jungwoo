from typing import List

def checkio(game_result):
    m = ''
    for e in game_result:
        m += e

    combinations = []
    combinations += game_result  # Row
    combinations += [m[e::3] for e in range(3)]  # Columns
    combinations += [m[::4]]  # Main Diagonal
    combinations += [m[2:7:2]]  # Second Diagonal

    x = 'XXX'  # x wins
    o = 'OOO'  # o wins

    if x in combinations:
        return 'X'
    elif o in combinations:
        return 'O'
    else:
        return 'D'


if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")