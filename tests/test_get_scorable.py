"""
Test suite for get_scorable module
"""

import numpy as np
from farkle_sim import analyze_roll


def test_count_roll():
    """Test if rolls are counted properly"""
    expected = np.array([3, 0, 1, 2, 0, 0])
    result = analyze_roll.count_roll(np.array([1, 1, 3, 1, 4, 4]))
    assert np.array_equal(expected, result) is True


def test_count_roll_fail():
    """Test is roll count fails properly"""
    expected = np.array([3, 0, 1, 5, 0, 0])
    result = analyze_roll.count_roll(np.array([1, 1, 3, 1, 4, 4]))
    assert np.array_equal(expected, result) is False


def test_get_scorable_ones_fives():
    """Test if ones, fives, and triplets are found"""
    roll = np.array([1, 1, 1, 5, 5, 5])
    expected = {
        "one": 3,
        "five": 3,
        "three-ones": True,
        "three-twos": False,
        "three-threes": False,
        "three-fours": False,
        "three-fives": True,
        "three-sixes": False,
        "four-of-a-kind": False,
        "five-of-a-kind": False,
        "six-of-a-kind": False,
        "straight": False,
        "three-pairs": False,
        "four-and-pair": False,
        "triplets": True,
    }
    actual = analyze_roll.get_scorable(roll)
    assert expected == actual

def test_get_scorable_twos_34okp():
    """Test if twos and 4ok and pair found"""
    roll = np.array([2, 2, 2, 2, 6, 6])
    expected = {
        "one": 0,
        "five": 0,
        "three-ones": False,
        "three-twos": False,
        "three-threes": False,
        "three-fours": False,
        "three-fives": False,
        "three-sixes": False,
        "four-of-a-kind": True,
        "five-of-a-kind": False,
        "six-of-a-kind": False,
        "straight": False,
        "three-pairs": False,
        "four-and-pair": True,
        "triplets": False,
    }
    actual = analyze_roll.get_scorable(roll)
    assert expected == actual

def test_get_scorable_threes_5ok():
    """Test if 5ok (3) and a 1 found"""
    roll = np.array([3, 3, 3, 3, 3, 1])
    expected = {
        "one": 1,
        "five": 0,
        "three-ones": False,
        "three-twos": False,
        "three-threes": False,
        "three-fours": False,
        "three-fives": False,
        "three-sixes": False,
        "four-of-a-kind": False,
        "five-of-a-kind": True,
        "six-of-a-kind": False,
        "straight": False,
        "three-pairs": False,
        "four-and-pair": False,
        "triplets": False,
    }
    actual = analyze_roll.get_scorable(roll)
    assert expected == actual

def test_get_scorable_4_6_3ok():
    """Test if 3ok 4 and 6 are found"""
    roll = np.array([4, 4, 4, 6, 6, 6])
    expected = {
        "one": 0,
        "five": 0,
        "three-ones": False,
        "three-twos": False,
        "three-threes": False,
        "three-fours": True,
        "three-fives": False,
        "three-sixes": True,
        "four-of-a-kind": False,
        "five-of-a-kind": False,
        "six-of-a-kind": False,
        "straight": False,
        "three-pairs": False,
        "four-and-pair": False,
        "triplets": True,
    }
    actual = analyze_roll.get_scorable(roll)
    assert expected == actual

def test_get_scorable_6ok_1():
    """Test if 6ok 1 are found"""
    roll = np.array([1, 1, 1, 1, 1, 1])
    expected = {
        "one": 6,
        "five": 0,
        "three-ones": False,
        "three-twos": False,
        "three-threes": False,
        "three-fours": False,
        "three-fives": False,
        "three-sixes": False,
        "four-of-a-kind": False,
        "five-of-a-kind": False,
        "six-of-a-kind": True,
        "straight": False,
        "three-pairs": False,
        "four-and-pair": False,
        "triplets": False,
    }
    actual = analyze_roll.get_scorable(roll)
    assert expected == actual

def test_get_scorable_straight():
    """Test if 6ok 1 are found"""
    roll = np.array([1, 2, 3, 4, 5, 6])
    expected = {
        "one": 1,
        "five": 1,
        "three-ones": False,
        "three-twos": False,
        "three-threes": False,
        "three-fours": False,
        "three-fives": False,
        "three-sixes": False,
        "four-of-a-kind": False,
        "five-of-a-kind": False,
        "six-of-a-kind": False,
        "straight": True,
        "three-pairs": False,
        "four-and-pair": False,
        "triplets": False,
    }
    actual = analyze_roll.get_scorable(roll)
    assert expected == actual

def test_get_scorable_3pair():
    """Test if 3 pair is found"""
    roll = np.array([1, 1, 5, 5, 2, 2])
    expected = {
        "one": 2,
        "five": 2,
        "three-ones": False,
        "three-twos": False,
        "three-threes": False,
        "three-fours": False,
        "three-fives": False,
        "three-sixes": False,
        "four-of-a-kind": False,
        "five-of-a-kind": False,
        "six-of-a-kind": False,
        "straight": False,
        "three-pairs": True,
        "four-and-pair": False,
        "triplets": False,
    }
    actual = analyze_roll.get_scorable(roll)
    assert expected == actual

def test_get_scorable_partial_roll_3ok_1():
    """Test if 3ok 1 is found"""
    roll = np.array([1, 1, 1])
    expected = {
        "one": 3,
        "five": 0,
        "three-ones": True,
        "three-twos": False,
        "three-threes": False,
        "three-fours": False,
        "three-fives": False,
        "three-sixes": False,
        "four-of-a-kind": False,
        "five-of-a-kind": False,
        "six-of-a-kind": False,
        "straight": False,
        "three-pairs": False,
        "four-and-pair": False,
        "triplets": False,
    }
    actual = analyze_roll.get_scorable(roll)
    assert expected == actual

def test_get_scorable_partial_roll_4ok_4():
    """Test if 4ok 4 pair is found"""
    roll = np.array([4, 4, 4, 4, 2])
    expected = {
        "one": 0,
        "five": 0,
        "three-ones": False,
        "three-twos": False,
        "three-threes": False,
        "three-fours": False,
        "three-fives": False,
        "three-sixes": False,
        "four-of-a-kind": True,
        "five-of-a-kind": False,
        "six-of-a-kind": False,
        "straight": False,
        "three-pairs": False,
        "four-and-pair": False,
        "triplets": False,
    }
    actual = analyze_roll.get_scorable(roll)
    assert expected == actual