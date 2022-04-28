from Token import Token
from Error import Error
from prettytable import PrettyTable


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
        #This is STATE 1, reserved words
        if character.isupper():
            self.state = 1
            self.buffer += character
            self.column += 1

        # This is STATE 2, hypertez
        elif character.islower():
            self.state = 2
            self.buffer += character
            self.column += 1

        # This is STATE 3, file name
        

        # This is STATE 4, numbers
        elif character.isnumeric():
            self.state = 4
            self.buffer += character
            self.column += 1

        # This is STATE 5
        elif character == '"':
            self.state = 5
            self.buffer += character
            self.column += 1

        # This is STATE 6
        elif character == '<':
            self.state = 6
            self.buffer += character
            self.column += 1
        
        # This is STATE 7
        elif character == '>':
            self.state = 7
            self.buffer += character
            self.column += 1
        
        # This is STATE 8
        elif character == '-':
            self.state = 8
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
        '''State S1,  Just reserved words'''

        if character.isupper():
            self.state = 1
            self.buffer += character
            self.column += 1

        elif self.buffer in ['RESULTADO', 'VS', 'TEMPORADA', 'JORNADA', 'GOLES', 'TOTAL', 'LOCAL', 'VISITANTE', 'TABLA', 'PARTIDOS', 'TOP', 'SUPERIOR', 'INFERIOR', 'ADIOS']:
            self.add_token(self.buffer, self.line, self.column, 'reserved_'+self.buffer)
            self.state = 0
            self.i -= 1
            
        # --> 2
        elif character.islower() or character == ' ':
            self.state = 2
            self.buffer += character
            self.column += 1
        # --> 3
        elif character.isnumeric() or character == '_':
            self.state = 3
            self.buffer += character
            self.column += 1

        

    def s2(self, character:str):
        '''State S2, Just team names'''
        if character.islower():
            self.state = 2
            self.buffer += character
            self.column += 1

        elif character.isupper():
            self.state = 2
            self.buffer += character
            self.column += 1

        elif character == ' ':
            if self.buffer in ['f', 'ji', 'jf', 'n']:
                self.add_token(self.buffer, self.line, self.column, 'reserved_'+self.buffer)
                self.state = 0
                self.i -= 1
            else:
                self.state = 2
                self.buffer += character
                self.column += 1
        # --> 3
        elif character.isnumeric() or character == '_':
            self.state = 3
            self.buffer += character
            self.column += 1

        else: 
            self.add_token(self.buffer, self.line, self.column, 'hypertext')
            self.state = 0
            self.i -= 1

    def s3(self, character:str):
        '''State S3, Just file names'''

        if character.isupper():
            self.state = 3
            self.buffer += character
            self.column += 1
        elif character.islower():
            self.state = 3
            self.buffer += character
            self.column += 1
        elif character.isnumeric():
            self.state = 3
            self.buffer += character
            self.column += 1
        elif character == '_':
            self.state = 3
            self.buffer += character
            self.column += 1
        else: 
            self.add_token(self.buffer, self.line, self.column, 'filename')
            self.state = 0
            self.i -= 1

    def s4(self, character:str):
        '''State S4, Just numbers'''

        if character.isnumeric():
            self.state = 4
            self.buffer += character
            self.column += 1
        else: 
            self.add_token(self.buffer, self.line, self.column, 'numeric')
            self.state = 0
            self.i -= 1
    def s5(self, character:str):
        '''S5, doubleQuote'''
        self.add_token(self.buffer, self.line, self.column, 'doubleQuote')
        self.state = 0
        self.i -= 1

    def s6(self, character:str):
        '''State S6'''
        self.add_token(self.buffer, self.line, self.column, 'leftAngle')
        self.state = 0
        self.i -= 1

    def s7(self, character:str):
        '''State S7'''
        self.add_token(self.buffer, self.line, self.column, 'rightAngle')
        self.state = 0
        self.i -= 1

    def s8(self, character:str):
        '''State S8 '''
        self.add_token(self.buffer, self.line, self.column, 'hyphen')
        self.state = 0
        self.i -= 1


    def analyzer(self, string):
        self.texto_modal = string
        string = string + '$'
        self.tokenList = []
        self.errorList = []
        self.i = 0

        while self.i < len(string):
            if self.state == 0:
                self.s0(string[self.i])
            elif self.state == 1:
                self.s1(string[self.i])
            elif self.state == 2:
                self.s2(string[self.i])
            elif self.state == 3:
                self.s3(string[self.i])
            elif self.state == 4:
                self.s4(string[self.i])
            elif self.state == 5:
                self.s5(string[self.i])
            elif self.state == 6:
                self.s6(string[self.i])
            elif self.state == 7:
                self.s7(string[self.i])
            elif self.state == 8:
                self.s8(string[self.i])

            self.i += 1


    def imprimirTokens(self):
        '''Imprimir una tabla con los tokens'''
        x = PrettyTable()
        x.field_names = ["Lexema", "linea", "columna", "tipo"]
        for token in self.tokenList:
            x.add_row([token.lexema, token.row, token.column, token.type])
        print(x)

