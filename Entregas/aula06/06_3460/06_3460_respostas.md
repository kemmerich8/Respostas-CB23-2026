# Aula 06 - Análise de Complexidade 

## Justificativa da Complexidade Amortizada para `desenfileirar()`

A operação `desenfileirar()` pode custar $O(N)$ no pior caso em uma chamada isolada. Isso acontece exclusivamente quando a pilha de saída está vazia e há $N$ elementos acumulados na pilha de entrada, exigindo a transferência de todos os itens de uma pilha para a outra para inverter a ordem.

No entanto, o custo **amortizado** (caso médio por operação) é **$O(1)$**. 

Isso se justifica analisando o ciclo de vida completo de cada elemento inserido na fila:
1. **1x `push`** na pilha de entrada ao enfileirar ($O(1)$).
2. **1x `pop`** da pilha de entrada ao transferir ($O(1)$).
3. **1x `push`** na pilha de saída ao transferir ($O(1)$).
4. **1x `pop`** da pilha de saída ao desenfileirar ($O(1)$).

Cada elemento passa exatamente por **4 operações de custo constante ($O(1)$)** ao longo de toda a sua permanência na fila. Como esse trabalho é distribuído entre as operações de remoção, o custo por elemento permanece constante, garantindo complexidade amortizada **$O(1)$**.