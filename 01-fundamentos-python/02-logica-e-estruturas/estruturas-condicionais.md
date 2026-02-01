# 📌 Estruturas Condicionais em Python.  

## 📖 Introdução:  
Estruturas condicionais permitem que o programa tome decisões
com base em condições. Elas fazem com que o código siga caminhos
diferentes dependendo das regras definidas.

---

## 🎯 Quando usar no dia a dia?  
- Validação de dados
- Regras de negócio
- Controle de acesso
- Decisões baseadas em condições
- Fluxos alternativos em sistemas

---

## 🧠 Conceito:  
Em Python, as estruturas condicionais são compostas por:

- `if` → executa um bloco se a condição for verdadeira  
- `elif` → avalia outra condição, se a anterior for falsa  
- `else` → executa quando nenhuma condição é atendida  

As condições sempre retornam valores booleanos (`True` ou `False`).

---

## 🧪 Exemplos práticos: 

#### Condicional simples.

```python
idade = 20

if idade >= 18:
    print("Maior de idade")
```

📌 Executa o bloco apenas se a condição for verdadeira.

#### Condicional com else.

```python
idade = 16

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

📌 Define um caminho alternativo.

#### Uso de elif. 

```python 
nota = 7

if nota >= 9:
    print("Excelente")
elif nota >= 6:
    print("Aprovado")
else:
    print("Reprovado")
```

📌 Avalia múltiplas condições de forma organizada.

#### Condição com operadores lógicos.

```python  
idade = 25
possui_cnh = True

if idade >= 18 and possui_cnh:
    print("Pode dirigir")
else:
    print("Não pode dirigir") 
```

📌 Combina lógica e regras do mundo real.

#### Erros comuns:

**Erro 1: Esquecer a indentação.**

```python
if idade >= 18:
print("Erro") 
# Indentação incorreta.
```

**Erro 2: Condições confusas ou longas demais.**
```python
if idade >= 18 and idade <= 65 and possui_cnh == True and ativo == True:
```

### ✅ Boas práticas:  

Usar indentação correta (4 espaços).  
Manter condições simples.  
Utilizar variáveis com nomes claros.    
Evitar aninhar muitos ifs.    
Preferir legibilidade à complexidade.    

### 🌍 Ligação com o mundo real: 
Estruturas condicionais estão presentes em:

Sistemas bancários.  
Regras de desconto.  
Validação de formulários.  
Processos de aprovação.  
APIs e automações.  

Elas são a base da tomada de decisão em qualquer sistema.


