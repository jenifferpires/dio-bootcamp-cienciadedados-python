# 🔁 Estruturas de Repetição em Machine Learning.  

Em Machine Learning, trabalhar com **grandes volumes de dados** é a regra.  
Para isso, utilizamos **estruturas de repetição**, que permitem executar blocos de código várias vezes de forma controlada e eficiente.

Essas estruturas são essenciais para percorrer dados, treinar modelos, ajustar parâmetros e avaliar resultados.

---

## 🎯 Objetivo deste módulo:  

Ao final deste conteúdo, você será capaz de:

- Entender o papel das estruturas de repetição em ML. 
- Utilizar `for` e `while` em cenários práticos.  
- Aplicar repetições em dados, modelos e métricas.  
- Evitar loops ineficientes ou infinitos.  
- Escrever código mais limpo e performático.  

---

## 🧠 Por que estruturas de repetição são fundamentais em ML?

Em projetos de Machine Learning, loops são usados para:

- Percorrer datasets.  
- Aplicar transformações em colunas.  
- Treinar modelos com diferentes parâmetros.  
- Avaliar métricas repetidamente.  
- Automatizar pipelines de dados.  

Sem estruturas de repetição, essas tarefas seriam impraticáveis.

---

## 🔄 Estrutura `for` em Python.  

O `for` é a estrutura de repetição mais utilizada em ML.

```python
for elemento in colecao:
    # código executado a cada iteração
```

## 📊 Exemplos práticos aplicados a ML.  

🔹 Percorrendo uma lista de features.  
```python
features = ["idade", "salario", "tempo_empresa"]

for feature in features:
    print(f"Processando a feature: {feature}")
```

🔹 Iterando sobre linhas de um dataset.  
```python
for index, row in df.iterrows():
    print(row["idade"], row["salario"])
```

#### ⚠️ Obs.: em bases grandes, prefira operações vetorizadas.

🔹 Treinando modelos com diferentes parâmetros. 
```python
for n in [10, 50, 100]:
    modelo = RandomForestClassifier(n_estimators=n)
    modelo.fit(X_train, y_train)
    print(f"Modelo treinado com {n} árvores.")
```

## 🔁 Estrutura `while` em ML.  

O while executa o código enquanto uma condição for verdadeira.
```python 
while condicao:
    # código executado repetidamente
```    

### 🧪 Exemplo prático: controle de erro do modelo:  
```python
erro = 1.0

while erro > 0.1:
    ajustar_modelo()
    erro = calcular_erro()
```

📌 Muito útil em processos iterativos, como otimização e ajustes manuais.

### ⛔ Cuidado com loops infinitos:  

Um loop infinito ocorre quando a condição nunca se torna falsa.
```python
while True:
    print("Loop infinito")
```
❌ Evite esse tipo de estrutura sem um controle de saída.  

## 🛑 Uso de `break` e `continue`. 
🔹 `break` — interrompe o loop.
```python
for valor in dados:
    if valor < 0:
        break
```

🔹 `continue` — pula para a próxima iteração. 
```python
for valor in dados:
    if valor == 0:
        continue
    print(valor)
```

### ⚠️ Erros comuns ao usar repetição em ML:  

❌ Loops desnecessários em grandes datasets.  
❌ Falta de condição de parada.  
❌ Uso de while quando for seria mais adequado.  
❌ Ignorar desempenho e escalabilidade.  
❌ Repetir operações que poderiam ser vetorizadas.  

## ✅ Boas práticas:  

✔️ Prefira for para coleções finitas.  
✔️ Use while apenas quando a condição for dinâmica.  
✔️ Evite loops em datasets grandes sem necessidade.  
✔️ Documente o objetivo do loop.  
✔️ Combine loops com funções para código mais limpo.  

### 🌍 Conexão com o mundo real:  

Em ambientes profissionais, estruturas de repetição são usadas para:

Treinar e testar múltiplos modelos.  
Automatizar pipelines de ML.  
Processar dados em lote.  
Avaliar métricas continuamente.  
Simular cenários e ajustes.  

> Loops bem implementados tornam o código eficiente, escalável e confiável.

### 🧾 Conclusão:  

As estruturas de repetição são a base da automação em Machine Learning.  
Elas permitem que o código escale junto com os dados, garantindo produtividade e consistência.  

➡️ No próximo conteúdo, veremos o primeiro código em Python para Machine Learning, conectando tudo o que foi aprendido até aqui.  