# 🔎 Análise Exploratória de Dados (EDA)

A análise exploratória de dados é a primeira etapa prática ao trabalhar com um dataset.
O objetivo é **entender o que os dados mostram**, identificar padrões, problemas e direcionar os próximos passos da análise.

Antes de qualquer modelagem ou visualização avançada, a EDA ajuda a evitar conclusões erradas.

---

## 🧭 Quando usar?
A EDA é aplicada quando:

- Recebemos um novo conjunto de dados.
- Precisamos entender estrutura e conteúdo.
- Investigamos inconsistências ou erros.
- Validamos hipóteses iniciais.
- Preparamos dados para análises mais profundas.

---

## 🧠 O que observar na EDA

Durante a análise exploratória, observamos principalmente:

- 📦 Estrutura do dataset (linhas e colunas).
- 🧬 Tipos de dados (numéricos, categóricos, datas).
- 🧹 Dados ausentes ou duplicados.
- 📊 Distribuição dos valores.
- ⚠️ Possíveis outliers.

Esses pontos orientam decisões técnicas e de negócio.

---

## 🧪 Exemplos práticos em Python:  

### 🔹 Visualizando as primeiras linhas. 
```python
import pandas as pd

df = pd.read_csv("dados.csv")
df.head()
```
Permite um primeiro contato com os dados e seus formatos.

### 🔹 Estrutura e tipos de dados.  
```python
df.info()
```
📌Ajuda a identificar:

Tipos de cada coluna. 
Quantidade de valores nulos. 
Tamanho do dataset.  

### 🔹 Estatísticas iniciais:
```python
df.describe()
```
📌Resume numericamente colunas numéricas, facilitando a identificação de valores fora do esperado.

### ⚠️ Erros e Armadilhas comuns: 

Pular a EDA e ir direto para modelos.  
Ignorar valores nulos ou inconsistentes.  
Analisar apenas médias.  
Não considerar o contexto dos dados.  
Confiar em conclusões iniciais sem validação.  

## ✅ Boas práticas:  

Explore os dados com calma e curiosidade.  
Combine análise numérica e visual (quando possível).  
Registre descobertas importantes.  
Valide suposições com os próprios dados.  
Refaça a EDA sempre que os dados mudarem.  

## 🌍 Aplicação no mundo real:  

A EDA é usada em:

Análises de negócio.   
Ciência e engenharia de dados.  
Investigações de incidentes.  
Avaliação de qualidade de dados.  
Preparação para dashboards e modelos.  

Uma boa análise exploratória reduz riscos e aumenta a confiabilidade das decisões.  