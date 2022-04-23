class Token:

    def __init__(self, lexema:str, row:int, column:int, type:str) -> None:
        self.lexema = lexema
        self.row = row
        self.column = column
        self.type = type
        