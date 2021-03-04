"""
Test suite for score_roll module
"""

import numpy as np
from farkle_sim import analyze_roll, score_roll


def test_score_ones_fives_triplets():
    """Test if triplets of 1s and 5s is properly scored"""
    roll = np.array([1, 1, 1, 5, 5, 5])
    expected = [[], [("triplets", 2500, 6)]]
    actual = score_roll.count_gathered(analyze_roll.get_scorable(roll))
    assert expected == actual


def test_score_ones_fives_pairs():
    """Test if pairs of 1s and 5s are properly scored"""
    roll = np.array([1, 1, 5, 5, 2, 2])
    expected = [[], [("three-pairs", 1500, 6)]]
    actual = score_roll.count_gathered(analyze_roll.get_scorable(roll))
    assert expected == actual


def test_score_straight():
    """Test if a straight is properly scored"""
    roll = np.array([5, 1, 4, 3, 2, 6])
    expected = [[], [("straight", 1500, 6)]]
    actual = score_roll.count_gathered(analyze_roll.get_scorable(roll))
    assert expected == actual

def test_score_four_and_pair_1and5():
    """Test if a four and pair is properly scored when 1s and 5s are rolled"""
    roll = np.array([1, 1, 1, 1, 5, 5])
    expected = [[], [("four-and-pair", 1500, 6)]]
    actual = score_roll.count_gathered(analyze_roll.get_scorable(roll))
    assert expected == actual