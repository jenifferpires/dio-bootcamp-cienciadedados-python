# 🚨 Outliers (Valores Atípicos).  

Outliers são valores que **fogem significativamente do padrão** observado em um conjunto de dados.
Eles podem representar erros, eventos raros ou comportamentos legítimos, mas extremos.

Identificar e tratar outliers corretamente é essencial para evitar análises distorcidas e conclusões equivocadas.

---

## 🧭 Quando outliers aparecem?
Outliers surgem com frequência quando:

- Há erros de digitação ou coleta.
- Sistemas registram valores fora do esperado.
- Ocorrem eventos excepcionais (picos de vendas, falhas, fraudes).
- Os dados têm distribuição naturalmente assimétrica.
- Bases de dados misturam populações diferentes.

Nem todo outlier é um erro, mas todo outlier merece atenção.

---

## 🧠 Por que outliers importam?

Valores atípicos podem:

- Distorcer médias e desvios padrão.
- Influenciar modelos estatísticos e preditivos.
- Gerar interpretações incorretas.
- Indicar problemas de qualidade dos dados.
- Revelar eventos relevantes para o negócio.

O impacto depende do contexto e do objetivo da análise.

---

## 🧪 Identificando outliers em Python.  

### 🔹 Análise estatística simples
```python
df["valor"].describe()
```
📌Diferenças grandes entre máximo, média e quartis podem indicar outliers.

### 🔹 Método do intervalo interquartil (IQR).
```python
Q1 = df["valor"].quantile(0.25)
Q3 = df["valor"].quantile(0.75)
IQR = Q3 - Q1

outliers = df[(df["valor"] < Q1 - 1.5 * IQR) | (df["valor"] > Q3 + 1.5 * IQR)]
```
📌Esse método é bastante utilizado por ser simples e robusto.

### 🔹 Visualização com boxplot.
```python
df["valor"].plot(kind="box")
```
📌 O boxplot facilita a identificação visual de valores extremos.

## 🛠️ Estratégias para lidar com outliers.  
### 🔹 Manter os outliers: 

Indicado quando:  

* Eles representam eventos reais.  
* Fazem parte do fenômeno analisado.  

### 🔹 Remover outliers:  
```python
df_filtrado = df[(df["valor"] >= Q1 - 1.5 * IQR) & (df["valor"] <= Q3 + 1.5 * IQR)]
```

Útil quando:

* Os valores são claramente erros.  
* Comprometem a análise.  

### 🔹 Limitar valores (capping):  
```python
limite_superior = Q3 + 1.5 * IQR
df["valor"] = df["valor"].clip(upper=limite_superior)
```
📌Reduz o impacto dos outliers sem removê-los.  

## ⚠️ Pontos de atenção. 

Alguns cuidados importantes:

Remover outliers sem análise pode eliminar informações valiosas.  
O método de detecção depende da distribuição dos dados.  
O que é outlier em um contexto pode não ser em outro.  
Decisões devem ser justificadas e documentadas.  

## ✅ Boas práticas:  

Identifique outliers usando mais de um método.  
Analise o contexto antes de tratar.  
Avalie o impacto com e sem outliers.  
Documente as decisões tomadas.  
Evite tratamentos automáticos sem critério.  

## 🌍 Aplicação no mundo real.  

O tratamento de outliers é comum em:

Análises financeiras.  
Detecção de fraudes.  
Monitoramento de sistemas.  
Modelos preditivos.  
Estudos de comportamento.  

Tratar corretamente outliers melhora a qualidade, a robustez e a credibilidade das análises.