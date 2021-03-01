import numpy as np

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
    'three-ones': 3,
    'three-twos': 3,
    'three-threes': 3,
    'three-fours': 3,
    'three-fives': 3,
    'three-sixes': 3,
    'four-of-a-kind': 4,
    'five-of-a-kind': 5,
    'six-of-a-kind': 6,
    'straight': 6,
    'three-pairs': 6,
    'four-and-pair': 6,
    'triplets': 6}

def gather_combos(analyzed_roll):
    three_combo_keys = [
        "three-ones",
        "three-twos",
        "three-threes",
        "three-fours",
        "three-fives",
        "three-sixes",
    ]
    
    hi_combo_keys = [
        "four-of-a-kind",
        "five-of-a-kind", 
        "six-of-a-kind"
    ]
    
    
    full_combo_keys = [
        "six-of-a-kind",
        "straight",
        "three-pairs",
        "four-and-pair",
        "triplets"
    ]
    
    combos = []
    
    for i in full_combo_keys:
        if analyzed_roll[i] == True:
            combos.append(i)
    if len(combos) == 0:
        for i in hi_combo_keys:
            if analyzed_roll[i] == True:
                combos.append(i)
    if len(combos) == 0:
        for i in three_combo_keys:
            if analyzed_roll[i] == True:
                combos.append(i)
                
    return combos

def gather_singles(analyzed_roll):
    single_keys = [
        "one",
        "five"
    ]
    
    singles = []
    
    for i in single_keys:
        # drops if triplet present
        if 3 > analyzed_roll[i] > 0:
            singles.append(i)
    
    return singles

def count_gathered(analyzed_roll):
    gathered_combos = gather_combos(analyzed_roll)
    gathered_singles = gather_singles(analyzed_roll)
    comb_score = []
    sing_score = []
    
    
    if len(gathered_combos)==0 and len(gathered_singles)== 0:
        print("FARKLE")

    elif len(gathered_combos) == 0:
        for i in gathered_singles:
            comb_score.append((i, (p_dict[i] * analyzed_roll[i]), analyzed_roll[i]))
        return comb_score

    elif len(gathered_singles) == 0:
        for i in gathered_combos:
            sing_score.append((i, p_dict[i], dice_count[i]))
        return sing_score
    
    else:
        for i in gathered_singles:
            comb_score.append((i, (p_dict[i] * analyzed_roll[i]), analyzed_roll[i]))
        for i in gathered_combos:
            sing_score.append((i, p_dict[i], dice_count[i]))
        return [comb_score, sing_score]
