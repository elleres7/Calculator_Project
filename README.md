
# Projeto de Calculadora em Python

Este é o meu primeiro projeto de uma calculadora simples feita em Python. A calculadora realiza operações básicas como soma, subtração, multiplicação e divisão. Este projeto foi desenvolvido com o objetivo de praticar conceitos de programação e familiarização com versionamento de código no GitHub.

## Componentes do Projeto

O projeto está organizado da seguinte forma:

```
📂 Calculator_Project
├── tests.py               # Arquivo com os testes automatizados
├── operations.py          # Arquivo com as funções da calculadora
├── calculator.py          # Arquivo principal para rodar a calculadora
└── README.md              # Arquivo explicativo do projeto
```

### Descrição dos Componentes

- **operations.py**: Contém as funções da calculadora (`som`, `sub`, `mult`, `div`). Essas funções executam as operações matemáticas e retornam os resultados.
- **tests.py**: Testes unitários para garantir o correto funcionamento das operações matemáticas. Utiliza o framework `unittest` do Python.
- **README.md**: Arquivo de documentação, explicando o projeto e como executá-lo.

## Funcionalidades da Calculadora

A calculadora pode realizar as seguintes operações:

1. **Soma**: Adiciona dois números.
2. **Subtração**: Subtrai o segundo número do primeiro.
3. **Multiplicação**: Multiplica dois números.
4. **Divisão**: Divide o primeiro número pelo segundo. Caso o segundo número seja zero, a função levanta um erro.

## Como Executar o Projeto

### Pré-requisitos

- Ter o Python instalado (versão 3.x).
- Um editor de código ou terminal para rodar o script.

### Passos para executar:

1. Clone este repositório:

```bash
git clone https://github.com/usuario/Calculator_Project.git
```

2. Navegue até o diretório do projeto:

```bash
cd Calculator_Project
```

3. Execute o arquivo principal `calculator.py` para utilizar a calculadora:

```bash
python calculator.py
```

4. Para rodar os testes unitários e garantir que tudo está funcionando corretamente:

```bash
python tests.py
```

## Testes

Os testes foram escritos para verificar a correção das operações de soma, subtração, multiplicação e divisão. Além disso, o teste de divisão também verifica se a exceção correta é levantada ao tentar dividir por zero.

## Exemplo de Uso

Aqui está um exemplo de como a calculadora funciona no terminal:

```bash
:: Calculadora Python ::

Escolha a operação que deseja realizar
 1 : Soma
 2 : Subtração
 3 : Multiplicação
 4 : Divisão

Digite a operação: 1
Digite o primeiro número: 10
Digite o segundo número: 5

Resultado: 15
```

## Tecnologias Utilizadas

- **Python**: Linguagem de programação para implementação do projeto.
- **Unittest**: Framework de testes utilizado para validar as funções.

## Autor

Desenvolvido por Suellen Elleres Silva.
