# Atividade 07 - Busca em Grafos e Labirintos

## Questão 1: Geração de Labirinto (DFS Iterativo)
Para gerar o labirinto, a recursão original foi substituída por um **DFS Iterativo**. Foi usada uma Pilha (`stack`) nativa do Python em vez da pilha de chamadas de função. O comportamento de "ir o mais fundo possível" foi mantido iterando sobre as direções, quebrando a parede do vizinho válido, adicionando a nova sala à pilha e executando um `break` para que a próxima iteração explore esse novo caminho imediatamente. Caso o código chegue a um beco sem saída (sem vizinhos não visitados), o *backtracking* é executado removendo a sala atual do topo da pilha com `stack.pop()`.

## Questão 2: Resolução do Labirinto (BFS vs DFS)
Para encontrar o caminho da posição inicial até o queijo, foi implementada uma **Busca em Largura (BFS - Breadth-First Search)** utilizando uma Fila (`collections.deque`), em vez da Busca em Profundidade (DFS).

**Justificativa Técnica:**
Embora a DFS consuma menos memória, a BFS é uma estrutura mais eficiente para algoritmos de busca de caminho (pathfinding).
Como o algoritmo gerador cria um "labirinto perfeito" (uma árvore geradora, ou seja, sem ciclos ou espaços abertos), existe estritamente um único caminho entre a origem e o queijo. Desta forma, tanto DFS quanto BFS encontrariam o mesmo caminho. 
Contudo, se o labirinto sofresse modificações e passasse a ter múltiplos caminhos, a DFS, por seu comportamento de "mergulhar", poderia encontrar um trajeto muito mais longo do que o necessário. A BFS, por outro lado, expande sua busca "nível a nível", o que garante matematicamente sempre encontrar o caminho mais curto entre dois pontos de forma sistêmica; é como se fosse um balde de água que se espalha espaço por espaço e, quando entra em contato com o alvo (queijo), salva o caminho e o imprime.