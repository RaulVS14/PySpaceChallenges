def sonic_how_many_rings_did_you_get(input_string):
    score_map = {
        "a": 1,
        "b": 1,
        "d": 1,
        "e": 1,
        "g": 1,
        "o": 1,
        "p": 1,
        "q": 1,
        "B": 2,
        "D": 1,
        "O": 1,
        "P": 1,
        "Q": 1,
        "R": 1,
        "0": 1,
        "6": 1,
        "8": 2,
        "9": 1
    }
    score = 0
    for i in input_string:
        if i in score_map:
            score += score_map[i]
    return score


if __name__ == '__main__':
    assert sonic_how_many_rings_did_you_get('Helloo') == 3
    assert sonic_how_many_rings_did_you_get("HELLOO") == 2
