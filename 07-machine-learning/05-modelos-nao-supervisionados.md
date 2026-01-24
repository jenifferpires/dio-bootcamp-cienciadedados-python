# 🧩 Modelos Não Supervisionados em Machine Learning.  

Modelos não supervisionados trabalham com **dados sem rótulos**, buscando padrões, estruturas e relações ocultas.    
Eles são amplamente utilizados quando o objetivo é **explorar os dados**, **segmentar grupos** ou **reduzir complexidade**, sem uma resposta correta previamente definida.

---

## 🎯 Objetivo deste módulo:  

Ao final deste conteúdo, você será capaz de:

- Entender o conceito de aprendizado não supervisionado.  
- Identificar problemas adequados a essa abordagem.  
- Conhecer os principais modelos não supervisionados.  
- Interpretar resultados de forma crítica.  
- Relacionar aplicações práticas no mundo real.  

---

## 🧠 O que caracteriza um modelo não supervisionado?

Um modelo não supervisionado é definido por:

- Ausência de rótulos (targets).  
- Aprendizado baseado em similaridade ou estrutura.  
- Descoberta de padrões sem supervisão explícita.  

Esses modelos **não “acertam” ou “erram”** no sentido clássico, mas **organizam os dados** de acordo com critérios matemáticos.  

---

## 🔍 Principais tipos de problemas não supervisionados.  

### 🔹 Clusterização (Agrupamento):  

Objetivo: agrupar dados semelhantes em **clusters**.

📌 **Exemplos:**
- Segmentação de clientes
- Agrupamento de produtos
- Análise de comportamento

---

### 🔹 Redução de Dimensionalidade:  

Objetivo: reduzir o número de variáveis mantendo a maior quantidade de informação possível.

📌 **Exemplos:**
- Visualização de dados
- Compressão
- Redução de ruído

---

## 📈 Principais modelos não supervisionados.  

### 🎯 K-Means:  

Algoritmo de clusterização que agrupa dados com base na distância ao centro do cluster.

📌 **Vantagens:**
- Simples e rápido.  
- Fácil interpretação.  

📌 **Cuidados:**
- Necessita definir o número de clusters.  
- Sensível a outliers.  

---

### 🧬 Hierarchical Clustering:  

Constrói uma hierarquia de clusters.

📌 **Vantagens:**
- Não exige número fixo de clusters inicialmente.  
- Visualização por dendrogramas.  

---

### 🔍 DBSCAN: 

Clusterização baseada em densidade.

📌 **Vantagens:**
- Identifica ruídos.  
- Não exige número fixo de clusters.  

📌 **Cuidados:**
- Sensível à escolha de parâmetros.  

---

### 📉 PCA (Análise de Componentes Principais).  

Técnica de redução de dimensionalidade.

📌 **Aplicações:**
- Visualização em 2D ou 3D.  
- Redução de ruído.  
- Pré-processamento para outros modelos.  

---

## 🧪 Exemplo simples em Python (K-Means).  

```python
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

clusters = kmeans.labels_
```

### ⚠️ Erros comuns:  

❌ Interpretar clusters como classes definitivas.  
❌ Escolher número de clusters sem análise.  
❌ Ignorar normalização dos dados.  
❌ Usar clusterização sem objetivo claro.  
❌ Não validar resultados visualmente.  

## ✅ Boas práticas:  

✔️ Entender o objetivo da análise antes de aplicar o modelo.  
✔️ Normalizar os dados quando necessário.  
✔️ Testar diferentes parâmetros.  
✔️ Avaliar resultados com visualizações.  
✔️ Documentar interpretações e decisões.  

## 🌍 Conexão com o mundo real:  

Modelos não supervisionados são amplamente usados em:

Segmentação de clientes.  
Análise de comportamento.  
Detecção de anomalias.  
Exploração inicial de dados.  
Apoio à tomada de decisão.  

Eles são fundamentais quando não existe resposta prévia, mas há grande valor em descobrir padrões.

### 🧾 Conclusão:  

Modelos não supervisionados permitem entender os dados antes de prever qualquer coisa.  
Eles ajudam a revelar estruturas ocultas e direcionar análises mais profundas.  

➡️ No próximo conteúdo, avançaremos para avaliação de modelos, etapa essencial para medir qualidade e confiabilidade.  