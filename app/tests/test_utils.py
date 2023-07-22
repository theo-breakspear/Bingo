from app.tests.constants import (
    PART1_WINNING_CARD_STRING,
    PART1_WINNING_INPUT,
    PART1_WINNING_NUMBERS_STRING,
    PART2_CARD1_STRING,
    PART2_CARD2_STRING,
    PART2_CARD3_STRING,
    PART2_INPUT,
    PART2_NUMBERS_STRING,
)
from app.utils import separate_input


class Test_separate_input:
    def test_splits_part1_input_correctly(self):
        numbers_string, card_string = separate_input(PART1_WINNING_INPUT)
        assert numbers_string == PART1_WINNING_NUMBERS_STRING
        assert card_string == PART1_WINNING_CARD_STRING

    def test_splits_part2_input_correctly(self):
        numbers_string, card1_string, card2_string, card3_string = separate_input(
            PART2_INPUT
        )
        assert numbers_string == PART2_NUMBERS_STRING
        assert card1_string == PART2_CARD1_STRING
        assert card2_string == PART2_CARD2_STRING
        assert card3_string == PART2_CARD3_STRING
