class Error:

    def __init__(self, description, row, column) -> None:
        self.description = description
        self.row = row
        self.column = column

class ErrorParser:
    def __init__(self, description, expected, given) -> None:
        self.description = description
        self.expected = expected
        self.given = given        