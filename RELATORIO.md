# Relatório — Nícolas Kemmerich (3460)
## Marco 1

### Ambiente

No Windows, o comando `where.exe python` retornou:
- `C:\Users\nicol\AppData\Local\Microsoft\WindowsApps\python.exe`
- `C:\Users\nicol\AppData\Local\Python\bin\python.exe`

O executável utilizado (`sys.executable`) foi `C:\Users\nicol\AppData\Local\Python\pythoncore-3.14-64\python.exe`.

Etapa 0: Python 3.14.3, NumPy 2.5.3 e fornecido 3.0. Todas as verificações iniciais do NumPy passaram.

### R1 — Expressões regulares

`re.match` verifica, desde o começo da string, se há alguma correspondência ao formato exigido, mas isso não implica que o restante da entrada também esteja correto. Já `re.fullmatch` verifica se a string inteira corresponde ao formato exigido. Pode-se usar como exemplo a tag `PT1010`: se o padrão reconhecer `PT101`, `re.match` poderá encontrar essa correspondência no início da string, embora `PT1010` seja uma tag inválida, o que pode causar erros nos processamentos posteriores. Portanto, utilizar `re.fullmatch` em `valida_tag` garante que a string inteira corresponda ao padrão definido para uma tag.
### R2 — Linhas inválidas

A função `ler_log` devolve as linhas inválidas para que a pessoa responsável pela análise dos dados possa examiná-las, investigar a causa do erro e buscar uma solução. Caso essas linhas fossem descartadas silenciosamente, falhas de comunicação ou linhas corrompidas poderiam passar despercebidas, dificultando a análise dos dados e podendo produzir resultados imprecisos devido à perda de leituras.

### R3 — Late binding

O dicionário `errados` utiliza o mesmo fator de conversão `k` para todas as suas funções `lambda`. Ao terminar a compreensão do dicionário, `k` corresponde ao último fator percorrido, que é `0.1`, da tag `FT201`. Por isso, `errados["PT102"](4095)` calcula 4095 x 0,1 = 409,5, em vez de retornar `600`. Já a função `criar_conversores` faz com que cada conversor preserve o fator correspondente à sua própria tag, evitando o problema de *late binding* e garantindo que a ordem dos itens não altere os resultados.

### R4 — Escala nominal

A escala nominal produz aproximadamente 262 kPa porque, no `marco1.py`, as contagens de `PT102` são convertidas por meio de um fator linear (`600/4095`). Entretanto, no `fornecido/simulador.py`, a função `c_real` utiliza arco-seno para gerar as contagens a partir da pressão, enquanto `p_real` utiliza seno na relação direta. Essa diferença explica por que a conversão nominal linear não recupera o valor de referência de 380 kPa.

### R5 — Previsão(*Estimativa retrospectiva) × medição (Etapa 3)

Não registrei as previsões em um commit antes das medições. As estimativas desta tabela foram reconstruídas posteriormente, com base no comportamento esperado das estruturas e operações.

| Grandeza | Estimativa retrospectiva | Medido |
| --- | --- | --- |
| Memória da lista / memória do `uint16` |10x|18,00x|
| Tempo do laço / tempo vetorizado |10x|19,21x|
| Tempo da compreensão / tempo do laço |1x|1,04x|

A maior diferença entre as estimativas retrospectivas e as medições ocorreu na razão entre o tempo do laço e o tempo vetorizado: 10× estimados contra 19,21× medidos. A `list` ocupou cerca de 18 vezes mais memória que `uint16`, pois armazena referências para objetos Python, enquanto cada elemento `uint16` ocupa 2 bytes. O produto 4095 × 20 = 81900 ultrapassa o máximo de 65535; o *overflow* corresponde a retirar uma volta de 65536, resultando em 16364. Escolheria `uint16` para contagens de 0 a 4095 e `float64` para pressões com valores decimais.
### R6 — Tipos da SerieTemporal (Etapa 4d)

Como não registrei os tipos previstos antes da implementação, a coluna de previsão abaixo foi reconstruída retrospectivamente.

| Expressão | Tipo previsto (*retrospectivamente) | Tipo observado |
| --- | --- | --- |
| `s + s` |SerieTemporal|SerieTemporal|
| `s[1:]` |SerieTemporal|SerieTemporal|
| `s * 2` |SerieTemporal|SerieTemporal|
| `s.sum()` |float64|SerieTemporal|
| `s[0]` |float64|float64|

O resultado de `s.sum()` me chamou a atenção porque eu esperava que a soma de todos os elementos retornasse um valor escalar. Entretanto, o resultado observado foi um objeto `SerieTemporal` de dimensão zero (`shape == ()`). Isso mostra que a operação preservou o tipo da subclasse `SerieTemporal`, mesmo produzindo um único valor.

### R7 — Issue #4

O defeito fazia `media_movel` retornar um resultado a menos: para uma série de 5 elementos e uma janela de 3, retornava 2 valores em vez dos 3 esperados. O teste `test_media_movel_tamanho_retornado` verifica a quantidade de resultados, enquanto `test_media_movel_valores_janela_2` confere as médias de `[10, 20, 30]`, que devem ser `[15, 25]`. A causa era a diferença entre fatias da soma acumulada sem um zero inicial; a correção foi inserir `0.0` no início para calcular também a primeira janela. Os testes de aceitação verificavam o tipo de retorno e os parâmetros inválidos, mas não esses casos específicos, cobertos pelos meus testes próprios.