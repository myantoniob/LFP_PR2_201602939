import csv

file = open('laligabot.csv', 'r')
reader = csv.reader(file)

'''
#0                #1          #2           #3           #4          #5        #6
Fecha,          Temporada,  Jornada,    Equipo1,      Equipo2,    Goles1,   Goles2
08/09/1979,     1979-1980,  1,          Betis,Rayo    Vallecano,     1,         2
'''

class Equipo:
    def __init__(self, name, lost_game, won_game, draw_game, points) -> None:
        self.name = name 
        self.lost_game = lost_game
        self.won_game = won_game
        self.draw_game = draw_game
        self.points = points 


# --> 1
def game_resultado(team1, team2, time_frame_list):
    date = f'{time_frame_list[0]}-{time_frame_list[1]}'
    respuesta = ''
    for row in reader:
        if row[1] == date and row[3] == team1 and row[4] == team2:
            respuesta = f'El resultado de este partido fue: {team1} {row[5]} - {team2} {row[6]}' 

    print(respuesta)


# --> 2
def game_jornada(jornada, time_frame_list, lista):
    date = f'{time_frame_list[0]}-{time_frame_list[1]}'
    respuesta = ''
    lista = [] # Save it on the file
    for row in reader:
        if row[1] == date and row[2] == jornada:
            lista.append(row)
    
    respuesta = f'Generando archivo de resultados jornada {jornada} temporada {date}'
    print(respuesta)
    

# --> 3
def game_goles(goles_type, team, time_frame_list):
    date = f'{time_frame_list[0]}-{time_frame_list[1]}'
    goles = 0
    respuesta = ''

    if goles_type == 'LOCAL':
        for row in reader:
            if row[3] == team:
                goles += 1
        respuesta = f'Los goles anotados por el {team} como {goles_type} en la temporada {date} fueron {goles}'


    elif goles_type == 'VISITANTE':
        for row in reader:
            if row[4] == team:
                goles += 1
        respuesta = f'Los goles anotados por el {team} como {goles_type} en la temporada {date} fueron {goles}'


    elif goles_type == 'TOTAL':
        for row in reader:
            if row[3] == team or row[4] == team:
                goles += 1   
        respuesta = f'Los goles anotados por el {team} en {goles_type} en la temporada {date} fueron {goles}'
    
    print(respuesta)


# --> 4
def game_tabla(time_frame_list, lista_banderas):
    date = f'{time_frame_list[0]}-{time_frame_list[1]}'

    # all the season
    temporada = []

    for row in reader:
        if row[1] == date:
            temporada.append(row)
    
    # Each team
    dic_teams = {}

    for row in temporada:
        dic_teams[row[3]] = row[1]


    # Equipo p_perdidos p_ganados p_draw puntos
    lost_game = 0
    won_game = 0
    draw_game = 0
    points = 0

    for team in dic_teams:
        for row_t in temporada:
            #local
            if row_t[3] == team:
                if int(row_t[5]) > int(row_t[6]):
                    won_game += 1
                    points += 3
                elif int(row_t[5]) < int(row_t[6]):
                    lost_game += 1
                elif int(row_t[5]) == int(row_t[6]):
                    draw_game += 1
                    points += 1


            #Visitante
            elif row_t[4] == team:
                if int(row_t[5]) > int(row_t[6]):
                    lost_game += 1
                elif int(row_t[5]) < int(row_t[6]):
                    won_game += 1
                    points += 3
                elif int(row_t[5]) == int(row_t[6]):
                    draw_game += 1
                    points += 1

        # Equipo          p_perdidos  p_draw p_ganados puntos
        dic_teams[team] = [lost_game, draw_game, won_game, points]
        lost_game = 0
        won_game = 0
        draw_game = 0
        points = 0
    
    # Sort list
    sort_list = []

    for key in dic_teams:
        team = Equipo(key,dic_teams[key][0], dic_teams[key][1], dic_teams[key][2], dic_teams[key][3])
        sort_list.append(team)
   

    for i in range(len(sort_list)):
        for j in range(len(sort_list)-i -1 ):
            if sort_list[j].points < sort_list[j+1].points:
               temp = sort_list[j+1]
               sort_list[j+1] = sort_list[j]
               sort_list[j] = temp 
    

    respuesta = f'Generando archivo de clasificacion de temporada {date}'
    print(respuesta)


'''
#0                #1          #2           #3           #4          #5        #6
Fecha,          Temporada,  Jornada,    Equipo1,      Equipo2,    Goles1,   Goles2
08/09/1979,     1979-1980,  1,          Betis,Rayo    Vallecano,     1,         2
'''
#--> 5
def game_partidos(team, time_frame_list, lista_banderas):
    date = f'{time_frame_list[0]}-{time_frame_list[1]}'

    for item in lista_banderas:
        print(lista_banderas)

    respuesta = ''

    for row in reader:
        if row[1] == date:
            if row[3] == team or row[4] == team:
                pass   

# --> 6
def game_top(top_list, time_frame, lista_banderas):
    print('6-->',top_list, time_frame, lista_banderas)

# --> 7
def game_adios(adios):
    print('7-->',adios) 