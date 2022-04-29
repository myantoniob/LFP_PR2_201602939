import webbrowser as wb

class reportes():
    def __init__(self) -> None:
        self.head_file = '''
<!doctype html>
<html lang="en">
<head>    
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
<title>Mynor Ramirez - USAC</title>
</head>
<body>
<table class="table">
<thead>
<tr>
'''
        self.footer_file = '''
        
        </tbody>
        </table>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</body>
</html>
'''


#0                #1          #2           #3           #4          #5        #6
#Fecha,          Temporada,  Jornada,    Equipo1,      Equipo2,    Goles1,   Goles2
#08/09/1979,     1979-1980,  1,          Betis,Rayo    Vallecano,     1,         2


    def reporte_jornada(self, lista, file_nam):
        mid_file = f'''
        <th scope="col">#</th>
            <th scope="col">Temporada</th>
            <th scope="col">Jornada</th>
            <th scope="col">Equipo 1</th>
            <th scope="col">Equipo 2</th>
            <th scope="col">Goles 1</th>
            <th scope="col">Goles 2</th>
          </tr>
        </thead>
        <tbody>
          ''' 

        cont= 0
        for item in lista:
            mid_file += f'<tr> \n <th scope="row">{cont + 1}</th> \n'
            mid_file += f'<td>{item[1]}</td> \n'
            mid_file += f'<td>{item[2]}</td> \n'
            mid_file += f'<td>{item[3]}</td> \n'
            mid_file += f'<td>{item[4]}</td> \n'
            mid_file += f'<td>{item[5]}</td> \n'
            mid_file += f'<td>{item[6]}</td> \n </tr> \n'

            cont += 1

        completo = self.head_file + mid_file + self.footer_file
        self.generar_reporte(completo, file_nam)

    def reporte_tabla(self, sort_list, file_name):
        # lost_game, draw_game, won_game, points
        mid_file = f'''
        <th scope="col">#</th>
            <th scope="col">Name</th>
            <th scope="col">Lost Games</th>
            <th scope="col">Draw Games</th>
            <th scope="col">Won Games</th>
            <th scope="col">Points</th>
            
          </tr>
        </thead>
        <tbody>
          ''' 

        cont= 0
        for item in sort_list:
            mid_file += f'<tr> \n <th scope="row">{cont + 1}</th> \n'
            mid_file += f'<td>{item.name}</td> \n'
            mid_file += f'<td>{item.lost_game}</td> \n'
            mid_file += f'<td>{item.draw_game}</td> \n'
            mid_file += f'<td>{item.won_game}</td> \n'
            mid_file += f'<td>{item.points}</td> \n'

            cont += 1

        completo = self.head_file + mid_file + self.footer_file


        self.generar_reporte(completo, file_name)     



    def generar_partidos(self, sorted_jornada, file_name):
        mid_file = f'''
        <th scope="col">#</th>
            <th scope="col">Temporada</th>
            <th scope="col">Jornada</th>
            <th scope="col">Equipo 1</th>
            <th scope="col">Equipo 2</th>
            <th scope="col">Goles 1</th>
            <th scope="col">Goles 2</th>
          </tr>
        </thead>
        <tbody>
          '''  

        cont= 0
        for item in sorted_jornada:
            mid_file += f'<tr> \n <th scope="row">{cont + 1}</th> \n'
            mid_file += f'<td>{item[1]}</td> \n'
            mid_file += f'<td>{item[2]}</td> \n'
            mid_file += f'<td>{item[3]}</td> \n'
            mid_file += f'<td>{item[4]}</td> \n'
            mid_file += f'<td>{item[5]}</td> \n'
            mid_file += f'<td>{item[6]}</td> \n </tr> \n'

            cont += 1

        completo = self.head_file + mid_file + self.footer_file

        self.generar_reporte(completo, file_name)


    def generar_reporte(self, mensaje, file_nam):
        file = open(f'{file_nam}.html', 'w+')
        file.write(mensaje)
        file.close()
        wb.open(f'{file_nam}.html') 