from Analyzer import LexicalAnalyzer


string = '''
PARTIDOS “Real Madrid” TEMPORADA <1999-2000> -f archivo -ji 1 -jf 18
'''

# RESULTADO "Real Madrid" VS "Villarreal" TEMPORADA <2019-2020>
# RESULTADO "Levante" VS "Español" TEMPORADA <2017-2018>
# JORNADA 12 TEMPORADA <2019-2020>
# PARTIDOS "Real Madrid" TEMPORADA <1999-2000> -ji 1 -jf 18

#lexico = LexicalAnalyzer()

#lexico.analyzer(string)
#lexico.imprimirTokens()

a = 1
b = 'a'
c = 3

lista_ = [f'{a}{b}', c]
print(lista_)