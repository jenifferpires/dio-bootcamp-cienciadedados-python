# 📊 Tipos de Gráficos.  

Escolher o tipo de gráfico correto é fundamental para **comunicar dados de forma clara e eficiente**.  
Cada tipo de gráfico responde melhor a **um tipo específico de pergunta**.

Um gráfico mal escolhido pode confundir.   
Um gráfico bem escolhido esclarece rapidamente. 

---

## 🧭 Quando pensar no tipo de gráfico?  

Antes de criar qualquer visualização, pergunte:  

- O objetivo é **comparar valores**?   
- Quero mostrar **distribuição**?  
- Preciso analisar **evolução no tempo**?  
- Desejo entender **proporções**?  
- Estou explorando **relação entre variáveis**?  

As respostas a essas perguntas orientam a escolha do gráfico mais adequado.  

---

## 📈 Gráfico de Linhas.  

Usado para analisar **evolução ao longo do tempo**.

```python
plt.plot(dias, vendas)
```
Ideal para:  
- Séries temporais.  
- Tendências.  
- Monitoramento contínuo.  
--- 

## 📊 Gráfico de Barras:  

Usado para comparar categorias.
```python
plt.bar(produtos, quantidades)
```
Ideal para:

- Comparar grupos.  
- Rankings.  
- Diferenças entre categorias.  
--- 

## 🥧 Gráfico de Pizza:  

Usado para mostrar proporções.
```python
plt.pie(valores, labels=labels)
```
Ideal para:  

- Distribuições simples. 
- Poucas categorias.  

⚠️ **Deve ser usado com cautela**, pois pode dificultar comparações quando há muitos valores.

---     

## 📦 Boxplot:  

Usado para analisar distribuição e outliers.
```python
plt.boxplot(valores)
```
Ideal para:  

- Identificar valores extremos.  
- Comparar distribuições.  
--- 

## 🔵 Gráfico de Dispersão:  

Usado para analisar relação entre variáveis.
```python
plt.scatter(x, y)
```
Ideal para:  

- Correlações.  
- Padrões e clusters.  
- Análise exploratória.  
--- 

### ⚠️ Pontos de atenção:  

- Nem todo dado precisa de gráfico.
- Gráficos inadequados geram interpretações erradas.
- Menos informação visual costuma ser melhor.
- Clareza deve vir antes da estética.
---

## ✅ Boas práticas:  

Escolha o gráfico conforme a pergunta.  
Evite misturar muitos elementos visuais.  
Rotule eixos e títulos corretamente.  
Use cores com propósito.  
Considere o público final.  

---

## 🌍 Aplicação no mundo real.  

A escolha correta do gráfico é essencial em:

Dashboards executivos.   
Relatórios de negócio.   
Análises exploratórias.  
Apresentações estratégicas.  

📌 Visualizar bem é comunicar bem.  