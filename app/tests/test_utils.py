from app.tests.constants import (
    LOSING_STRING,
    NUMBERS,
    WINNING_COLUMN_STRING,
    WINNING_STRING,
)
from app.utils import separate_input


class Test_separate_input:
    def test_splits_part1_input_correctly(self):
        numbers_string, card_string = separate_input(f"{NUMBERS}\n\n{WINNING_STRING}")
        assert numbers_string == NUMBERS
        assert card_string == WINNING_STRING

    def test_splits_part2_input_correctly(self):
        numbers_string, card1_string, card2_string, card3_string = separate_input(
            f"{NUMBERS}\n\n{WINNING_STRING}\n\n{WINNING_COLUMN_STRING}\n\n{LOSING_STRING}"
        )
        assert numbers_string == NUMBERS
        assert card1_string == WINNING_STRING
        assert card2_string == WINNING_COLUMN_STRING
        assert card3_string == LOSING_STRING
