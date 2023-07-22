from app.tests.constants import LOSING_STRING, NUMBERS, WINNING_STRING
from app.part1 import part1


class Test_part1:
    def test_winning_input_returns_true(self):
        assert part1(f"{NUMBERS}\n\n{WINNING_STRING}") == True

    def test_losing_input_returns_false(self):
        assert part1(f"{NUMBERS}\n\n{LOSING_STRING}") == False
