# Conversão de Tipos em Python. 

A **conversão de tipos** (type casting) é o processo de transformar um valor de um tipo de dado em outro. Em Python, isso é feito de forma explícita por meio de funções específicas.

Esse conceito é fundamental, principalmente ao trabalhar com **entrada de dados**, **cálculos**, **APIs** e **manipulação de arquivos**.

---

## 🔁 Conversão Explícita.

Python fornece funções nativas para conversão de tipos:

* `int()` → converte para inteiro
* `float()` → converte para decimal
* `str()` → converte para texto
* `bool()` → converte para booleano

### Exemplos:

```python
numero_texto = "10"
numero = int(numero_texto)

preco = float("19.90")

idade = str(25)
```

---

## ⌨️ Conversão com input(). 

Por padrão, a função `input()` sempre retorna uma **string**.

### Exemplo incorreto:

```python
idade = input("Digite sua idade: ")
print(idade + 1)  # Erro
```

### Exemplo correto:

```python
idade = int(input("Digite sua idade: "))
print(idade + 1)
```

---

## 🔄 Conversão Implícita. 

A conversão implícita ocorre automaticamente quando o Python ajusta tipos compatíveis.

### Exemplo:

```python
resultado = 10 + 2.5
print(resultado)  # 12.5
```

Nesse caso, o Python converte o `int` para `float` automaticamente.

---

## ⚠️ Erros comuns. 

### ❌ Erro 1 — Converter string inválida. 

```python
numero = int("dez")  # ValueError
```

### ❌ Erro 2 — Esquecer de converter input. 

```python
quantidade = input("Digite a quantidade: ")
total = quantidade * 2  # Resultado inesperado
```

---

## ✅ Boas práticas: 

### ✔️ Boa prática 1. 

Sempre valide dados antes de converter:

```python
if valor.isdigit():
    valor = int(valor)
```

### ✔️ Boa prática 2. 

Converta o tipo o mais próximo possível da entrada do dado:

```python
peso = float(input("Digite o peso: "))
```

---

## 📝 Observações: 

* Conversões incorretas são uma das maiores fontes de erros em aplicações iniciantes.
* Em sistemas reais, é comum utilizar **tratamento de exceções** (`try/except`) para lidar com erros de conversão.
* Esse conceito será essencial nos próximos módulos de **lógica**, **estruturas condicionais** e **análise de dados**.
