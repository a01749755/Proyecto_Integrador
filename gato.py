tablero = [
        [' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']
    ]

def visualizar_tablero(tablero):
    for linea in tablero:
        print(linea)
    pass

def checar_ganador(tablero):
    ganador = ' '
    if (tablero[0][0] == 'x' and tablero[0][1] == 'x' and tablero[0][2]== 'x'):
        ganador = 'x'
    else:
        if (tablero[1][0] == 'x' and tablero[1][1] == 'x' and tablero[1][2]== 'x'):
            ganador = 'x'
        else:
            if (tablero[2][0] == 'x' and tablero[2][1] == 'x' and tablero[2][2]== 'x'):
                ganador = 'x'
            else:
                if (tablero[0][0] == 'x' and tablero[1][1] == 'x' and tablero[2][2]== 'x'):
                    ganador = 'x'
                else:
                    if (tablero[0][2] == 'x' and tablero[1][1] == 'x' and tablero[2][0]== 'x'):
                        ganador = 'x'
                    else:
                        if (tablero[0][0] == 'x' and tablero[1][0] == 'x' and tablero[2][0]== 'x'):
                            ganador = 'x'
                        else:
                            if (tablero[0][1] == 'x' and tablero[1][1] == 'x' and tablero[2][1]== 'x'):
                                ganador = 'x'
                            else:
                                if (tablero[0][2] == 'x' and tablero[1][2] == 'x' and tablero[2][2]== 'x'):
                                    ganador = 'x'
                                else:
                                    if (tablero[0][0] == 'o' and tablero[0][1] == 'o' and tablero[0][2]== 'o'):
                                        ganador = 'o'
                                    else:
                                        if (tablero[1][0] == 'o' and tablero[1][1] == 'o' and tablero[1][2]== 'o'):
                                            ganador = 'o'
                                        else:
                                            if (tablero[2][0] == 'o' and tablero[2][1] == 'o' and tablero[2][2]== 'o'):
                                                ganador = 'o'
                                            else:
                                                if (tablero[0][0] == 'o' and tablero[1][1] == 'o' and tablero[2][2]== 'o'):
                                                    ganador = 'o'
                                                else:
                                                    if (tablero[0][2] == 'o' and tablero[1][1] == 'o' and tablero[2][0]== 'o'):
                                                        ganador = 'o'
                                                    else:
                                                        if (tablero[0][0] == 'o' and tablero[1][0] == 'o' and tablero[2][0]== 'o'):
                                                            ganador = 'o'
                                                        else:
                                                            if (tablero[0][1] == 'o' and tablero[1][1] == 'o' and tablero[2][1]== 'o'):
                                                                ganador = 'o'
                                                            else:
                                                                if (tablero[0][2] == 'o' and tablero[1][2] == 'o' and tablero[2][2]== 'o'):
                                                                    ganador = 'o'
    if ganador == 'x' or ganador == 'o':
        print(f'el ganador es {ganador}')
        return True
    else:
        print(f'aún no hay ganador')
        return False
        pass

def verificar_casilla(x, y):
            if (tablero[x][y] == ' '):
                return(True)
            else:
                return(False)
                pass

def verificar_lleno(x, y):
    for i in tablero:
        if (tablero[x][y] != ''):
            lleno = 'El espacio está lleno'
    return lleno
    pass

def pinta_casilla(tablero, x, y, tirador):
    if verificar_casilla(x, y) ==True:
        if tirador == 'x':
            tiro = tablero[x][y] = 'x'
            return tiro
        else:
            if tirador == 'o':
                tiro = tablero[x][y] = 'o'
                return tiro
        return tablero
        pass

def main():
    tirador = input('Quién eres? x/o: ')
    contador = 0
    while True:
        x = int(input('Escogue un renglón 0, 1, 2: '))
        y = int(input('Escogue la calumna 0, 1, 2: '))
        verificar_casilla(x,y)
        if(verificar_casilla(x,y)== True):
            contador += 1
            if contador%2 == 0:
                pinta_casilla(tablero, x, y, 'o')
                visualizar_tablero(tablero)
            else:
                pinta_casilla(tablero, x, y, 'x')
                visualizar_tablero(tablero)
        else: 
            if verificar_casilla(x,y) == False:
                print(verificar_lleno(x,y))
        if (checar_ganador(tablero) == True):
            break
    pass
main()
