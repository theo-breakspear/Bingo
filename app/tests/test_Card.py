from app.Card import Card

import pytest

from app.tests.constants import (
    LOSING_STRING,
    NUMBERS,
    WINNING_CARD_COLUMNS,
    WINNING_CARD_ROWS,
    WINNING_COLUMN_STRING,
    WINNING_STRING,
)


class Test_Card:
    @pytest.fixture()
    def winningRowCard(self):
        return Card(WINNING_STRING)

    @pytest.fixture()
    def winningColumnCard(self):
        return Card(WINNING_COLUMN_STRING)

    @pytest.fixture()
    def losingCard(self):
        return Card(LOSING_STRING)

    def test_Card_initializes_correct_rows(self, winningRowCard):
        assert winningRowCard.rows == WINNING_CARD_ROWS

    def test_Card_initializes_correct_columns(self, winningColumnCard):
        assert winningColumnCard.columns == WINNING_CARD_COLUMNS

    def test_play_bingo_returns_correct_number_for_a_winning_row(self, winningRowCard):
        assert winningRowCard.play_bingo(NUMBERS.split(",")) == 5

    def test_play_bingo_returns_infinity_for_no_win(self, losingCard):
        assert losingCard.play_bingo(NUMBERS.split(",")) == float("inf")
