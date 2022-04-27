
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
    
    def DOUBLEQUOTE(self):
        token = self.popToken()
        if token is None:
            self.addError('doubleQuote', 'None')
            return
        elif token.type == 'doubleQuote':
            return token.lexema
        else:
            self.addError('doubleQuote', token.type)


    def GAMERESULTADO(self):
        '''1) GAMERESULTADO ::= reserved_RESULTADO hypertext reserved_VS hypertext 
        reserved_TEMPORADA  TIMEFRAME'''
        team1 = ''
        team2 = ''

        token = self.popToken()
        if token.type == 'reserved_RESULTADO':

            token = self.popToken()
            if token is None:
                self.addError('doubleQuote', 'None')
                return
            elif token.type == 'doubleQuote':

                token = self.popToken()
                if token is None:
                    self.addError('hypertext', 'None')
                    return

                elif token.type == 'hypertext':
                    team1 = token.lexema

                    quote = self.DOUBLEQUOTE()
                    if quote is None:
                        return

                    token = self.popToken()

                    if token is None:
                        self.addError('reserved_VS', 'None')
                        return
                    elif token.type == 'reserved_VS':

                        quote = self.DOUBLEQUOTE()
                        if quote is None:
                            return


                        token = self.popToken()

                        if token is None:
                            self.addError('hypertext', 'None')
                            return
                        elif token.type == 'hypertext':
                            team2 = token.lexema

                            quote = self.DOUBLEQUOTE()
                            if quote is None:
                                return


                            token = self.popToken()

                            if token is None:
                                self.addError('reserved_TEMPORADA', 'None')
                                return

                            elif token.type == 'reserved_TEMPORADA':


                                time_frame_list = self.TIMEFRAME()
                                if time_frame_list is None:
                                    return

                                game_resultado(team1, team2, time_frame_list)

                            else:
                                self.addError('reserved_TEMPORADA', token.type)
                        else:
                            self.addError('hypertext', token.type)

                    else:
                        self.addError('reserved_VS', token.type)

                else:
                    self.addError('hypertext', token.type)
            else:
                self.addError('doubleQuote', token.type)

        else: 
            self.addError('reserved_RESULTADO', token.type)




    def GAMEJORNADA(self):
        '''2) GAMEJORNADA ::= reserved_JORNADA numeric reserved_TEMPORADA 
            TIMEFRAME LISTABANDERAS '''
        jornada = 0
        date1 = 0
        date2 = 0
        token = self.popToken()
        if token.type == 'reserved_JORNADA':


            token = self.popToken()
            if token is None:
                self.addError('numeric', 'None')
                return
            elif token.type == 'numeric':
                jornada = token.lexema

                token = self.popToken()
                if token is None:
                    self.addError('reserved_TEMPORADA', 'None')
                    return
                elif token.type == 'reserved_TEMPORADA':
                    
                    time_frame_list = self.TIMEFRAME()
                    if time_frame_list is None:
                        return

                    lista_banderas = self.LISTABANDERAS()
                    if lista_banderas is None:
                        return

                    game_jornada(jornada, time_frame_list, lista_banderas)

                else:
                    self.addError('reserved_TEMPORADA', token.type)


            else:
                self.addError('numeric', token.type) 
        else:
            self.addError('reserved_JORNADA', token.type)



    def GAMEGOLES(self):
        '''3) GAMEGOLES ::= reserved_GOLES GOLESLIST hypertext 
                reserved_TEMPORADA TIMEFRAME'''
        team = ''
        token = self.popToken()

        if token.type == 'reserved_GOLES':

            goles_type = self.GOLESLIST() 

            if goles_type is None:
                return
            
            quote = self.DOUBLEQUOTE()
            if quote is None:
                return

            token = self.popToken()
            if token is None:
                self.addError('hypertext', 'None')
                return
            elif token.type == 'hypertext':
                team = token.lexema

                quote = self.DOUBLEQUOTE()
                if quote is None:
                    return

                token = self.popToken()
                if token is None:
                    self.addError('reserved_TEMPORADA', 'None')
                    return
                elif token.type == 'reserved_TEMPORADA':

                    time_frame_list = self.TIMEFRAME()
                    if time_frame_list is None:
                        return

                    game_goles(goles_type, team, time_frame_list)

                else:
                    self.addError('reserved_TEMPORADA', token.type)


            else:
                self.addError('hypertext', token.type) 

                
        else:
            self.addError('reserved_GOLES', token.type)

    def GOLESLIST(self):
        token = self.popToken()

        if token is None:
            self.addError('reserved_TOTAL | reserved_LOCAL | reserved_VISITANTE','None')
            return
        
        elif token.type == 'reserved_TOTAL':
            return token.lexema
        elif token.type == 'reserved_LOCAL':
            return token.lexema
        elif token.type == 'reserved_VISITANTE':
            return token.lexema
        else:
            self.addError('reserved_TOTAL | reserved_LOCAL | reserved_VISITANTE', token.type)


    def GAMETABLA(self):
        '''4) GAMETABLA ::= reserved_TABLA reserved_TEMPORADA 
        TIMEFRAME LISTABANDERAS'''

        token = self.popToken()
        if token.type == 'reserved_TABLA':
            

            token = self.popToken()
            if token is None:
                self.addError('reserved_TEMPORADA', 'None')
                return
            elif token.type == 'reserved_TEMPORADA':
                

                time_frame_list = self.TIMEFRAME()
                if time_frame_list is None:
                    return
                lista_banderas = self.LISTABANDERAS()
                if lista_banderas is None:
                    return

                game_tabla(time_frame_list, lista_banderas)
            else:
                self.addError('reserved_TEMPORADA', token.type)


        else:
            self.addError('reserved_TABLA', token.type) 




    def GAMEPARTIDOS(self):
        '''5) GAMEPARTIDOS ::= reserved_PARTIDOS DOUBLEQUOTE hypertext DOUBLEQUOTE 
        reserved_TEMPORADA TIMEFRAME LISTABANDERAS'''

        team = ''
        token = self.popToken()

        if token.type == 'reserved_PARTIDOS':
            
            quote = self.DOUBLEQUOTE()
            if quote is None:
                return

            token = self.popToken()
            if token is None:
                self.addError('hypertext', 'None')
            elif token.type == 'hypertext':
                team = token.lexema

                quote = self.DOUBLEQUOTE()
                if quote is None:
                    return    

                token = self.popToken()
                if token is None:
                    self.addError('reserved_TEMPORADA', 'None')
                    return
                elif token.type == 'reserved_TEMPORADA':
                    

                    time_frame_list = self.TIMEFRAME()
                    if time_frame_list is None:
                        return
                    
                    lista_banderas = self.LISTABANDERAS()
                    if lista_banderas is None:
                        return

                    game_partidos(team, time_frame_list, lista_banderas)

                else:
                    self.addError('reserved_TEMPORADA', token.type)


            else:
                self.addError('hypertext', token.type)


        else:
            self.addError('reserved_PARTIDOS', token.type) 



    def GAMETOP(self):
        '''6) GAMETOP ::= reserved_TOP TOPLIST reserved_TEMPORADA 
                TIMEFRAME LISTABANDERAS'''

        token = self.popToken()
        if token.type == 'reserved_TOP':

            top_list = self.TOPLIST()
            if top_list is None:
                return

            token = self.popToken()
            if token is None:
                self.addError('reserved_TEMPORADA', 'None')
                return
            elif token.type == 'reserved_TEMPORADA':
                
                time_frame = self.TIMEFRAME()
                if time_frame is None:
                    return
                
                lista_banderas = self.LISTABANDERAS()
                if lista_banderas is None:
                    return

                game_top(top_list, time_frame, lista_banderas)

            else:
                self.addError('reserved_TEMPORADA', token.type) 
            
        else:
            self.addError('reserved_TOP', token.type)



    def GAMEADIOS(self):
        '''7) GAMEADIOS = reserved_ADIOS'''

        token = self.popToken()

        if token.type == 'reserved_ADIOS':
            game_adios(token.lexema)
        else:
            self.addError('reserved_ADIOS', token.type)  

# <------------------------------------------------->
    def TIMEFRAME(self):
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
                            return [date1, date2]
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

    def TOPLIST(self):
        token = self.popToken()

        if token is None:
            self.addError('reserved_SUPERIOR | reserved_INFERIOR', 'None')
            return

        if token.type == 'reserved_SUPERIOR':
            return token.lexema
        elif token.type == 'reserved_INFERIOR':
            return token.lexema
        else:
            self.addError('reserved_SUPERIOR | reserved_INFERIOR', token.type)
