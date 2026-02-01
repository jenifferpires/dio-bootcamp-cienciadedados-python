# 🧹 Preparação de Dados para Machine Learning.  

Antes de treinar qualquer modelo de Machine Learning, é indispensável preparar os dados.  
A **preparação de dados** garante qualidade, consistência e representatividade, impactando diretamente o desempenho e a confiabilidade dos modelos.

Na prática, esta etapa costuma consumir **a maior parte do tempo** em projetos de ML.

---

## 🎯 Objetivo deste módulo:  

Ao final deste conteúdo, você será capaz de:

- Entender a importância da preparação de dados em ML.  
- Identificar problemas comuns em bases de dados.  
- Aplicar técnicas básicas de limpeza e transformação.  
- Preparar dados para uso em modelos supervisionados e não supervisionados.  

---

## 🧠 Por que a preparação de dados é tão importante?

Modelos de Machine Learning aprendem **padrões a partir dos dados fornecidos**.  
Se os dados forem inconsistentes, incompletos ou enviesados, o modelo refletirá esses problemas.

Uma boa preparação ajuda a:
- Reduzir ruído
- Evitar vieses
- Melhorar a performance do modelo
- Garantir resultados mais confiáveis

---

## 🔍 Etapas comuns na preparação de dados

Embora variem conforme o problema, as etapas mais comuns são:

1. Entendimento da base de dados.    
2. Limpeza dos dados.    
3. Tratamento de valores ausentes.  
4. Tratamento de outliers.    
5. Conversão de variáveis categóricas.    
6. Normalização ou padronização.    
7. Separação entre treino e teste.    

---

## 📊 Entendimento inicial dos dados:  

Antes de qualquer transformação, é essencial **explorar a base**.

```python
df.head()
df.info()
df.describe()
```
Esses comandos ajudam a identificar:

Tipos de variáveis
Valores ausentes
Distribuição dos dados
Possíveis inconsistências

### 🧼 Limpeza de dados:  

A limpeza envolve remover ou corrigir dados inválidos.

🔹 Exemplos de problemas comuns: 

* Valores negativos onde não deveriam existir.  
* Registros duplicados.  
* Dados fora do domínio esperado.  

```python
df = df[df["salario"] >= 0]
df = df.drop_duplicates()
```

### ❓ Tratamento de valores ausentes:  

Valores ausentes são comuns e devem ser tratados com cuidado.

🔹 Estratégias comuns:  

* Remoção de registros.  
* Substituição por média, mediana ou moda.  
* Uso de valores padrão.  

```python
df["idade"] = df["idade"].fillna(df["idade"].median())
```

**⚠️ A estratégia deve considerar o contexto do problema.** 

### 📉 Tratamento de outliers.  

Outliers são valores extremos que podem distorcer o modelo.

🔹 Possíveis abordagens:  

* Remover outliers.  
* Limitar valores (capping).  
* Analisar se representam casos reais.  

```python
limite = df["salario"].quantile(0.99)
df = df[df["salario"] <= limite]
```

### 🏷️ Conversão de variáveis categóricas:  

Modelos de ML trabalham com números.
Variáveis categóricas precisam ser transformadas.

🔹 Técnicas comuns:  

* Label Encoding.
* One-Hot Encoding.

```python
df = pd.get_dummies(df, columns=["categoria"])
```

### 📐 Normalização e padronização:

Escalas diferentes podem prejudicar o aprendizado do modelo.

🔹 Normalização; 

Transforma os dados para um intervalo específico (ex.: 0 a 1).

🔹 Padronização: 

Centraliza os dados em média 0 e desvio padrão 1.

Essas técnicas são especialmente importantes em:

* Regressão

* KNN

* Redes neurais

### 🔀 Separação entre treino e teste:  

Separar os dados evita que o modelo seja avaliado com informações que já viu.
```PYTHON
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

### ⚠️ Erros comuns na preparação de dados:  

❌ Treinar modelo sem limpar os dados.  
❌ Ignorar valores ausentes.  
❌ Vazamento de dados entre treino e teste.  
❌ Tratar outliers sem análise.  
❌ Aplicar encoding incorreto.   

### ✅ Boas práticas:  

✔️ Explorar os dados antes de qualquer decisão.  
✔️ Documentar todas as transformações.  
✔️ Aplicar as mesmas transformações em treino e teste.  
✔️ Testar diferentes abordagens de preparação.  
✔️ Avaliar impacto das transformações no modelo.  

### 🌍 Conexão com o mundo real:  

Em ambientes profissionais, pipelines de preparação de dados são:

Automatizados   
Versionados  
Testados  
Reutilizáveis  

A qualidade do modelo depende diretamente da qualidade dos dados.

#### 🧾 Conclusão:  

A preparação de dados é a base de qualquer projeto de Machine Learning.
Modelos sofisticados não compensam dados mal preparados.

➡️ No próximo conteúdo, avançaremos para modelos supervisionados, aplicando os dados preparados ao treinamento de algoritmos.