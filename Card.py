class Card:
    def __init__(self, card_string):
        self.rows = [line.split(" ") for line in card_string.split("\n")]
        self.columns = self._initialize_columns(self.rows)

    def _initialize_columns(self, rows):
        columns = []
        for i in range(len(rows)):
            columns.append([row[i] for row in rows])
        return columns
