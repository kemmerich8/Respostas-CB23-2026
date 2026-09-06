# Respostas da Atividade Prática - Aula 05

## Questão 1: Relações de Herança

Analisando o diagrama fornecido, identificam-se três hierarquias distintas de herança:

### 1. Hierarquia de Pessoas e Cargos
* **Classe Base (Superclasse):** `Pessoa` (atributos: `nome: str`, `idade: int`).
* **Subclasse Intermediária:** `Funcionário` (herda de `Pessoa` e adiciona `salario: float`, `carga_horaria: int`).
* **Subclasses Específicas:** `Garçom`, `Chefe de cozinha` e `Gerente`.
  * `Garçom` herda os atributos de `Pessoa` e `Funcionário`, adicionando o método `anotar_pedido()`.
  * `Chefe de cozinha` herda os atributos de `Pessoa` e `Funcionário`, adicionando o método `preparar()`.
  * `Gerente` herda os atributos de `Pessoa` e `Funcionário`, adicionando o método `demitir()`.
* **Justificativa:** Todo funcionário é uma pessoa. Todos os cargos específicos (Garçom, Chefe, Gerente) são funcionários, compartilhando salário e carga horária, mas desempenhando responsabilidades únicas no sistema.

### 2. Hierarquia de Estabelecimentos
* **Classe Base (Superclasse):** `Restaurante` (atributos: `nome: str`, `endereco: str`, `telefone: str`).
* **Subclasse:** `Pizzaria` (herda de `Restaurante` e adiciona `rodizio: bool`).
* **Justificativa:** Uma pizzaria é uma especialização de restaurante. Ela possui nome, endereço e telefone como qualquer restaurante, acrescentando a opção de rodízio.

### 3. Hierarquia de Alimentos
* **Classe Base (Superclasse):** `Iguaria (comida)` (atributos: `nome: str`, `preco: float`).
* **Subclasses:** `Pizza` e `Bolo`.
  * `Pizza` herda `nome` e `preco` de `Iguaria`, adicionando `borda_rechada: bool`.
  * `Bolo` herda `nome` e `preco` de `Iguaria`, adicionando `formato: str`.
* **Justificativa:** Pizzas e bolos são tipos específicos de iguarias/comidas do cardápio, compartilhando características fundamentais como nome e preço.

---

## Questão 2: Relação entre Restaurante e Iguaria

* **Modelagem:** A relação deve ser modelada como uma **Agregação** com multiplicidade `1` para `0..*` (ou `1..*`), indicando que um restaurante possui um conjunto de iguarias em seu cardápio, mas as iguarias existem conceitualmente de forma independente.
* **Implementação:**
  1. A classe `Restaurante` deve incluir o atributo `cardapio: list[Iguaria]`.
  2. A classe `Restaurante` deve incluir métodos de gerenciamento, como `adicionar_iguaria(iguaria: Iguaria) -> None` e `remover_iguaria(iguaria: Iguaria) -> None`.

---

## Questão 3: Tipagem dos Argumentos

### 1. `argumento1` em `Garçom.anotar_pedido(argumento1)`
* **Tipo Apropriado:** `list[Iguaria]`
* **Justificativa:** Um garçom anota pedidos contendo itens alimentícios do cardápio. Tipar como `list[Iguaria]` aproveita o polimorfismo, permitindo que a lista contenha instâncias de qualquer subclasse de `Iguaria` (como `Pizza` ou `Bolo`).

### 2. `argumento2` em `Chefe de cozinha.preparar(argumento2)`
* **Tipo Apropriado:** `Iguaria`
* **Justificativa:** O chefe de cozinha prepara um item alimentício específico. Usar a superclasse `Iguaria` garante que o método aceite tanto um objeto `Pizza` quanto `Bolo`.
 
### 3. `argumento3` em `Gerente.demitir(argumento3)`
* **Tipo Apropriado:** `Funcionário`
* **Justificativa:** O gerente demite colaboradores do estabelecimento. A tipagem com a classe base `Funcionário` permite passar instâncias de qualquer subclasse (`Garçom`, `Chefe de cozinha` ou outro `Gerente`).