# 📌 Entrada e Saída de Dados em Python.  

## 📖 Introdução:  

Entrada e saída de dados são fundamentais para permitir a interação entre o usuário e o programa. Em Python, isso é feito principalmente por meio das funções `input()` e `print()`, que possibilitam receber informações e exibir resultados de forma simples e eficiente.

---

## 🎯 Quando usar no dia a dia:  

* Receber dados digitados pelo usuário em sistemas simples
* Coletar parâmetros para cálculos ou validações
* Exibir resultados, mensagens de erro ou feedbacks
* Simular interações comuns em scripts, APIs e automações

---

## 🧠 Conceito:  

* `input()` sempre retorna um valor do tipo **string**
* `print()` é usada para exibir informações no console
* Para trabalhar com números, é necessário converter o valor recebido com `input()`

---

## 🧪 Exemplos práticos:  

### Exemplo 1: Entrada e saída simples.  

```python
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")
```

📌 O programa solicita o nome do usuário e exibe uma mensagem personalizada.

---

### Exemplo 2: Entrada com conversão de tipo.  

```python
idade = int(input("Digite sua idade: "))
print(f"Você tem {idade} anos")
```

📌 O valor digitado é convertido para inteiro para permitir cálculos futuros.

---

## ⚠️ Erros comuns:  

**Erro 1:** Esquecer que `input()` retorna string

```python
idade = input("Digite sua idade: ")
print(idade + 1)  # Erro
```

**Erro 2:** Conversão inválida

```python
numero = int(input("Digite um número: "))  # Digitar letras gera erro
```

---

## ✅ Boas práticas:  

* Sempre validar entradas do usuário.  
* Converter tipos explicitamente.  
* Usar mensagens claras no `input()`.  
* Utilizar f-strings para melhorar a legibilidade do `print()`.  

---

## 🌍 Ligação com o mundo real.  

Entrada e saída de dados estão presentes em:

* Formulários de cadastro.  
* Sistemas bancários.  
* APIs que recebem parâmetros.  
* Scripts de automação e ETL.  

Dominar esse conceito é essencial para evoluir de scripts simples para aplicações reais.
