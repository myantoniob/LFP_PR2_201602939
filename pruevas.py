
from Analyzer import LexicalAnalyzer
from Parser import Parser

# 1) RESULTADO "Real Madrid" VS "Villarreal" TEMPORADA <2019-2020>

# 2) JORNADA 12 TEMPORADA <2019-2020>
# 2.2) JORNADA 1 TEMPORADA <1996-1997> -f jornada1Reporte

# 3) GOLES LOCAL "Valencia" TEMPORADA <1998-1999>
# 3.1) GOLES VISITANTE "Valencia" TEMPORADA <1998-1999>
# 3.2) GOLES TOTAL "Valencia" TEMPORADA <1998-1999>

# 4) TABLA TEMPORADA <2018-2019>
# 4.1) TABLA TEMPORADA <1996-1997> -f reporteGlobal1

# 5) PARTIDOS "Real Madrid" TEMPORADA <1999-2000> -ji 1 -jf 18
# 5.1) PARTIDOS "Español" TEMPORADA <1999-2000> -f reporteEspanol
# 5.2) PARTIDOS "Real Madrid" TEMPORADA <1999-2000>  -jf 18 -f reporteEspanol

# 6) TOP SUPERIOR TEMPORADA <2000-2001>
# 6.1)  TOP INFERIOR TEMPORADA <1999-2000> -n 10

# 7) ADIOS


def request_element(string):
    #string = '''GOLES LOCAL "Valencia" TEMPORADA <1998-1999>'''

    lexico = LexicalAnalyzer()
    lexico.analyzer(string)
    #lexico.imprimirTokens()

    sintactico = Parser(lexico.tokenList)
    respuesta = sintactico.analyze()
    return respuesta
    #print(respuesta)



