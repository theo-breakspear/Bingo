# separate numbers and card
# extract card columns and rows
# for each number check each row and column and remove number if exists
# check if any empty rows or columns

from Card import Card


input = "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1\n\n22 13 17 11 0\n8 2 23 4 24\n21 9 14 16 7\n6 10 3 18 5\n1 12 20 15 19"

numbers_string, card_string = input.split("\n\n")

numbers = numbers_string.split(",")

card = Card(card_string)

print(card.rows)
print(card.columns)
