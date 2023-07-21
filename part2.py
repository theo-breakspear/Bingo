from Card import Card


def part2(input: str) -> bool:
    numbers_string, card1_string, card2_string, card3_string = input.split("\n\n")

    numbers = numbers_string.split(",")
    card1 = Card(card1_string)
    card2 = Card(card2_string)
    card3 = Card(card3_string)

    result1 = card1.playBingo(numbers)
    result2 = card2.playBingo(numbers)
    result3 = card3.playBingo(numbers)

    smallest_result = min(result1, result2, result3)

    if result1 == result2 == result3:
        return "Draw"
    if smallest_result == result1:
        return "card1"
    elif smallest_result == result2:
        return "card2"
    else:
        return "card3"
