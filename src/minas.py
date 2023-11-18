import random

def iniciar_tablero(filas, columnas, num_minas):
    """
    Inicializa el tablero del juego con minas y números de minas adyacentes.

    Parametros:
    - filas (int): Número de filas del tablero.
    - columnas (int): Número de columnas del tablero.
    - num_minas (int): Número de minas a colocar en el tablero.

    Retorna:
    - tupla: Matriz que representa el tablero del juego y conjunto de posiciones de las minas.
    """
    tablero = [[' ' for x in range(columnas)] for x in range(filas)]
    minas = set()

    while len(minas) < num_minas:
        fila, columna = random.randint(0, filas - 1), random.randint(0, columnas - 1)
        minas.add((fila, columna))
        tablero[fila][columna] = '*'

    for fila in range(filas):
        for columna in range(columnas):
            if  tablero[fila][columna] != '*':
                minas_adyacentes = sum(
                    1 for i in range(-1, 2) for j in range(-1, 2)
                    if 0 <= fila + i < filas and 0 <= columna + j < columnas and tablero[fila + i][columna + j] == '*'
                )
                
                tablero[fila][columna] = str(minas_adyacentes) if minas_adyacentes > 0 else '0'
    
    return tablero, minas

def imprimir_tablero(tablero, celdas_reveladas, celdas_marcadas):
    print("   " + " ".join(str(i) for i in range(1, len(tablero[0])+ 1)))
    for i, fila in enumerate(tablero, start = 1):
        print(f"{i} " + " ".join(('M' if (i - 1, j) in celdas_marcadas else celda) if (i - 1, j) in celdas_reveladas or (i - 1, j) in celdas_marcadas else '.' for j, celda in enumerate(fila)))

def revelar_celda(fila, columna, tablero, celdas_reveladas, celdas_marcadas, minas):
    """
    Revela una celda en el tablero y maneja las consecuencias del movimiento.

    Parametros:
    - fila (int): Fila de la celda a revelar.
    - columna (int): Columna de la celda a revelar.
    - tablero (list): Matriz que representa el tablero del juego.
    - celdas_reveladas (set): Conjunto de celdas que han sido reveladas.
    - celdas_marcadas (set): Conjunto de celdas que han sido marcadas como posibles minas.
    - minas (set): Conjunto de posiciones de las minas en el tablero.

    Retorna:
    - bool: True si se revela una mina, False de lo contrario.
    """
    if (fila - 1, columna - 1) in celdas_reveladas or (fila - 1, columna - 1) in celdas_marcadas:
        print*("Ya has revelado/marcado esta celda")
        return False
    
    elif tablero[fila- 1][columna - 1] == '*':
        print("Boom! Has golpeado una mina. Fin del juego")
        mostrar_minas(tablero, minas, celdas_marcadas)
        return True
    
    else:
        revelar_celdas_vacias(fila - 1, columna - 1, tablero, celdas_reveladas)
        return False

def marcar_celda(fila, columna, celdas_marcadas):
    """
    Marca o desmarca una celda como posible mina.

    Parametros:
    - fila (int): Fila de la celda a marcar/desmarcar.
    - columna (int): Columna de la celda a marcar/desmarcar.
    - celdas_marcadas (set): Conjunto de celdas que han sido marcadas como posibles minas.
    """
    celda = (fila - 1, columna - 1)
    if celda in celdas_marcadas:
        celdas_marcadas.remove(celda)
        print(f"Celda ({fila}, {columna}) desmarcada")
    else:
        celdas_marcadas.add(celda)
        print(f"Celda ({fila}, {columna}) marcada como posible mina (M)")

def verificar_victoria(tablero, celdas_reveladas, minas):
    """
    Verifica si todas las celdas sin minas han sido reveladas, lo que indica una victoria.

    Parametros:
    - tablero (list): Matriz que representa el tablero del juego.
    - celdas_reveladas (set): Conjunto de celdas que han sido reveladas.
    - minas (set): Conjunto de posiciones de las minas en el tablero.

    Retorna:
    - bool: True si todas las celdas sin minas han sido reveladas, False de lo contrario.
    """
    celdas_sin_minas = {(i, j) for i in range(len(tablero)) for j in range(len(tablero[0]))} - set(minas)
    return celdas_reveladas == celdas_sin_minas

def revelar_celdas_vacias(fila, columna, tablero, celdas_reveladas):
    """
    Revela todas las celdas vacías adyacentes a la celda dada.

    Parametros:
    - fila (int): Fila de la celda a revelar.
    - columna (int): Columna de la celda a revelar.
    - tablero (list): Matriz que representa el tablero del juego.
    - celdas_reveladas (set): Conjunto de celdas que han sido reveladas.
    """
    if 0 <= fila < len(tablero) and 0 <= columna < len(tablero[0]) and (fila, columna) not in celdas_reveladas:
        celdas_reveladas.add((fila, columna))
        if tablero[fila][columna] == '0':
            for i in range(-1, 2):
                for j in range(-1, 2):
                    revelar_celdas_vacias(fila + i, columna + j, tablero, celdas_reveladas)

def mostrar_minas(tablero, minas, celdas_marcadas):
    for fila, columna in minas:
        tablero[fila][columna] = '*' if (fila, columna) not in celdas_marcadas else 'M'
    imprimir_tablero(tablero, set(minas), celdas_marcadas)
def jugar():
    filas, columnas, num_minas = 8, 8, 10
    tablero, minas = iniciar_tablero(filas, columnas, num_minas)
    celdas_reveladas, celdas_marcadas = set(), set()
    juego_terminado = False

    while not juego_terminado:
        imprimir_tablero(tablero, celdas_reveladas, celdas_marcadas)
        print("\nElige una accion:")
        print("1. Revelar celda")
        print("2. Marcar celda")
        print("3. Salir del juego")

        eleccion = input("Elige una opcion: ")

        if eleccion == '1':
            try:
                fila, columna = map(int, input("Ingresa la fila y la columna (Separadas por un espacio): ").split())
                juego_terminado = revelar_celda(fila, columna, tablero, celdas_reveladas, celdas_marcadas, minas)
            except ValueError:
                print("Entrada invalida, Ingresa 2 numeros separados por un espacio")
        
        elif eleccion == '2':
            try:
                fila, columna = map(int, input("Ingresa la fila y la columna (Separadas por un espacio): ").split())
                marcar_celda(fila, columna, celdas_marcadas)
            except ValueError:
                print("Entrada invalida, Ingresa 2 numeros separados por un espacio")
        
        elif eleccion == '3':
            juego_terminado = True

        juego_terminado = juego_terminado or verificar_victoria(tablero, celdas_reveladas, minas)

    if verificar_victoria(tablero, celdas_reveladas, minas):
        print("Felicidades Has ganado!")

if __name__ == "__main__":
    jugar()