# 🧪 Primeiro Código em Python para Machine Learning. 

O objetivo deste conteúdo é consolidar, na prática, os principais conceitos vistos até aqui:

- Ambiente e ferramentas.  
- Tipos de variáveis e estruturas de dados. 
- Estruturas condicionais.  
- Estruturas de repetição.  

Aqui, vamos criar um **script simples**, com lógica clara e aplicável ao contexto de Machine Learning:     
**validar dados, gerar uma previsão baseada em regra e avaliar o resultado**.  

> 📌 Este ainda não é um modelo treinado, mas sim a base lógica que costuma existir antes (e ao redor) de qualquer modelo real.

---

## 🎯 Objetivo deste módulo:  

Ao final deste conteúdo, você será capaz de:

- Montar um fluxo simples de classificação com Python.  
- Validar dados de entrada com condicionais.  
- Processar dados com loops.  
- Gerar métricas básicas para avaliar resultados.  

---

## 🧠 Contexto do exemplo.   

Suponha que temos uma base simples de clientes com:

- `idade`
- `salario`
- `tempo_empresa`

E queremos classificar se um cliente é **"alto potencial"** (1) ou **"baixo potencial"** (0) com uma regra simples:

✅ Alto potencial se:
- salário ≥ 5000 **e**
- tempo de empresa ≥ 2 anos

⚠️ Essa lógica é apenas um exemplo para praticar estrutura de código.  
Em projetos reais, essa decisão seria aprendida por um modelo supervisionado.

---

## 📦 Dados de entrada (exemplo):  

```python
clientes = [
    {"idade": 25, "salario": 3500, "tempo_empresa": 1},
    {"idade": 30, "salario": 6000, "tempo_empresa": 3},
    {"idade": 45, "salario": 8000, "tempo_empresa": 10},
    {"idade": 22, "salario": 5000, "tempo_empresa": 1},
]
```

### ✅ Passo 1 — Função de validação:  

Antes de aplicar qualquer regra ou modelo, é importante validar os dados.
```python
def validar_cliente(cliente):
    campos_obrigatorios = ["idade", "salario", "tempo_empresa"]

    for campo in campos_obrigatorios:
        if campo not in cliente:
            return False

    if cliente["idade"] <= 0:
        return False

    if cliente["salario"] < 0:
        return False

    if cliente["tempo_empresa"] < 0:
        return False

    return True
```

### 🤖 Passo 2 — Regra de classificação (simulação de previsão):  
```python
def classificar_cliente(cliente):
    if cliente["salario"] >= 5000 and cliente["tempo_empresa"] >= 2:
        return 1
    return 0
```

### 🔁 Passo 3 — Processamento em lote:  

Agora percorremos todos os clientes, validamos e classificamos.
```python
previsoes = []
invalidos = 0

for cliente in clientes:
    if not validar_cliente(cliente):
        invalidos += 1
        continue

    previsao = classificar_cliente(cliente)
    previsoes.append(previsao)
```
### 📊 Passo 4 — Avaliação simples do resultado:  

Aqui vamos calcular quantos clientes foram classificados como alto potencial.
```python
total_validos = len(previsoes)
altos_potenciais = sum(previsoes)

print(f"Clientes válidos processados: {total_validos}")
print(f"Clientes inválidos ignorados: {invalidos}")
print(f"Altos potenciais identificados: {altos_potenciais}")
```
### 🧪 Código completo (pronto para executar):  
```python
clientes = [
    {"idade": 25, "salario": 3500, "tempo_empresa": 1},
    {"idade": 30, "salario": 6000, "tempo_empresa": 3},
    {"idade": 45, "salario": 8000, "tempo_empresa": 10},
    {"idade": 22, "salario": 5000, "tempo_empresa": 1},
]

def validar_cliente(cliente):
    campos_obrigatorios = ["idade", "salario", "tempo_empresa"]

    for campo in campos_obrigatorios:
        if campo not in cliente:
            return False

    if cliente["idade"] <= 0:
        return False

    if cliente["salario"] < 0:
        return False

    if cliente["tempo_empresa"] < 0:
        return False

    return True

def classificar_cliente(cliente):
    if cliente["salario"] >= 5000 and cliente["tempo_empresa"] >= 2:
        return 1
    return 0

previsoes = []
invalidos = 0

for cliente in clientes:
    if not validar_cliente(cliente):
        invalidos += 1
        continue

    previsao = classificar_cliente(cliente)
    previsoes.append(previsao)

total_validos = len(previsoes)
altos_potenciais = sum(previsoes)

print(f"Clientes válidos processados: {total_validos}")
print(f"Clientes inválidos ignorados: {invalidos}")
print(f"Altos potenciais identificados: {altos_potenciais}")
```
### ⚠️ Erros comuns:  

❌ Não validar os dados antes de processar.  
❌ Misturar tipos (ex.: salário como string).  
❌ Aplicar regras sem entender o contexto.  
❌ Não ter controle para dados inválidos.  
❌ Não separar validação, previsão e avaliação em funções.  


### ✅ Boas práticas:  

✔️ Validar dados de entrada sempre.  
✔️ Criar funções pequenas e reutilizáveis.  
✔️ Usar nomes claros para variáveis e funções.  
✔️ Garantir que o fluxo seja reprodutível.  
✔️ Separar dados, regras e resultados.  

### 🌍 Conexão com o mundo real:  

Esse exemplo é a base de um pipeline real, onde normalmente o próximo passo seria:

Transformar os dados em uma estrutura tabular (Pandas).  
Aplicar pré-processamento (normalização, encoding).  
Treinar um modelo supervisionado (Scikit-learn).  
Avaliar desempenho com métricas e validação.  

#### 🧾 Conclusão:  

Antes de um modelo de Machine Learning existir, existe um código bem estruturado que:

organiza os dados
valida entradas
processa em lote
gera resultados mensuráveis.  

➡️ A partir daqui, já temos base para avançar com conceitos e modelos de ML de forma mais consistente.