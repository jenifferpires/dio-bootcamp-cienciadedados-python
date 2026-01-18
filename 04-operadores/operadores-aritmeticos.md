# 📌 Operadores Aritméticos em Python. 

## 📖 Introdução: 
Operadores aritméticos são utilizados para realizar cálculos matemáticos básicos.  
Eles estão presentes em praticamente qualquer sistema, desde cálculos simples até
processamentos complexos de dados.

---

## 🎯 Quando usar no dia a dia. 
- Cálculo de valores financeiros
- Processamento de dados numéricos
- Cálculo de médias, totais e percentuais
- Regras de negócio baseadas em números

---

## 🧠 Conceito:
Os operadores aritméticos permitem realizar operações matemáticas entre valores
numéricos, como soma, subtração, multiplicação e divisão.

Principais operadores:

- `+` → Soma  
- `-` → Subtração  
- `*` → Multiplicação  
- `/` → Divisão  
- `//` → Divisão inteira  
- `%` → Módulo (resto da divisão)  
- `**` → Exponenciação  

---

## 🧪 Exemplos práticos: 

#### Soma e subtração.
```python
a = 10
b = 3

print(a + b)  # 13
print(a - b)  # 7
```

📌 Utilizado em cálculos simples como totais e ajustes de valores.

#### Multiplicação e divisão.
```python
preco = 50
quantidade = 4

total = preco * quantidade
print(total)  # 200
```

📌 Muito comum em cálculos de compras, faturamento e estoque.

#### Divisão inteira e módulo.
```python
total_itens = 10
itens_por_caixa = 3

caixas = total_itens // itens_por_caixa
resto = total_itens % itens_por_caixa

print(caixas)  # 3
print(resto)   # 1
```

📌 Usado para divisão de recursos, páginas, lotes ou pacotes.

#### Exponenciação.
```python
base = 2
expoente = 3

resultado = base ** expoente
print(resultado)  # 8
```

📌 Aplicado em cálculos matemáticos, científicos e financeiros.

⚠️ Erros comuns

Erro 1: Dividir por zero
```python
resultado = 10 / 0  # Erro
```

Erro 2: Confundir / com //
```python
print(10 / 3)   # 3.333...
print(10 // 3)  # 3
```

### ✅ Boas práticas: 

Use // apenas quando a divisão inteira fizer sentido.  
Verifique divisões por zero.  
Utilize variáveis com nomes claros.  
Prefira clareza ao invés de expressões complexas.  

### 🌍 Ligação com o mundo real: 

Operadores aritméticos estão presentes em:  

Sistemas financeiros.   
Análises de dados.   
Relatórios e dashboards.   
Cálculos de métricas e indicadores.  

Eles formam a base para qualquer processamento numérico em Python.