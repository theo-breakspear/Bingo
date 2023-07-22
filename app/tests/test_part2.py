from app.tests.constants import LOSING_STRING, NUMBERS, WINNING_STRING
from app.part2 import part2


class Test_part2:
    def test_returns_card1_if_1_wins(self):
        assert (
            part2(
                f"{NUMBERS}\n\n{WINNING_STRING}\n\n{LOSING_STRING}\n\n{LOSING_STRING}"
            )
            == "Card 1 wins"
        )

    def test_returns_card2_if_2_wins(self):
        assert (
            part2(
                f"{NUMBERS}\n\n{LOSING_STRING}\n\n{WINNING_STRING}\n\n{LOSING_STRING}"
            )
            == "Card 2 wins"
        )

    def test_returns_card3_if_3_wins(self):
        assert (
            part2(
                f"{NUMBERS}\n\n{LOSING_STRING}\n\n{LOSING_STRING}\n\n{WINNING_STRING}"
            )
            == "Card 3 wins"
        )

    def test_returns_draw_if_no_bingo(self):
        assert (
            part2(f"{NUMBERS}\n\n{LOSING_STRING}\n\n{LOSING_STRING}\n\n{LOSING_STRING}")
            == "All cards draw"
        )

    def test_returns_draw_if_all_win(self):
        assert (
            part2(
                f"{NUMBERS}\n\n{WINNING_STRING}\n\n{WINNING_STRING}\n\n{WINNING_STRING}"
            )
            == "All cards draw"
        )

    def test_returns_draw_if_1_and_2_draw(self):
        assert (
            part2(
                f"{NUMBERS}\n\n{WINNING_STRING}\n\n{WINNING_STRING}\n\n{LOSING_STRING}"
            )
            == "Cards 1 and 2 draw"
        )

    def test_returns_draw_if_2_and_3_draw(self):
        assert (
            part2(
                f"{NUMBERS}\n\n{LOSING_STRING}\n\n{WINNING_STRING}\n\n{WINNING_STRING}"
            )
            == "Cards 2 and 3 draw"
        )

    def test_returns_draw_if_1_and_3_draw(self):
        assert (
            part2(
                f"{NUMBERS}\n\n{WINNING_STRING}\n\n{LOSING_STRING}\n\n{WINNING_STRING}"
            )
            == "Cards 1 and 3 draw"
        )
