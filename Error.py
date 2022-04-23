class Error:

    def __init__(self, description, row, column) -> None:
        self.description = description
        self.row = row
        self.column = column

        