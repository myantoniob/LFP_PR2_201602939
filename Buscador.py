import csv

file = open('laligabot.csv', 'r')
reader = csv.reader(file)

count = 0
for row in reader:

    if row[3] == 'Burgos':
        print(row[1], row[3], row[4])
    

    if count > 5:
        break

    count += 1
    
'''
Fecha,          Temporada,  Jornada,    Equipo1,      Equipo2,    Goles1,   Goles2
08/09/1979,     1979-1980,  1,          Betis,Rayo    Vallecano,     1,         2
'''