import os


def cadena_a_matriz(cadena: str) -> list[list[str]]:
    filas = cadena.split('\n')
    matriz = [list(fila) for fila in filas]
    return matriz


def mostrar_matriz(matriz: list[list[str]]):
    os.system('cls' if os.name == 'nt' else 'clear')
    for fila in matriz:
        print("".join(fila))


def main_loop(mapa: list[list[str]], inicio: tuple[int, int], final: tuple[int, int]):
    px, py = inicio
    fx, fy = final
    mapa[px][py] = 'P'
    mapa[fx][fy] = '.'

    while (px, py) != (fx, fy):
        mostrar_matriz(mapa)
        movimiento = input('Mueve con las teclas (w: arriba, s: abajo, a: izquierda, d: derecha): ')

        nx, ny = px, py
        if movimiento == 'w':
            nx -= 1
        elif movimiento == 's':
            nx += 1
        elif movimiento == 'a':
            ny -= 1
        elif movimiento == 'd':
            ny += 1

        if 0 <= nx < len(mapa) and 0 <= ny < len(mapa[0]) and mapa[nx][ny] == '.':
            mapa[px][py] = '.'
            px, py = nx, ny
            mapa[px][py] = 'P'

    print('¡Has llegado al final del laberinto!')


if __name__ == '__main__':
    laberinto_cadena = '''...#...
                         ...#...
                         ...#...
                         ...#...
                         ...#...
                         ...#...
                         .......'''
    mapa = cadena_a_matriz(laberinto_cadena)
    inicio = (0, 0)
    final = (6, 6)
    main_loop(mapa, inicio, final)