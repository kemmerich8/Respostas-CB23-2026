import AP_03_ordenacao
import time
import random
import sys

sys.setrecursionlimit(10000)

random.seed(8)

tamanhos_N = [100,500,1000,5000]

def caso_medio(N):
    caso_m = random.sample(range(1,N*10),N)
    return caso_m 

def caso_pior(N):
    caso_p = list(range(N,0,-1))
    return caso_p

def tempo(lista_ordenada,funcao_geradora,N,K=50):
    n = time.perf_counter()
    for _ in range(K):
        lista_random = funcao_geradora(N)
        lista_ordenada(lista_random)
    m = time.perf_counter()
    diferenca = (m-n)/K
    return diferenca

for N in tamanhos_N:
    print(f"N = {N}")
    print()

    selection_medio = (tempo(AP_03_ordenacao.selection_sort,caso_medio,N))
    selection_pior = (tempo(AP_03_ordenacao.selection_sort,caso_pior,N))
    print(f"Selection sort | Caso médio:{selection_medio:.6f} | Pior caso: {selection_pior:.6f}")
    

    merge_medio = (tempo(AP_03_ordenacao.divide_and_conquer_sort,caso_medio,N))
    merge_pior = (tempo(AP_03_ordenacao.divide_and_conquer_sort,caso_pior,N))
    print(f"Merge sort     | Caso médio:{merge_medio:.6f} | Pior caso: {merge_pior:.6f}")
        

    quick_medio = tempo(AP_03_ordenacao.quick_sort,caso_medio,N)
    quick_pior = tempo(AP_03_ordenacao.quick_sort,caso_pior,N)
    print(f"Quick sort     | Caso médio:{quick_medio:.6f} | Pior caso: {quick_pior:.6f}")
    print("--------------------------------------------------------------------------")