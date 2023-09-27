from itertools import permutations


def identify_ninja(ninja_name, all_villagers):
    list_of_permutations = [''.join(p) for p in permutations(ninja_name)]
    potential_names = []
    for villager in all_villagers:
        if villager in list_of_permutations:
            potential_names.append(villager)
    return potential_names


if __name__ == '__main__':
    assert identify_ninja('obb', ['bob', 'richard']) == ["bob"]
