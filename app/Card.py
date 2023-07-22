from typing import List


class Card:
    def __init__(self, card_string: str):
        self.rows = [line.split(" ") for line in card_string.split("\n")]
        self.columns = self._initialize_columns(self.rows)

    def _initialize_columns(self, rows: List[List[str]]):
        columns = []
        for i in range(len(rows)):
            columns.append([row[i] for row in rows])
        return columns

    def play_bingo(self, numbers: List[str]) -> int or None:
        rows = self.rows
        columns = self.columns
        call_count = 0
        for number in numbers:
            for row in rows:
                if number in row:
                    row.pop(row.index(number))
            for column in columns:
                if number in column:
                    column.pop(column.index(number))
            call_count += 1
            for row in rows:
                if not row:
                    return call_count
            for column in columns:
                if not column:
                    return call_count
        return float("inf")
