from ..Card import Card
from .constants import (
    PART1_WINNING_CARD_STRING,
    PART1_WINNING_COLUMNS,
    PART1_WINNING_ROWS,
)
import pytest


@pytest.fixture()
def card():
    return Card(PART1_WINNING_CARD_STRING)


def test_Card_initializes_correct_columns(card):
    assert card.columns == PART1_WINNING_COLUMNS


def test_Card_initializes_correct_rows():
    assert card.rows == PART1_WINNING_ROWS
