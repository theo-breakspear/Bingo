from Card import Card
from utils import separate_input


def part2(input: str) -> bool:
    numbers_string, card1_string, card2_string, card3_string = separate_input(input)

    numbers = numbers_string.split(",")
    card1 = Card(card1_string)
    card2 = Card(card2_string)
    card3 = Card(card3_string)

    result1 = card1.play_bingo(numbers)
    result2 = card2.play_bingo(numbers)
    result3 = card3.play_bingo(numbers)

    smallest_result = min(result1, result2, result3)

    if smallest_result == result1 == result2 == result3:
        return "All cards draw"
    if smallest_result == result1 == result2:
        return "Cards 1 and 2 draw"
    if smallest_result == result2 == result3:
        return "Cards 2 and 3 draw"
    if smallest_result == result1 == result3:
        return "Cards 1 and 3 draw"
    if smallest_result == result1:
        return "Card 1 wins"
    if smallest_result == result2:
        return "Card 2 wins"
    else:
        return "Card 3 wins"
