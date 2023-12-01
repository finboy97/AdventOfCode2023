import pandas as pd
from source.day_01.day_01 import retrieve_calibration_with_words
test_input_1 = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

test_input_2 = pd.DataFrame(
    [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
        "eighthree"
    ],
    columns=["line"]
)

def test_part_2():
    assert retrieve_calibration_with_words(test_input_2)==364