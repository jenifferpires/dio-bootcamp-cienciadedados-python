# 📌 Operadores Relacionais em Python.

## 📖 Introdução: 
Operadores relacionais são utilizados para comparar valores.
Eles permitem que o programa tome decisões com base em condições,
retornando sempre um valor booleano: `True` ou `False`.

---

## 🎯 Quando usar no dia a dia: 
- Validações de regras de negócio.  
- Comparação de valores.  
- Controle de fluxos condicionais (`if`, `elif`, `else`).  
- Filtros em listas, dados e relatórios.  

---

## 🧠 Conceito:  
Os operadores relacionais comparam dois valores e retornam
um resultado lógico.  

Principais operadores:  

- `==` → Igual a  
- `!=` → Diferente de  
- `>` → Maior que  
- `<` → Menor que  
- `>=` → Maior ou igual  
- `<=` → Menor ou igual  

O resultado de qualquer comparação será sempre `True` ou `False`.

---

## 🧪 Exemplos práticos: 

### Comparação simples. 
```python
a = 10
b = 5

print(a > b)   # True
print(a == b)  # False
```

📌 Muito usado em validações básicas.

Comparando números: 

```python
idade = 18

print(idade >= 18)  # True
```

📌 Exemplo clássico de validação de maioridade.

Comparando strings: 
```python
usuario = "admin"

print(usuario == "admin")  # True
```

📌 Usado em autenticação e controle de acesso.

Comparando valores recebidos do usuário:
```python
senha = input("Digite a senha: ")

if senha == "1234":
    print("Acesso permitido")
else:
    print("Acesso negado")
```

📌 Comparações são essenciais para decisões condicionais.

⚠️ Erros comuns:

Erro 1: Usar = ao invés de ==

```python
if idade = 18:  # Erro de sintaxe
```

Erro 2: Comparar tipos diferentes sem conversão.

```python
idade = input("Digite sua idade: ")
print(idade >= 18)  # Erro
```

### ✅ Boas práticas: 

Sempre verificar o tipo dos dados comparados.  
Converter valores recebidos por input().  
Usar nomes de variáveis claros.  
Manter comparações simples e legíveis. 

## 🌍 Ligação com o mundo real: 

Operadores relacionais são usados em:

Sistemas de login.  
Validação de formulários.  
Regras de desconto.  
Processos de aprovação.  

Eles são a base para qualquer tomada de decisão em um sistema.


