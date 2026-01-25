# 📈 Matplotlib — Visualização de Dados em Python.

O **Matplotlib** é a principal biblioteca de visualização de dados em Python.  
Ela permite criar gráficos **simples ou altamente customizados**, sendo a base para muitas outras bibliotecas, como o Seaborn.  

Neste módulo, o foco é entender **como criar gráficos**, **controlar elementos visuais** e **evitar erros comuns**.  

---

## 🧠 O que é o Matplotlib?  

Matplotlib é uma biblioteca que permite transformar dados em **representações visuais**, como:

- Gráficos de linhas.  
- Gráficos de barras.  
- Histogramas.  
- Boxplots.  
- Gráficos de dispersão.  

Ela é amplamente utilizada em:
- Análise exploratória de dados (EDA).  
- Ciência de dados.  
- Machine Learning.  
- Relatórios e dashboards.  

---

## 🛠️ Estrutura básica de uso.  

O módulo mais utilizado é o `pyplot`, normalmente importado como `plt`.

```python
import matplotlib.pyplot as plt
```
A lógica geral segue este fluxo:

1. Definir os dados. 
2. Criar o gráfico.  
3. Ajustar títulos e rótulos.  
4. Exibir o gráfico.  

--- 

## 📊 Exemplo: Gráfico de linhas: 
```python
dias = [1, 2, 3, 4, 5]
vendas = [100, 120, 90, 150, 180]

plt.plot(dias, vendas)
plt.title("Evolução de Vendas")
plt.xlabel("Dias")
plt.ylabel("Quantidade")
plt.show()
```
📌 Ideal para analisar tendências ao longo do tempo.  

--- 

## 📊 Exemplo: Gráfico de barras:
```python
produtos = ["A", "B", "C"]
quantidades = [30, 50, 20]

plt.bar(produtos, quantidades)
plt.title("Vendas por Produto")
plt.xlabel("Produto")
plt.ylabel("Quantidade")
plt.show()
```
📌 Muito utilizado para comparar categorias.

---

## 📦 Exemplo: Histograma:
```python
import random

valores = [random.randint(1, 100) for _ in range(100)]

plt.hist(valores, bins=10)
plt.title("Distribuição dos Valores")
plt.show()
```
📌 Usado para analisar distribuição de dados.  

---

## 🔵 Exemplo: Gráfico de dispersão: 
```python 
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 6]

plt.scatter(x, y)
plt.title("Relação entre X e Y")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
```
📌 Ideal para identificar correlações e padrões.  

---

## 🎨 Customização básica:  

Alguns parâmetros importantes:
```python
plt.plot(x, y, color="blue", linestyle="--", marker="o")
```
`color`: define a cor.  
`linestyle`: estilo da linha.  
`marker`: marcador dos pontos.  

A customização deve melhorar a leitura, não poluir o gráfico.  

---

## ⚠️ Erros comuns ao usar Matplotlib.  

Alguns erros frequentes:

- Criar gráficos sem título.  
- Não rotular os eixos.  
- Usar cores aleatórias sem significado.  
- Misturar muitos gráficos em uma única visualização.  
- Esquecer o `plt.show()`.  

Esses erros dificultam a interpretação e reduzem a qualidade da análise.  

## ✅ Boas práticas:  

Sempre use título, rótulos e legendas quando necessário.  
Prefira gráficos simples e objetivos.  
Ajuste o tamanho do gráfico se necessário.  
Pense na mensagem que o gráfico deve transmitir.  
Menos informação visual costuma ser melhor.  

## 🌍 Aplicação no mundo real.  

Matplotlib é amplamente usado em:

- Análises exploratórias.  
- Protótipos de dashboards.  
- Relatórios técnicos.  
- Visualização de resultados de modelos de Machine Learning.  

Ele é a base para entender visualização de dados em Python.  

---

### 🧾 Observação final:  

Aprender Matplotlib é um passo essencial para quem trabalha com dados.  
Mesmo quando outras bibliotecas são usadas, o entendimento do Matplotlib continua sendo fundamental.  

Visualizar dados corretamente é transformar números em decisões.  