# 🔢 Tipos de Variáveis em Python para Machine Learning.  

Em Machine Learning, **dados são o insumo principal**.  
Antes de aplicar qualquer algoritmo, é essencial entender **como os dados são representados em Python** e **como cada tipo de variável impacta o modelo**.

Este conteúdo conecta os fundamentos da linguagem Python com sua aplicação prática em Machine Learning.

---

## 🎯 Objetivo deste módulo:  

Ao final deste material, você será capaz de:

- Identificar os principais tipos de variáveis em Python.  
- Entender como esses tipos são usados em ML.  
- Reconhecer quais formatos são aceitos por algoritmos.  
- Evitar erros comuns relacionados a tipos de dados.  

---

## 🧠 Por que os tipos de variáveis importam em ML?

Algoritmos de Machine Learning **não entendem texto ou conceitos humanos**.  
Eles trabalham com **valores numéricos**, estruturas bem definidas e padrões matemáticos.

Um tipo de dado incorreto pode:

- Gerar erros na execução.  
- Prejudicar o treinamento do modelo.  
- Produzir resultados inconsistentes.  
- Impedir a convergência do algoritmo.  

---

## 🐍 Principais tipos de variáveis em Python

### 🔢 Inteiros (`int`).  

Representam números inteiros, positivos ou negativos.

**Exemplos em ML:**
- Quantidade de vendas
- Número de acessos
- Idade (em alguns contextos)

```python
idade = 30
quantidade_vendas = 120
```
### 🔢 Números decimais (float).  

Representam valores contínuos, com casas decimais.

Muito comuns em ML, pois muitos algoritmos trabalham com variáveis contínuas.

Exemplos:  

Preço   
Temperatura  
Probabilidade  
Média de valores  

```python
preco = 49.90
temperatura = 22.5
```

### 🔤 Texto (`str`).   

Representam dados textuais.  

**⚠️ Importante:**  
*Algoritmos de ML não trabalham diretamente com strings.  
Esses dados precisam ser transformados antes do uso.*

Exemplos de dados textuais:   

Nome de produto  
Categoria  
Cidade  
Tipo de cliente  

```python
categoria = "Eletrônicos"
cidade = "São Paulo"
```

**➡️ Esses dados serão convertidos posteriormente em valores numéricos.**

### ✅ Valores booleanos (`bool`).  

Representam estados binários: verdadeiro ou falso.

Exemplos em ML:

Cliente ativo ou inativo.  
Pagamento realizado ou não.  
Produto disponível ou indisponível.  

```python
cliente_ativo = True
pagamento_confirmado = False
```

## 📦 Estruturas de dados mais usadas em ML:  

Além dos tipos básicos, Machine Learning utiliza estruturas para armazenar conjuntos de dados.

### 📋 Listas (`list`). 

Armazenam múltiplos valores em sequência.

```python
notas = [7.5, 8.0, 9.2]
```
São úteis, mas nem sempre ideais para operações matemáticas complexas.

### 🧱 Arrays NumPy (`ndarray`)

Estrutura fundamental para ML em Python.

Mais eficientes.  
Otimizados para cálculos matemáticos.  
Base para bibliotecas de ML.  

```python
import numpy as np

dados = np.array([1, 2, 3, 4])
```

### 📊 DataFrames (pandas.DataFrame).  

Estrutura tabular, semelhante a uma planilha.  
Muito usada na preparação e análise dos dados antes do treinamento.  

```python
import pandas as pd

df = pd.DataFrame({
    "idade": [25, 30, 45],
    "salario": [3000, 4500, 7000]
})
```

### 🔄 Tipos numéricos vs. tipos categóricos.  

Em ML, os dados geralmente são classificados como:

#### 🔢 Variáveis numéricas:    

Inteiros  
Decimais  
Quantitativas  

#### 🏷️ Variáveis categóricas:    

Texto    
Classes    
Rótulos    

**⚠️ Variáveis categóricas precisam ser transformadas antes de serem usadas em modelos.**

### ⚠️ Erros comuns ao lidar com variáveis em ML:  

❌ Usar strings diretamente em modelos.  
❌ Não verificar tipos de dados antes do treino.  
❌ Misturar tipos incompatíveis.  
❌ Ignorar valores nulos ou inválidos.  
❌ Tratar variáveis categóricas como numéricas sem conversão.  

### ✅ Boas práticas:  

✔️ Verificar os tipos de dados antes de treinar o modelo.  
✔️ Converter textos em formatos numéricos adequados.  
✔️ Padronizar estruturas de dados.  
✔️ Usar NumPy e Pandas para manipulação.  
✔️ Validar os dados antes do treinamento.  

### 🌍 Conexão com o mundo real.  

Em projetos profissionais de Machine Learning:

Grande parte do tempo é gasto preparando dados.  
Tipos incorretos causam falhas silenciosas.  
Bons modelos começam com bons dados.  
Entender variáveis é tão importante quanto escolher algoritmos.  

#### 🧾 Conclusão:  

Machine Learning começa antes dos algoritmos.  
Entender os tipos de variáveis em Python é um passo essencial para construir modelos confiáveis, eficientes e escaláveis.  

➡️ No próximo conteúdo, veremos como aplicar estruturas condicionais em Machine Learning, conectando lógica de programação com decisões baseadas em dados.
