from Card import Card
from app.utils import separate_input


def part1(input: str) -> bool:
    numbers_string, card_string = separate_input(input)

    numbers = numbers_string.split(",")
    card = Card(card_string)

    result = card.playBingo(numbers)
    return type(result) == int
