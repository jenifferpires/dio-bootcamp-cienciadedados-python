# 🎨 Seaborn — Visualização Estatística em Python.

O **Seaborn** é uma biblioteca de visualização construída **sobre o Matplotlib**, focada em **análises estatísticas** e gráficos mais informativos com menos código.

Enquanto o Matplotlib oferece controle total, o Seaborn facilita a criação de gráficos **mais expressivos, esteticamente agradáveis e orientados a dados estatísticos**.

---

## 🧠 O que é o Seaborn?

Seaborn é utilizado principalmente para:

- Visualizar distribuições estatísticas
- Explorar relações entre variáveis
- Comparar grupos e categorias
- Analisar correlações
- Trabalhar com DataFrames (Pandas)

Ele integra-se naturalmente ao **Pandas**, o que o torna muito popular em **análise exploratória de dados (EDA)**.

---

## 🛠️ Instalação e importação:  

```bash
pip install seaborn
```
```python
import seaborn as sns
import matplotlib.pyplot as plt
```
📌 Mesmo usando Seaborn, o Matplotlib continua sendo usado para exibir e ajustar gráficos.  

## 📊 Dataset de exemplo:  

Seaborn já fornece alguns datasets prontos para estudo.

```python
import seaborn as sns

df = sns.load_dataset("tips")
df.head()
```
Esse dataset contém informações sobre contas de restaurante, gorjetas, dias da semana e categorias.  

---  

## 📈 Gráfico de distribuição (Histogram + KDE):

```python
sns.histplot(df["total_bill"], kde=True)
plt.title("Distribuição do valor total da conta")
plt.show()
```
📌 Ideal para analisar distribuição e densidade dos dados.  

---

## 📦 Boxplot — análise de outliers:  

```python
sns.boxplot(x="day", y="total_bill", data=df)
plt.title("Distribuição das contas por dia")
plt.show()
```
📌 Muito utilizado para:

- Identificar outliers.  
- Comparar distribuições entre categorias.  
---

## 🔵 Gráfico de dispersão com categorias:  

```python
sns.scatterplot(x="total_bill", y="tip", hue="sex", data=df)
plt.title("Relação entre valor da conta e gorjeta")
plt.show()
```
📌 Permite analisar relações entre variáveis, separando grupos por cor.  

---

## 📊 Gráfico de barras estatístico:

```python
sns.barplot(x="day", y="total_bill", data=df)
plt.title("Média do valor da conta por dia")
plt.show()
``` 
📌 Diferente do Matplotlib, o Seaborn aplica agregações estatísticas automaticamente (média por padrão).  

---

## 🔥 Mapa de calor (Heatmap):  

```python
correlacao = df.corr(numeric_only=True)

sns.heatmap(correlacao, annot=True, cmap="coolwarm")
plt.title("Mapa de correlação")
plt.show()
```
📌 Muito usado para:  

- Analisar correlações.  
- Identificar padrões entre variáveis numéricas.  

---

## 🎨 Estilos e temas:  

Seaborn permite aplicar estilos prontos:

```python
sns.set_theme(style="whitegrid")
```
Alguns estilos comuns:

`whitegrid`  
`darkgrid`  
`ticks`  
`dark`  

📌 Use estilos para melhorar legibilidade, não apenas estética.

### ⚠️ Erros comuns ao usar Seaborn:  

- Confiar apenas na estética e ignorar o significado do gráfico. 
- Não entender a estatística aplicada automaticamente.  
- Misturar muitos gráficos diferentes sem propósito.  
- Esquecer de validar os dados antes de visualizar.  

## ✅ Boas práticas:  

Sempre entenda o que o gráfico está calculando.  
Use Seaborn para análises estatísticas.  
Use Matplotlib para ajustes finos quando necessário.  
Combine clareza visual com contexto analítico.  
Pense no público-alvo da visualização.  

## 🌍 Aplicação no mundo real.  

Seaborn é amplamente utilizado em:

Análise exploratória de dados.  
Estudos estatísticos.  
Ciência de dados aplicada.  
Relatórios analíticos.  
Preparação de dados para Machine Learning.  

Ele ajuda a transformar dados em insights rapidamente.  

## 🧾 Observação final:  

Seaborn não substitui o Matplotlib, ele o complementa.  
Dominar ambos permite criar visualizações claras, informativas e profissionais.  

Visualização estatística é entender dados antes de modelar.  