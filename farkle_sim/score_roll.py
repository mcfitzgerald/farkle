"""
Module contains functions to score an analyzed roll.
"""
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
    "five-of-a-kind": 2000,
    "six-of-a-kind": 3000,
    "straight": 1500,
    "three-pairs": 1500,
    "four-and-pair": 1500,
    "triplets": 2500,
}

dice_count = {
    "three-ones": 3,
    "three-twos": 3,
    "three-threes": 3,
    "three-fours": 3,
    "three-fives": 3,
    "three-sixes": 3,
    "four-of-a-kind": 4,
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

    hi_combo_keys = ["four-of-a-kind", "five-of-a-kind", "six-of-a-kind"]

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


def gather_singles(analyzed_roll):
    """
    Identify , count, and score any occuring single in a roll.
    """

    singles = []

    # test for 3 pairs exception

    if analyzed_roll["three-pairs"]:
        if analyzed_roll["one"] == 2:
            single_keys = ["five"]
        if analyzed_roll["five"] == 2:
            single_keys = ["one"]
        if analyzed_roll["one"] == 2 and analyzed_roll["five"] == 2:
            single_keys = []
    else:
        single_keys = ["one", "five"]

    for i in single_keys:
        # drops if 3ok present
        # still need to handle pairs (1,1,5,5,x,x) - see below
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
