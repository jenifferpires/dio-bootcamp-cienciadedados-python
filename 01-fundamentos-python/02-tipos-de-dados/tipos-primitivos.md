# Tipos Primitivos em Python.

Os **tipos primitivos** representam as estruturas de dados mais básicas da linguagem Python. Eles são usados para armazenar valores simples, como números, textos e valores lógicos, servindo como base para qualquer aplicação.

Compreender bem esses tipos é essencial para escrever códigos corretos, eficientes e fáceis de manter.

---

## 🔢 int — Números Inteiros.

O tipo `int` representa números inteiros, positivos ou negativos, sem casas decimais.

### Exemplos:

```python
idade = 30
quantidade = -5
```

Uso comum:

* Contadores
* Quantidades
* Índices de listas

---

## 🔢 float — Números Decimais. 

O tipo `float` representa números com casas decimais.

### Exemplos:

```python
altura = 1.75
preco = 19.99
```

⚠️ Atenção: operações com `float` podem apresentar pequenas imprecisões devido à forma como números decimais são representados internamente.

---

## 🔤 str — Texto (Strings). 

O tipo `str` representa sequências de caracteres (texto).

### Exemplos:

```python
nome = "Jeniffer"
mensagem = 'Bem-vinda ao Python'
```

Strings podem ser:

* Concatenadas
* Fatiadas
* Iteradas

---

## ✅ bool — Valores Booleanos. 

O tipo `bool` representa valores lógicos, podendo ser apenas:

* `True`
* `False`

### Exemplos:

```python
ativo = True
maior_de_idade = idade >= 18
```

Muito utilizado em:

* Condições (`if`, `elif`, `else`)
* Laços (`while`)
* Validações

---

## ⚠️ Erros comuns. 

### ❌ Erro 1 — Confundir tipos numéricos

```python
numero = "10" + 5  # TypeError
```

### ❌ Erro 2 — Comparar string com número

```python
idade = "18"
print(idade > 10)  # TypeError
```

---

## ✅ Boas práticas: 

### ✔️ Boa prática 1. 

Sempre verifique o tipo da variável quando houver dúvida:

```python
print(type(variavel))
```

### ✔️ Boa prática 2. 

Use nomes de variáveis claros e coerentes com o tipo armazenado:

```python
preco_produto = 29.90
```

---

## 📝 Observações: 

* Python é uma linguagem de tipagem dinâmica, ou seja, o tipo da variável é definido em tempo de execução. 
* Apesar disso, entender os tipos evita erros e melhora a legibilidade do código. 
* Esses tipos serão amplamente utilizados nos próximos módulos, principalmente em lógica, estruturas de controle e manipulação de dados. 
