# 📐 Avaliação de Modelos em Machine Learning. 

Após treinar um modelo de Machine Learning, é fundamental **avaliar seu desempenho**.  
A avaliação permite entender se o modelo está aprendendo corretamente, se generaliza bem para novos dados e se é confiável para uso real.

Sem avaliação adequada, um modelo pode parecer bom, mas falhar gravemente na prática.

---

## 🎯 Objetivo deste módulo:  

Ao final deste conteúdo, você será capaz de:

- Entender por que a avaliação de modelos é essencial.  
- Diferenciar métricas para classificação e regressão.
- Interpretar resultados corretamente.  
- Identificar overfitting e underfitting.  
- Aplicar boas práticas de validação.  

---

## 🧠 Por que avaliar modelos?

Avaliar um modelo serve para responder perguntas como:

- O modelo generaliza bem para dados novos?
- Ele está errando muito?
- Está aprendendo padrões reais ou apenas decorando os dados?
- Qual modelo performa melhor para o problema?

📌 **Treinar sem avaliar é como dirigir sem painel.**

---

## 🧪 Tipos de divisão dos dados.  

### 🔹 Treino e Teste:  

A base é dividida em dois conjuntos:

- **Treino:** usado para aprender os padrões.  
- **Teste:** usado apenas para avaliação final.  

```text
Treino → aprendizado  
Teste → avaliação
```
### 🔹 Treino, Validação e Teste:  

Usado em cenários mais robustos:

- **Treino**: aprendizado.  
- **Validação**: ajuste de parâmetros.  
- **Teste**: avaliação final.  
---

## 📊 Avaliação de modelos de classificação. 
#### 🎯 Acurácia: 

Percentual de previsões corretas.

📌 Boa quando as classes estão balanceadas.

---

#### 🎯 Precisão:  

Entre os positivos previstos, quantos estão corretos?

📌 Importante quando falsos positivos são críticos.

---

### 🎯 Recall (Sensibilidade):  

Entre os positivos reais, quantos o modelo identificou?

📌 Importante quando falsos negativos são críticos.

---

### 🎯 F1-Score:  

Média harmônica entre precisão e recall.

📌 Ideal para dados desbalanceados.

---

### 🎯 Matriz de Confusão:  

Mostra erros e acertos de forma detalhada.
```text
Verdadeiros Positivos | Falsos Positivos
Falsos Negativos      | Verdadeiros Negativos
```
---

### 📉 Avaliação de modelos de regressão:  
🔹 MAE (Erro Absoluto Médio)

Média dos erros absolutos.

---

🔹 MSE (Erro Quadrático Médio)

Penaliza erros maiores.

---

🔹 RMSE

Raiz quadrada do MSE, mais interpretável.

---

🔹 R² (Coeficiente de Determinação)

Indica quanto da variabilidade dos dados o modelo explica.

---

### 🧪 Exemplo prático em Python:  
```python
from sklearn.metrics import accuracy_score, confusion_matrix

accuracy = accuracy_score(y_test, y_pred)
matriz = confusion_matrix(y_test, y_pred)

print(accuracy)
print(matriz)
```

### ⚠️ Erros comuns:  

❌ Avaliar o modelo com dados de treino.   

❌ Usar apenas uma métrica.  

❌ Ignorar desbalanceamento de classes.  

❌ Comparar modelos com métricas diferentes.  

❌ Não validar resultados visualmente.  

### ✅ Boas práticas:  

✔️ Separar corretamente treino e teste.  
✔️ Escolher métricas adequadas ao problema.  
✔️ Avaliar mais de uma métrica.  
✔️ Analisar erros, não só acertos.  
✔️ Documentar resultados e decisões.  

### 🌍 Conexão com o mundo real.  

A avaliação de modelos é crítica em:

Sistemas de crédito.  
Diagnóstico médico.  
Detecção de fraudes.  
Recomendação de produtos.  
Tomada de decisão automatizada.  

Modelos mal avaliados podem gerar impactos reais e prejuízos.

### 🧾 Conclusão:  

Avaliar modelos é tão importante quanto treiná-los.
Uma boa avaliação garante confiabilidade, transparência e qualidade no uso de Machine Learning.  

➡️ No próximo conteúdo, avançaremos para boas práticas e erros comuns em ML, consolidando todo o aprendizado do módulo.  


