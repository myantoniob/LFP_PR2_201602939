
from Error import ErrorParser
from Boot import *
class Parser:

    def __init__(self, tokens: list) -> None:
        self.errores = [] 
        self.tokens = tokens

    def addError(self, expected, given):
        self.errores.append(f'ERROR SINTÁCTICO: se obtuvo {given} se esperaba {expected}')

    def popToken(self):

        try:
            return self.tokens.pop(0)
        except:
            return None

    def scanToken(self):
        try: 
            return self.tokens[0]
        except:
            return None

    def analyze(self):
        self.S()
    
    def S(self):
        self.INICIO()

    def INICIO(self):

        temporal = self.scanToken()

        if temporal is None:
            self.addError('RESULTADO | JORNADA | GOLES | TABLA | PARTIDOS | TOP | ADIOS', 'None')
        elif temporal.type == 'reserved_RESULTADO':
            self.GAMERESULTADO() 
        elif temporal.type == 'reserved_JORNADA':
            self.GAMEJORNADA()
        elif temporal.type == 'reserved_GOLES':
            self.GAMEGOLES()
        elif temporal.type == 'reserved_TABLA':
            self.GAMETABLA()
        elif temporal.type == 'reserved_PARTIDOS':
            self.GAMEPARTIDOS()
        elif temporal.type == 'reserved_TOP':
            self.GAMETOP()   
        elif temporal.type == 'reserved_ADIOS':
            self.GAMEADIOS()
        else:
            self.addError('RESULTADO | JORNADA | GOLES | TABLA | PARTIDOS | TOP | ADIOS', temporal.type)  
            
    def GAMERESULTADO(self):
        '''reserved_RESULTADO hypertext reserved_VS hypertext 
        reserved_TEMPORADA  leftAngle numeric hyphen numeric rightAngle '''
        team1 = ''
        team2 = ''
        date1 = 0
        date2 = 0

        token = self.popToken()
        if token.type == 'reserved_RESULTADO':

            token = self.popToken()
            if token is None:
                self.addError('hypertext', 'None')
                return

            elif token.tye == 'hypertext':
                team1 = token.lexema
                token = self.popToken()

                if token is None:
                    self.addError('reserved_VS', 'None')
                    return
                elif token.type == 'reserved_VS':
                    token = self.popToken()

                    if token is None:
                        self.addError('hypertext', 'None')
                        return
                    elif token.type == 'hypertext':
                        team2 = token.lexema
                        token = self.popToken()

                        if token is None:
                            self.addError('reserved_TEMPORADA', 'None')
                            return

                        elif token.type == 'reserved_TEMPORADA':
                            token = self.popToken()

                            if token is None:
                                self.addError('leftAngle', 'None')
                                return
                            elif token.type == 'leftAngle':
                                token = self.popToken()

                                if token is None:
                                    self.addError('numeric', 'None')
                                    return 
                                elif token.type == 'numeric':
                                    date1 = token.lexema

                                    token = self.popToken()

                                    if token is None:
                                        self.addError('hyphen', 'None')
                                        return
                                    elif token.type == 'hyphen':
                                        token = self.popToken()

                                        if token is None:
                                            self.addError('numeric', 'None')
                                            return
                                        elif token.type == 'numeric':
                                            date2 = token.lexema

                                            token = self.popToken()
                                            if token is None:
                                                self.addError('rightAngle', 'None')
                                                return
                                            elif token.type == 'rightAngle':
                                                # Final step
                                                game_resultado(team1, team2, date1, date2)
                                            else: 
                                                self.addError('rightAngle', token.type)
                                        else: 
                                            self.addError('numeric', token.type)


                                    else:
                                        self.addError('hyphen', token.type)
                                    
                                else:
                                    self.addError('numeric', token.type) 

                            else:
                                self.addError('leftAngle', token.type)  
                        else:
                            self.addError('reserved_TEMPORADA', token.type)
                    else:
                        self.addError('hypertext', token.type)

                else:
                    self.addError('reserved_VS', token.type)

            else:
                self.addError('hypertext', token.type)


        else: 
            self.addError('reserved_RESULTADO', token.type)




    def GAMEJORNADA(self):
        '''GAMEJORNADA ::= reserved_JORNADA numeric reserved_TEMPORADA leftAngle 
        numeric hyphen numeric rightAngle LISTABANDERAS'''

        token = self.popToken()
        if token.type == 'reserved_JORNADA':


            token = self.popToken()
            if token is None:
                self.addError('numeric', 'None')
                return
            elif token.type == 'numeric':
                

                token = self.popToken()
                if token is None:
                    self.addError('reserved_TEMPORADA', 'None')
                    return
                elif token.type == 'reserved_TEMPORADA':
                    

                    token = self.popToken()
                    if token is None:
                        self.addError('leftAngle', 'None')
                        return
                    elif token.type == 'leftAngle':
                        

                        token = self.popToken()
                        if token is None:
                            self.addError('numeric', 'None')
                            return
                        elif token.type == 'numeric':
                            

                            token = self.popToken()
                            if token is None:
                                self.addError('hyphen', 'None')
                                return
                            elif token.type == 'hyphen':
                                

                                token = self.popToken()
                                if token is None:
                                    self.addError('numeric', 'None')
                                    return
                                elif token.type == 'numeric':
                                    

                                    token = self.popToken()
                                    if token is None:
                                        self.addError('rightAngle', 'None')
                                        return
                                    elif token.type == 'rightAngle':
                                        

                                        lista = self.LISTABANDERAS()

                                        '''if lista is None:
                                            return

                                        if token is None:
                                            self.addError('#', 'None')
                                            return
                                        elif token.type == '#':
                                            pass
                                        else:
                                            self.addError('#', token.type)'''


                                    else:
                                        self.addError('#', token.type)


                                else:
                                    self.addError('#', token.type)


                            else:
                                self.addError('#', token.type)


                        else:
                            self.addError('#', token.type)


                    else:
                        self.addError('#', token.type)


                else:
                    self.addError('#', token.type)


            else:
                self.addError('#', token.type) 
        else:
            self.addError('reserved_JORNADA', token.type)



    def GAMEGOLES(self):
        token = self.popToken()



    def GAMETABLA(self):
        token = self.popToken()



    def GAMEPARTIDOS(self):
        token = self.popToken()



    def GAMETOP(self):
        token = self.popToken()



    def GAMEADIOS(self):
        token = self.popToken() 

# <------------------------------------------------->

# <------------------------------------------------->

    def LISTABANDERAS(self):

        bandera_unica = self.BANDERAUNICA()

        lista_banderas_ = self.LISTABANDERAS_()
        return [bandera_unica] + [lista_banderas_]

    def LISTABANDERAS_(self):
        token = self.scanToken()

        if token is None:
            return []
        elif token.type == 'hyphen':
            bandera_unica = self.BANDERAUNICA()
            lista_banderas_ = self.LISTABANDERAS_()
            return [bandera_unica] + [lista_banderas_]
        else: 
            return []


    def BANDERAUNICA(self):
        token = self.scanToken()

        if token is None:
            return []
        
        if token.type == 'hyphen':
            token = self.popToken()

            bandera = self.BANDERA()
            tipo = self.TIPO()
            return [f'{token.lexema}{bandera}', tipo]
        else: 
            return []  

    def BANDERA(self):
        token = self.popToken()

        if token is None:
            self.addError('reserved_f | reserved_ji | reserved_jf | reserved_n', 'None')
            return
        if token.type == 'reserved_f':
            return token.lexema
        elif token.type == 'reserved_ji':
            return token.lexema
        elif token.type == 'reserved_jf':
            return token.lexema
        elif token.type == 'reserved_n':
            return token.lexema
        else:
            self.addError('reserved_f | reserved_ji | reserved_jf | reserved_n', token.type)
            

    def TIPO(self):
        token = self.popToken()

        if token is None:
            self.addError('filename | numeric', 'None')
            return
        if token.type == 'filename':
            return token.lexema
        elif token.type == 'numeric':
            return int(token.lexema)
        else:
            self.addError('filename | numeric', token.type)