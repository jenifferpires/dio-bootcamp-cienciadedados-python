# 🔀 Estruturas Condicionais em Machine Learning.  

Em Machine Learning, **tomar decisões faz parte do processo** — desde o pré-processamento dos dados até a aplicação de regras, validações e fluxos de execução.

As **estruturas condicionais em Python** permitem que o código **responda dinamicamente aos dados**, sendo fundamentais em pipelines de ML.

---

## 🎯 Objetivo deste módulo:  

Ao final deste conteúdo, você será capaz de:

- Compreender o papel das estruturas condicionais em ML.  
- Utilizar `if`, `elif` e `else` de forma aplicada.  
- Implementar regras de decisão baseadas em dados.  
- Evitar erros lógicos comuns em fluxos condicionais.  

---

## 🧠 Por que estruturas condicionais são importantes em ML?

Embora os modelos façam previsões automaticamente, o código ao redor deles precisa:

- Validar dados de entrada.  
- Tratar valores inválidos ou ausentes.  
- Definir fluxos diferentes para treino e teste.  
- Aplicar regras de negócio.  
- Controlar execuções e exceções.  

Tudo isso depende de **condições bem definidas**.

---

## 🧩 Estrutura básica do `if` em Python

```python
if condicao:
    # código executado se a condição for verdadeira
```
**A condição deve sempre resultar em True ou False.** 

## 🔁 Estrutura completa: `if`, `elif` e `else`. 
```python 
if condicao_1:
    # executa se condicao_1 for verdadeira
elif condicao_2:
    # executa se condicao_2 for verdadeira
else:
    # executa se nenhuma condição anterior for verdadeira
```

## 📊 Exemplos práticos aplicados a ML:  

🔹 Validação de dados antes do treino.
```python
if len(dados) == 0:
    print("Base de dados vazia. Treinamento cancelado.")
else:
    print("Dados válidos. Iniciando treinamento.")
```    

🔹 Verificando presença de valores nulos.
```python
if df.isnull().sum().any():
    print("Existem valores nulos na base.")
else:
    print("Base sem valores nulos.")
```    

🔹 Separação entre treino e teste.
```python
if modo == "treino":
    treinar_modelo()
elif modo == "teste":
    avaliar_modelo()
else:
    print("Modo inválido.")
```    

## 🤖 Condicionais baseadas em métricas de modelo.  

Após o treinamento, decisões podem ser tomadas com base nos resultados.
```python
if acuracia >= 0.8:
    print("Modelo aprovado.")
else:
    print("Modelo precisa de ajustes.")
```

### ⚠️ Erros comuns no uso de condicionais em ML:  

❌ Condições mal definidas.  
❌ Comparações incorretas entre tipos diferentes.  
❌ Uso excessivo de if encadeados.  
❌ Falta de tratamento para casos inesperados.  
❌ Ignorar validações antes do treino.  

## ✅ Boas práticas:  

✔️ Escrever condições claras e objetivas.  
✔️ Validar dados antes de treinar modelos.  
✔️ Evitar lógica excessivamente complexa.  
✔️ Usar comentários para explicar decisões importantes.  
✔️ Testar todos os fluxos possíveis.  

## 🌍 Conexão com o mundo real:  

Em projetos reais de Machine Learning, estruturas condicionais são usadas para:

Automatizar pipelines.  
Validar dados de entrada.  
Controlar versões de modelos.  
Aplicar regras de negócio.  
Gerenciar erros e exceções.  

Um modelo eficiente depende de decisões bem estruturadas no código.

### 🧾 Conclusão:  

As estruturas condicionais conectam lógica de programação com decisões baseadas em dados.  
Elas garantem que o pipeline de Machine Learning seja robusto, confiável e adaptável a diferentes cenários.  

➡️ No próximo conteúdo, veremos como aplicar estruturas de repetição (for) em Machine Learning, fundamentais para percorrer dados, treinar modelos e avaliar resultados.  