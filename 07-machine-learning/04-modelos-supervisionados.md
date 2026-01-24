# 📊 Modelos Supervisionados em Machine Learning.  

Modelos supervisionados aprendem a partir de **dados rotulados**, ou seja, cada exemplo de entrada possui uma resposta correta associada.  
Eles são amplamente utilizados quando o objetivo é **prever valores** ou **classificar informações** com base em histórico conhecido.

Este é um dos tipos de aprendizado mais comuns e aplicados no mercado.

---

## 🎯 Objetivo deste módulo:  

Ao final deste conteúdo, você será capaz de:

- Entender o conceito de aprendizado supervisionado.  
- Diferenciar classificação e regressão. 
- Conhecer os principais modelos supervisionados.  
- Identificar quando utilizar cada abordagem.  
- Relacionar modelos com problemas reais.  

---

## 🧠 O que caracteriza um modelo supervisionado?

Um modelo supervisionado é definido por:

- **Dados de entrada (features)**  
- **Rótulos (target)**  
- **Processo de aprendizado baseado em erro**  

Durante o treinamento, o modelo compara suas previsões com os rótulos reais e ajusta seus parâmetros para reduzir o erro.

---

## 🔍 Principais tipos de problemas supervisionados

### 🔹 Classificação:  

Objetivo: prever **categorias ou classes**.

📌 **Exemplos:**
- Cliente irá cancelar o serviço? (sim / não)
- Email é spam ou não?
- Transação é fraudulenta?

---

### 🔹 Regressão:  

Objetivo: prever **valores numéricos contínuos**.

📌 **Exemplos:**
- Preço de um imóvel
- Demanda de vendas
- Consumo de energia

---

## 📈 Principais modelos supervisionados.  

### 📐 Regressão Linear:  

Modelo simples e interpretável, utilizado para problemas de regressão.

📌 **Quando usar?**
- Relação aproximadamente linear entre variáveis.  
- Análises exploratórias e previsões simples.  

---

### 🧮 Regressão Logística:  

Apesar do nome, é usada para **classificação**.

📌 **Aplicações comuns:**
- Classificação binária
- Probabilidades de eventos

---

### 🌳 Árvore de Decisão:  

Modelo baseado em regras e divisões do espaço de dados.

📌 **Vantagens:**
- Fácil interpretação
- Visualização clara

📌 **Cuidados:**
- Pode sofrer overfitting

---

### 🌲 Random Forest:  

Conjunto de várias árvores de decisão para melhorar a performance.

📌 **Vantagens:**
- Reduz overfitting
- Boa performance em diversos cenários

📌 **Desvantagens:**
- Menor interpretabilidade

---

### 👥 K-Nearest Neighbors (KNN).  

Classifica com base na proximidade entre os dados.

📌 **Quando usar?**
- Bases pequenas ou médias
- Dados bem distribuídos

---

## 🧪 Exemplo simples em Python:  

```python
from sklearn.linear_model import LogisticRegression

modelo = LogisticRegression()
modelo.fit(X_train, y_train)

previsoes = modelo.predict(X_test)
```
### ⚠️ Erros comuns:  

❌ Treinar modelos sem dados preparados.  
❌ Não separar treino e teste.  
❌ Usar modelo complexo sem necessidade.  
❌ Ignorar overfitting.  
❌ Avaliar o modelo apenas pela acurácia.  

## ✅ Boas práticas:  

✔️ Começar com modelos simples.  
✔️ Validar resultados com métricas adequadas.  
✔️ Comparar diferentes modelos.  
✔️ Ajustar hiperparâmetros quando necessário.  
✔️ Documentar decisões e resultados.  

## 🌍 Conexão com o mundo real:  

Modelos supervisionados são amplamente usados em:

Previsão de vendas.  
Detecção de fraudes.  
Análise de risco. 
Sistemas de recomendação.  
Classificação de clientes.  

Eles formam a base de muitas soluções de Machine Learning em produção.

## 🧾 Conclusão:  

Modelos supervisionados permitem transformar dados históricos em previsões acionáveis.  
Escolher o modelo correto depende do problema, da qualidade dos dados e dos objetivos do negócio.  

➡️ No próximo conteúdo, exploraremos modelos não supervisionados, focados na descoberta de padrões sem rótulos.  
