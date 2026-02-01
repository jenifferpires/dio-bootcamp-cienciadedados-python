# 🧩 Dados Ausentes.  

Dados ausentes (missing values) são informações que não foram registradas ou estão indisponíveis em um conjunto de dados.
Eles são comuns em bases reais e, quando ignorados, podem comprometer análises, métricas e modelos.

Entender **por que** os dados estão ausentes é tão importante quanto decidir **o que fazer** com eles.

---

## 🧭 Quando dados ausentes aparecem?  
Dados ausentes surgem com frequência quando:

- Campos não são preenchidos por usuários.
- Há falhas em integrações ou coletas automáticas.
- Sistemas legados não possuem determinadas informações.
- Dados são opcionais ou dependem de condições específicas.
- Ocorrem erros de processamento ou importação.

---

## 🧠 Tipos de dados ausentes.  

### 🔹 Ausência aleatória:  
O dado está ausente sem relação com outras variáveis.
Geralmente causa menos impacto estatístico.

---

### 🔹 Ausência não aleatória:  
A ausência está relacionada a algum padrão ou comportamento.
Exemplo: clientes que não informam renda.

Esse tipo exige mais cuidado na análise.

---

## 🧪 Identificando dados ausentes em Python.  

### 🔹 Verificando valores nulos:  
```python
df.isnull().sum()
```
📌Mostra a quantidade de valores ausentes por coluna.

### 🔹 Percentual de dados ausentes:  
```python
df.isnull().mean() * 100
``` 
📌Ajuda a avaliar o impacto dos dados ausentes no dataset.

## 🛠️ Estratégias para lidar com dados ausentes.  
### 🔹 Remoção de registros:  
```python
df.dropna()
```
📌 Útil quando:
A quantidade de dados ausentes é pequena.  
A remoção não compromete a análise.  

### 🔹 Preenchimento com valor fixo:  
```python
df.fillna(0)
```
📌Pode ser usado quando o valor ausente representa ausência real.   
Deve ser aplicado com cautela. 

### 🔹 Preenchimento com média ou mediana:  
```python
df["valor"].fillna(df["valor"].median())
```
📌A mediana costuma ser mais robusta em dados com outliers.  

### 🔹 Preenchimento categórico:  
```python
df["categoria"].fillna("Não informado")
```
📌Mantém registros e deixa explícita a ausência.  

## ⚠️ Pontos de atenção:  

Alguns cuidados importantes:

Remover dados pode reduzir amostra e viés.  
Preencher incorretamente pode distorcer resultados.  
Nem todo dado ausente deve ser tratado da mesma forma.  
O contexto do problema deve guiar a decisão.  

## ✅ Boas práticas:  

Sempre identifique e quantifique dados ausentes.  
Entenda a causa antes de aplicar uma estratégia.  
Documente decisões de tratamento.  
Teste o impacto das escolhas na análise.  
Evite soluções automáticas sem critério.  

## 🌍 Aplicação no mundo real. 

O tratamento de dados ausentes é essencial em:

Análises de negócio.  
Modelos preditivos.  
Relatórios corporativos.  
Sistemas de recomendação.  
Integrações entre bases de dados.  

Lidar corretamente com dados ausentes aumenta a confiabilidade e a qualidade das análises.  