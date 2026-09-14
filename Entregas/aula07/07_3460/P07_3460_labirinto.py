import random
from collections import deque

def generate_maze_iterative(m, n, room=' ', wall='W', cheese='*'):
    maze = [[wall] * (2 * n + 1) for _ in range( 2 * m + 1)]# Cria a matriz cheia de paredes
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    stack = [(0, 0)] # Inicio da pilha

    maze[1][1] = room # primeira sala, (lógica 0,0-> matriz 1,1)

    while stack:
        x, y = stack[-1]# Pega a posição atual sem remover da pilha

        random.shuffle(directions)#Faz o labirinto ficar aleatório

        conseguiu_andar = False #Variável para saber se da para andar os se estamos em um beco sem saída

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < m and 0 <= ny < n and maze[2 * nx + 1][2 * ny + 1] == wall:#Verifica se esta dentro dos limites

                maze[2 * x + 1 + dx][2 * y + 1 + dy] = room#Vai da sala atual para a nova

                maze[2 * nx + 1][2 * ny + 1] = room#Marca a sala nova como visitada

                stack.append((nx,ny))

                conseguiu_andar = True
                break
        if not conseguiu_andar:
            stack.pop()

    while True: #Posiciona o queijo em um espaço aleatório
        i = random.randint(1, 2 * m - 1)
        j = random.randint(1, 2 * n - 1)

        if maze[i][j] == room:
            maze[i][j] = cheese
            break
    return maze


def solve_maze_bfs(maze, start=(1, 1), room=' ', wall='W', cheese='*'):
    #É o tamanho da matriz para não sair dos limites
    rows = len(maze)
    cols = len(maze[0])

    queue = deque([(start[0], start[1], [start])])#A fila vai guardar a linha a coluna e o caminho ate elas

    visited = set([start])#Guardar os lugares ja visitados

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r, c, path = queue.popleft()

        if maze[r][c] == cheese:#Caso ache o queijo
            return path
        
        for dr, dc in directions:#Se não achar o queijo, olhamos nas 4 direções
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols:#verificando os limites da matriz

                if maze[nr][nc] != wall and (nr, nc) not in visited:#Verifica se o espaço ao lado ja não foi visitado
                    visited.add((nr, nc))

                    queue.append((nr, nc, path + [(nr, nc)]))#Coloca o vizinho no final da fila para saber o caminho até ele

    return []

def print_solved_maze(maze, path, room=' ', cheese='*', wall='W', path_char='.'):
    solved_maze = [row[:] for row in maze]#Cópia do labirinto par anão estragar o original

    for r, c in path:#Marcação do caminho com '.'
        if solved_maze[r][c] not in (wall, cheese):
            solved_maze[r][c] = path_char

    for row in solved_maze:
        print(" ".join(map(str, row)))