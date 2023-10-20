import requests

def funcionPrincipal(file):
    ## Valores predeterminados para que python no se queje
    cc = 'prs_cc'
    mincc = 1
    maxcc = 12
    level = 'prs'

    ## Seleccionar la dificultad en la que se recorren las canciones
    selectDone = False
    dificultad = input("Introduzca la dificultad en la que quiere ordenar las canciones (pasado, presente, futuro o beyond): ")
    while selectDone == False:
        selectDone = True
        if dificultad == 'pasado':
            cc = 'pst_cc'
            maxcc = 7
            level = 'pst'
        elif dificultad == 'presente':
            mincc = 3.5
            maxcc = 9.5
        elif dificultad == 'futuro':
            cc = 'ftr_cc'
            mincc = 7
            maxcc = 11.3
            level = 'ftr'
        elif dificultad == 'beyond':
            cc = 'byd_cc'
            mincc = 9.5
            level = 'byd'
        else:
            dificultad = input("Input no reconocido, vuelva a introducurlo: ")
            selectDone = False
    todasLasCanciones(file, cc, mincc, maxcc, level)

def todasLasCanciones(file, cc, mincc, maxcc, level):
    ## Recorrer las canciones
    while mincc <= maxcc:
        i = 0
        for canciones in data['canciones']:
            if data['canciones'][i][cc] == mincc:
                cancion = data['canciones'][i]['nombre']
                pack = data['canciones'][i]['pack']
                coleccion = data['canciones'][i]['col']
                if coleccion == None: coleccion = 'Ninguna'
                nivel = data['canciones'][i][level]
                bando = data['canciones'][i]['lado']
                duracion = data['canciones'][i]['length']
                print ("Nombre: {0:43s} Pack: {1:22s} Colección: {2:20s} Dificultad: {3:3s} Bando: {4:9s} Duración: {5:7s}"
                    .format(cancion, pack, coleccion, nivel, bando, duracion))
            i = i+1
        if mincc < 8:
            mincc = mincc+0.5
        else: mincc = round(mincc+0.1, 1)

## Cojer el json de internet
try:
    file = requests.get('https://raw.githubusercontent.com/JavierEstudios/ritmo/main/canciones.json', timeout=1)
except:
    print("Error al coger los datos")
else:
    data = file.json()
    ## Llamar al resto del programa
    funcionPrincipal(file)
    file.close()