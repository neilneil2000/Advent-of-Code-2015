"""Tests for Day 8"""

import pytest
from day_8 import real_length, read_file


@pytest.fixture
def puzzle_input():
    return read_file("day_8_input.txt")


test_parameters = [
    (read_file("day_8_input.txt")[0], 7),
    (read_file("day_8_input.txt")[1], 22),
    (read_file("day_8_input.txt")[2], 29),
    (read_file("day_8_input.txt")[3], 5),
    (read_file("day_8_input.txt")[4], 22),
    (read_file("day_8_input.txt")[5], 19),
    (read_file("day_8_input.txt")[6], 26),
]

""" [
    ("qxfcsmh", 7),
    (r'"ffsfyxbyuhqkpwatkjgudo"', 22),
    (r'"byc\x9dyxuafof\\\xa6uf\\axfozomj\\olh\x6a"', 29),
    (r'"jtqvz"', 5),
    (r""" 'uzezxa"jgbmojtwyfbfguz' """, 23),
    (r'"vqsremfk\x8fxiknektafj"', 20),
    (r""" 'wzntebpxnnt"vqndz"i\x47vvjqo"' """, 0),
    (r""" 'higvez"k"riewqk' """, 0),
    (r'"dlkrbhbrlfrp\\damiauyucwhty"', 0),
] """


@pytest.mark.parametrize("test_input,expected_output", test_parameters)
def test_real_length(test_input, expected_output):
    """Test for real_length function"""
    output = real_length(test_input)
    assert output == expected_output
