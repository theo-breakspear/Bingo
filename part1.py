from Card import Card


def part1(input: str) -> bool:
    numbers_string, card_string = input.split("\n\n")

    numbers = numbers_string.split(",")
    card = Card(card_string)

    result = card.playBingo(numbers)
    return type(result) == int
