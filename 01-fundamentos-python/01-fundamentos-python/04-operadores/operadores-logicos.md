# 📌 Operadores Lógicos em Python.  

## 📖 Introdução:  
Operadores lógicos permitem combinar múltiplas condições em uma única expressão.
Eles são essenciais para criar regras de negócio mais completas e decisões
mais inteligentes dentro de um sistema.

---

## 🎯 Quando usar no dia a dia?  
- Validações com mais de uma condição
- Controle de acesso e permissões
- Regras de negócio complexas
- Filtros em dados e processos automatizados

---

## 🧠 Conceito:  
Os operadores lógicos trabalham com valores booleanos (`True` ou `False`)
e permitem combinar ou negar condições.

Principais operadores:

- `and` → Retorna True se **todas** as condições forem verdadeiras  
- `or` → Retorna True se **pelo menos uma** condição for verdadeira  
- `not` → Inverte o valor lógico  

---

## 🧪 Exemplos práticos:  

### Operador `and`
```python
idade = 20
possui_cnh = True

print(idade >= 18 and possui_cnh)  # True
```
📌 Usado quando todas as condições precisam ser atendidas.  

### Operador `or`
```python
dia_semana = "sábado"
feriado = False

print(dia_semana == "sábado" or feriado)  # True
```
📌 Utilizado quando apenas uma condição já é suficiente.  

### Operador `not`
```python
usuario_logado = False

print(not usuario_logado)  # True
```
📌 Muito usado para negar condições ou estados.

### Combinando operadores lógicos e relacionais: 
```python
nota = 7
frequencia = 80

if nota >= 6 and frequencia >= 75:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")
```
📌 Exemplo clássico de regra de negócio educacional.

## ⚠️ Erros comuns:  

**Erro 1: Esquecer a ordem de avaliação.**
```python
print(True or False and False)  # True
```
📌 and é avaliado antes de or.

**Erro 2: Comparações mal estruturadas.**
```python
if idade >= 18 and <= 65:  # Erro
```

## ✅ Boas práticas:  

Usar parênteses para melhorar a legibilidade.  
Manter condições simples e claras.  
Evitar expressões muito longas.  
Nomear variáveis de forma semântica.  

## 🌍 Ligação com o mundo real.  

Operadores lógicos são usados em:

Sistemas de autenticação.  
Regras de crédito e risco.  
Filtros de busca.  
Processos de decisão automatizados.  

Eles são fundamentais para transformar lógica em comportamento real do sistema.