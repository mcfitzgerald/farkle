"""
Module contains functions to score an analyzed roll.
"""
# Point dictionary. Plan to make configurable.
p_dict = {
    "one": 100,
    "five": 50,
    "three-ones": 1000,
    "three-twos": 200,
    "three-threes": 300,
    "three-fours": 400,
    "three-fives": 500,
    "three-sixes": 600,
    "four-of-a-kind": 1000,
    "three-and-one": 1100,
    "five-of-a-kind": 2000,
    "six-of-a-kind": 3000,
    "straight": 1500,
    "three-pairs": 1500,
    "four-and-pair": 1500,
    "triplets": 2500,
}

# Number of dice in each combo
dice_count = {
    "three-ones": 3,
    "three-twos": 3,
    "three-threes": 3,
    "three-fours": 3,
    "three-fives": 3,
    "three-sixes": 3,
    "four-of-a-kind": 4,
    "three-and-one": 4,
    "five-of-a-kind": 5,
    "six-of-a-kind": 6,
    "straight": 6,
    "three-pairs": 6,
    "four-and-pair": 6,
    "triplets": 6,
}


def gather_combos(analyzed_roll):
    """
    Identify , count, and score any occuring combinations in a roll.
    """
    three_combo_keys = [
        "three-ones",
        "three-twos",
        "three-threes",
        "three-fours",
        "three-fives",
        "three-sixes",
    ]

    hi_combo_keys = ["four-of-a-kind", "three-and-one", "five-of-a-kind"]

    full_combo_keys = [
        "six-of-a-kind",
        "straight",
        "three-pairs",
        "four-and-pair",
        "triplets",
    ]

    combos = []

    for i in full_combo_keys:
        if analyzed_roll[i]:
            combos.append(i)
    if len(combos) == 0:
        for i in hi_combo_keys:
            if analyzed_roll[i]:
                combos.append(i)
    if len(combos) == 0:
        for i in three_combo_keys:
            if analyzed_roll[i]:
                combos.append(i)

    return combos


def handle_four_and_pair(analyzed_roll):
    """Case switching lookup to handle four and pairs containing 1 or 5"""
    case = (analyzed_roll["one"], analyzed_roll["five"])
    print(f"the four-and-pair case is {case}")

    _lookup = {
        (2, 0): ["five"],
        (4, 0): ["five"],
        (0, 2): ["one"],
        (0, 4): ["one"],
        (2, 4): [],
        (4, 2): [],
    }

    return _lookup.get(case, ["one", "five"])


def handle_three_pair(analyzed_roll):
    """Case switching lookup to handle three pairs containing 1 or 5"""
    case = (analyzed_roll["one"], analyzed_roll["five"])
    print(f"the three-pair case is {case}")

    _lookup = {
        (2, 0): ["five"],
        (0, 2): ["one"],
        (2, 2): [],
    }

    return _lookup.get(case, ["one", "five"])


def gather_singles(analyzed_roll):
    """
    Identify , count, and score any occuring single in a roll.
    """

    singles = []
    single_keys = ["one", "five"]

    # test for 4 and pair exception
    if analyzed_roll["four-and-pair"]:
        single_keys = handle_four_and_pair(analyzed_roll)

    # test for 3 pair exception
    if analyzed_roll["three-pairs"]:
        single_keys = handle_three_pair(analyzed_roll)

    # test for straight exception
    if analyzed_roll["straight"]:
        single_keys = []

    # test for 3 and 1 exception
    if analyzed_roll["three-and-one"]:
        single_keys = ["five"]

    for i in single_keys:
        # drops if 3ok present
        # handles triplets too!
        if 3 > analyzed_roll[i] > 0:
            singles.append(i)

    return singles


def count_gathered(analyzed_roll):
    """
    Combines combos and singles and filters for any duplicates.
    Returns a list of tuples with high-scoring combos/single, number of dice, and points.
    If farkle, and empty list is returned.

    Example output:
    roll: [1,1,5,5,2,2]
    tally: [[], [('three-pairs', 1500, 6)]]
    """
    gathered_combos = gather_combos(analyzed_roll)
    gathered_singles = gather_singles(analyzed_roll)
    comb_score = []
    sing_score = []

    for i in gathered_singles:
        sing_score.append((i, (p_dict[i] * analyzed_roll[i]), analyzed_roll[i]))

    for i in gathered_combos:
        comb_score.append((i, p_dict[i], dice_count[i]))

    return [sing_score, comb_score]
