"""
This module contains functions to determine which dice \
or combinations of dice in a roll can be scored
"""
import numpy as np

# defined for comparison
straight_array = np.array([1, 2, 3, 4, 5, 6])


def count_roll(roll):
    """
    Takes an array of of dice rolls and counts recurrent values. It will always return a 1x6 array
    representing values 1,2,3,4,5,6 in their respective positions.
    """
    return np.array([np.sum(roll == i) for i in range(1, 7)])


def get_scorable(roll):
    """
    takes numpy array of counted simulated roll and returns dict
    of scorable dice and combos of dice.
    """
    counted_roll = count_roll(roll)

    scorable = {}

    # single dice
    scorable["one"] = counted_roll[0]  # count of ones in first (0 index) position
    scorable["five"] = counted_roll[4]  # count of fives in fifth (4 index) position

    # 3 of a kind
    tok_keys = [
        "three-ones",
        "three-twos",
        "three-threes",
        "three-fours",
        "three-fives",
        "three-sixes",
    ]
    tok_array = counted_roll == 3
    for i in range(0, 6):
        scorable[tok_keys[i]] = tok_array[i]

    # combos
    scorable["four-of-a-kind"] = (counted_roll[1:] == 4).any() # excludes one position
    scorable["three-and-one"] = (counted_roll[0] == 4) # special case count 4ok ones as 3 and 1 for 1100 pts.
    scorable["five-of-a-kind"] = (counted_roll == 5).any()
    scorable["six-of-a-kind"] = (counted_roll == 6).any()
    scorable["straight"] = np.isin(straight_array, roll).all()
    scorable["three-pairs"] = (counted_roll == 2).sum() == 3
    scorable["four-and-pair"] = (counted_roll == 4).any() and (counted_roll == 2).any()
    scorable["triplets"] = (counted_roll == 3).sum() == 2

    # handle four and pair with ones vs three and one 
    if scorable["four-and-pair"]:
        scorable["three-and-one"] = False
    

    return scorable
