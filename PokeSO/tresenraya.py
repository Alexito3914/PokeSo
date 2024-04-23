def imprimir_tablero(tablero):
    for fila in tablero:
        print("|".join(fila))
        print("-" * 5)
    jugador_actual = "X"

def verificar_ganador(tablero, jugador):
    # Verificar filas
    for fila in tablero:
        if all(cell == jugador for cell in fila):
            return True

    # Verificar columnas
    for i in range(3):
        if all(tablero[row][i] == jugador for row in range(3)):
            return True

    # Verificar diagonales
    if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2 - i] == jugador for i in range(3)):
        return True

    return False

def jugar_tres_en_raya():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador_actual = "X"

    while True:
        print(f"Turno del jugador {jugador_actual}")
        imprimir_tablero(tablero)
        fila = int(input("Ingrese el número de fila (1, 2, 3): "))
        columna = int(input("Ingrese el número de columna (1, 2, 3): "))

        fila -= 1  # Ajuste para que la entrada del usuario coincida con el índice del tablero
        columna -= 1  # Ajuste para que la entrada del usuario coincida con el índice del tablero

        if tablero[fila][columna] != " ":
            print("Esa casilla ya está ocupada. Inténtalo de nuevo.")
            continue

        tablero[fila][columna] = jugador_actual

        if verificar_ganador(tablero, jugador_actual):
            print(f"¡El jugador {jugador_actual} ha ganado!")
            break

        if all(tablero[i][j] != " " for i in range(3) for j in range(3)):
            print("¡Empate!")
            break

        jugador_actual = "O" if jugador_actual == "X" else "X"

jugar_tres_en_raya()