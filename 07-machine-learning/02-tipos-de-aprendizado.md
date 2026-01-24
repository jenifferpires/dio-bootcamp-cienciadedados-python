# 🧠 Tipos de Aprendizado em Machine Learning.  

Em Machine Learning, os algoritmos aprendem **padrões a partir de dados** para realizar previsões, classificações ou tomadas de decisão.  
Esses algoritmos podem ser organizados em **tipos de aprendizado**, de acordo com a forma como os dados são apresentados e como o modelo aprende.

Compreender esses tipos é essencial para **escolher a abordagem correta**, preparar os dados adequadamente e interpretar os resultados.

---

## 🎯 Objetivo deste módulo:  

Ao final deste conteúdo, você será capaz de:

- Entender os principais tipos de aprendizado em Machine Learning.  
- Identificar quando usar cada abordagem.  
- Relacionar tipos de aprendizado a problemas reais.  
- Conectar conceitos teóricos com aplicações práticas.  

---

## 🔍 O que define um tipo de aprendizado?

O tipo de aprendizado é definido principalmente por:

- Existência ou não de **rótulos** nos dados.  
- Forma como o modelo recebe feedback.  
- Objetivo do problema (previsão, agrupamento, decisão).  

---

## 🔹 1. Aprendizado Supervisionado.  

No aprendizado supervisionado, o modelo é treinado com **dados rotulados**, ou seja, cada entrada possui uma resposta correta associada.

📌 **Exemplo:**  
Uma base de clientes com informações e a indicação se houve ou não cancelamento de serviço.

### 📊 Principais tarefas:  
- **Classificação** → prever categorias (ex.: sim/não)
- **Regressão** → prever valores numéricos (ex.: preço, demanda)

### 📈 Algoritmos comuns:  
- Regressão Linear
- Regressão Logística
- Árvore de Decisão
- Random Forest
- K-Nearest Neighbors (KNN)

🧠 **Quando usar?**
- Quando existe histórico confiável de dados.  
- Quando o objetivo é prever um resultado conhecido.  

---

## 🔹 2. Aprendizado Não Supervisionado:  

No aprendizado não supervisionado, os dados **não possuem rótulos**.  
O modelo busca padrões, estruturas ou agrupamentos de forma automática.

📌 **Exemplo:**  
Agrupar clientes por comportamento de compra sem saber previamente quais grupos existem.

### 📊 Principais tarefas:  
- Clusterização
- Redução de dimensionalidade
- Descoberta de padrões

### 📈 Algoritmos comuns:  
- K-Means
- DBSCAN
- Hierarchical Clustering
- PCA (Análise de Componentes Principais)

🧠 **Quando usar?**
- Quando não há rótulos disponíveis
- Quando o objetivo é explorar e entender os dados

---

## 🔹 3. Aprendizado Semi-Supervisionado:  

O aprendizado semi-supervisionado combina **dados rotulados e não rotulados** durante o treinamento.

📌 **Exemplo:**  
Poucos registros rotulados e uma grande quantidade de dados sem rótulo.

🧠 **Quando usar?**
- Quando rotular dados é caro ou demorado
- Quando há poucos dados confiáveis rotulados

📈 **Aplicações comuns**
- Classificação de imagens
- Processamento de linguagem natural
- Detecção de fraudes

---

## 🔹 4. Aprendizado por Reforço:  

No aprendizado por reforço, um **agente aprende por tentativa e erro**, interagindo com um ambiente e recebendo recompensas ou punições.

📌 **Exemplo:**  
Um agente aprendendo a jogar um jogo maximizando sua pontuação ao longo do tempo.

### 🧩 Componentes principais:  
- Agente
- Ambiente
- Ações
- Recompensa

📈 **Aplicações comuns**
- Jogos
- Robótica
- Sistemas de recomendação
- Otimização de processos

---

## 🧩 Comparativo resumido:  

| Tipo de Aprendizado | Dados Rotulados | Objetivo Principal |
|--------------------|-----------------|--------------------|
| Supervisionado     | Sim             | Previsão e classificação |
| Não supervisionado | Não             | Descoberta de padrões |
| Semi-supervisionado| Parcialmente    | Melhorar aprendizado |
| Reforço            | Não             | Tomada de decisão |

---

## ⚠️ Erros comuns:  

- ❌ Escolher o tipo de aprendizado sem entender o problema
- ❌ Usar aprendizado supervisionado sem rótulos confiáveis
- ❌ Interpretar clusters como classes definitivas
- ❌ Ignorar o contexto do negócio

---

## ✅ Boas práticas:  

✔️ Entender bem o problema antes de escolher o modelo  
✔️ Avaliar a qualidade dos dados disponíveis  
✔️ Testar diferentes abordagens quando possível  
✔️ Validar resultados com métricas adequadas  

---

## 🌍 Conexão com o mundo real.  

No mercado, os tipos de aprendizado são aplicados em:

- Previsão de demanda
- Detecção de fraudes
- Sistemas de recomendação
- Segmentação de clientes
- Otimização de processos

Não existe um tipo “melhor”, mas sim o **mais adequado ao contexto**.

---

## 🧾 Conclusão:  

Machine Learning não começa no algoritmo, mas na **escolha correta da abordagem**.  
Entender os tipos de aprendizado é fundamental para construir soluções eficazes, interpretáveis e alinhadas ao problema real.

➡️ No próximo conteúdo, avançaremos para a **preparação de dados para Machine Learning**, etapa essencial antes do treinamento de modelos.
