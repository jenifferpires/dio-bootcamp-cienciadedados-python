# 📐 Estatística Descritiva.  

A estatística descritiva permite **resumir e compreender os dados** por meio de métricas numéricas.
Ela ajuda a responder perguntas simples, porém essenciais, como:  
“Qual é o valor típico?”, “Os dados variam muito?” e “Existem valores extremos?”.

Essa etapa complementa a análise exploratória e fornece uma base objetiva para interpretações.

---

## 🧭 Quando usar?  
A estatística descritiva é usada quando:

- Precisamos resumir grandes volumes de dados.
- Queremos entender o comportamento geral de uma variável.
- Comparamos grupos ou categorias.
- Identificamos variações e dispersões.
- Preparamos dados para análises mais avançadas.

---

## 🧠 Principais medidas.  

### 🔹 Medidas de tendência central:  
Indicam um valor representativo do conjunto.

- **Média**: soma dos valores dividida pela quantidade.
- **Mediana**: valor central quando os dados estão ordenados.
- **Moda**: valor que mais se repete.

Cada uma oferece uma visão diferente sobre os dados.

---

### 🔹 Medidas de dispersão:  
Mostram o quanto os dados variam.

- **Mínimo e máximo**: limites inferior e superior.
- **Amplitude**: diferença entre máximo e mínimo.
- **Desvio padrão**: indica o grau de dispersão em relação à média.

Dispersão alta geralmente indica dados mais heterogêneos.

---

## 🧪 Exemplos práticos em Python: 

### 🔹 Estatísticas gerais. 
```python
df.describe()
```
📌Retorna métricas como média, desvio padrão, mínimo, máximo e quartis para colunas numéricas.

### 🔹 Média e mediana.  
```python
df["valor"].mean()
df["valor"].median()
```
📌Comparar média e mediana ajuda a identificar assimetria nos dados.

### 🔹 Moda.
```sql
df["categoria"].mode()
```
📌Útil para entender valores mais frequentes em dados categóricos.

### 🔹 Desvio padrão:
```python
df["valor"].std()
```
📌Indica o quanto os valores se afastam da média.

## ⚠️ Pontos de atenção:  

Alguns cuidados importantes ao usar estatística descritiva:

A média pode ser distorcida por outliers.  
A mediana costuma representar melhor dados assimétricos.  
Moda pode não existir ou ter mais de um valor.  
Métricas isoladas não contam toda a história.  
Sempre analise as medidas em conjunto.  

## ✅ Boas práticas:  

Use mais de uma métrica para interpretar os dados.  
Combine estatística com análise visual.  
Analise contexto e domínio do problema.  
Documente interpretações importantes.  
Evite conclusões baseadas em um único número.  

## 🌍 Aplicação no mundo real:  

Estatística descritiva é usada em:

Relatórios gerenciais.  
Análises financeiras.  
Estudos de comportamento.  
Monitoramento de métricas.  
Avaliação de desempenho.  

Ela transforma dados brutos em informações compreensíveis, facilitando decisões baseadas em evidências.  
