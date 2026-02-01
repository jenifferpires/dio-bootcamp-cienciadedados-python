# 🛠️ Preparação dos Dados.  

A preparação dos dados é a etapa em que transformamos dados brutos em dados prontos para análise, visualização ou modelagem.
Mesmo datasets aparentemente “bons” quase sempre precisam de ajustes antes de serem usados.

Essa etapa conecta a análise exploratória aos próximos passos do projeto.

---

## 🧭 Quando preparar os dados?
A preparação dos dados é necessária quando:

- Os dados vêm de fontes diferentes.
- Existem valores ausentes ou inconsistentes.
- As colunas não estão no formato correto.
- Precisamos criar novas variáveis.
- Os dados serão usados em modelos ou dashboards.

Quanto melhor a preparação, mais confiáveis serão os resultados.

---

## 🧠 O que envolve a preparação dos dados

A preparação pode incluir várias ações, como:

- 🧹 Limpeza de dados (nulos, duplicados, inconsistências).
- 🔄 Conversão de tipos (texto, datas, números).
- 🏷️ Padronização de valores categóricos.
- ➕ Criação de novas variáveis.
- 📐 Normalização ou padronização numérica.

Nem todas as etapas são sempre necessárias; tudo depende do objetivo.

---

## 🧪 Exemplos práticos em Python.  

### 🔹 Remoção de duplicados: 
```python
df = df.drop_duplicates()
```

📌Remove registros duplicados do dataset.

### 🔹 Conversão de tipos:  
```python
df["data"] = pd.to_datetime(df["data"])
```
📌Garante que a coluna seja tratada como data.

### 🔹 Padronização de texto:
```python
df["categoria"] = df["categoria"].str.lower().str.strip()
```
📌Evita problemas causados por variações de escrita.  

### 🔹 Criação de nova variável:
```python
df["valor_total"] = df["quantidade"] * df["preco_unitario"]
```
📌Cria uma nova coluna a partir de informações existentes.

### 🔹 Normalização simples: 
```python
df["valor_normalizado"] = (df["valor"] - df["valor"].min()) / (df["valor"].max() - df["valor"].min())
```
📌Coloca os valores em uma escala comum.

## ⚠️ Pontos de atenção:  

Durante a preparação, é importante evitar:

Alterar dados sem registrar o motivo.  
Perder informações relevantes. 
Aplicar transformações sem entender o impacto.  
Misturar etapas de preparação com análise final.  
Tornar o processo irreproduzível.  

## ✅ Boas práticas:  

Planeje a preparação de acordo com o objetivo final.

Documente todas as transformações.  
Mantenha o código organizado e legível.  
Crie funções reutilizáveis quando possível.  
Valide os dados após cada etapa.  

## 🌍 Aplicação no mundo real.  

A preparação de dados é essencial em:

Projetos de ciência de dados.  
Engenharia de dados.  
Criação de dashboards.  
Modelos de machine learning.  
Integração de múltiplas fontes de dados.  

Boa preparação reduz erros, melhora desempenho e aumenta a confiança nos resultados.  

## 🧾 Observação final:  

Grande parte do tempo em projetos de dados é gasto preparando dados.  
Investir nessa etapa é investir na qualidade de todo o trabalho que vem depois.  

