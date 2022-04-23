from Token import Token
from Error import Error


class LexicalAnalyzer:

    def __init__(self) -> None:
        self.tokenList = []
        self.errorList = []
        self.line = 1
        self.column = 0
        self.buffer = ''
        self.state = 0
        self.i = 0 

    def add_token(self, character, row, column, description):
        self.tokenList.append(Token(character, row, column, description))
        self.buffer = ''

    def add_error(self, character, row, column):
        self.errorList.append(Error('Unknown character '+character+' for language', row, column))

    def s0(self, character:str):
        '''State S0'''
        #This is STATE 1
        if character.isupper():
            self.state = 1
            self.buffer += character
            self.column += 1

        # This is STATE 2
        elif character.islower():
            self.state = 2
            self.buffer += character
            self.column += 1

        # This is STATE 3
        elif character.isnumeric():
            self.state = 3
            self.buffer += character
            self.column += 1

        # This is STATE 4
        elif character == '"':
            self.state = 4
            self.buffer += character
            self.column += 1

        # This is STATE 5
        elif character == '<':
            self.state = 5
            self.buffer += character
            self.column += 1
        
        # This is STATE 6
        elif character == '>':
            self.state = 6
            self.buffer += character
            self.column += 1
        
        # This is STATE 7
        elif character == '-':
            self.state = 7
            self.buffer += character
            self.column += 1
        # Clear
        elif character == '\n':
            self.line +=1
            self.column = 0
        elif character == '\t':
            self.column += 5
        elif character == ' ':
            self.column += 1

        elif character == '$':
            pass
        else:
             self.add_error(character, self.line, self.column)

        
    def s1(self, character:str):
        '''State S1 '''

        if character.isupper():
            self.state = 1
            self.buffer += character
            self.column += 1
        elif self.buffer in ['RESULTADO', 'VS', 'TEMPORADA', 'JORNADA', 'GOLES', 'TOTAL', 'LOCAL', 'TABLA', 'PARTIDOS', 'TOP', 'SUPERIOR', 'INFERIOR', 'ADIOS']:
            self.add_token(self.buffer, self.line, self.column, 'reserved_'+self.buffer)
            self.state = 0
            self.i -= 1
        elif character.islower():
            self.state = 2
            self.buffer += character
            self.column += 1
