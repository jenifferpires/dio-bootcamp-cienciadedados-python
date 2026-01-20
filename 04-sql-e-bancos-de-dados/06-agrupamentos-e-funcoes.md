# 📌 Agrupamentos e Funções em SQL.  

## 📖 Introdução:  
Agrupamentos e funções agregadas permitem **resumir, calcular e analisar dados** de forma consolidada.
Em vez de analisar linha por linha, conseguimos obter totais, médias, contagens e outros indicadores importantes.

Esses recursos são essenciais para relatórios, análises e tomada de decisão baseada em dados.

---

## 🎯 Como usar no dia a dia?
Você utiliza agrupamentos e funções quando precisa:

- Calcular totais de vendas.
- Contar registros (clientes, pedidos, acessos).
- Obter médias, valores mínimos ou máximos.
- Agrupar dados por categoria, data ou status.
- Criar métricas para dashboards e relatórios.

---

## 🧠 Conceito.  

### 🔹 Funções agregadas
São funções que **operam sobre um conjunto de linhas** e retornam um único valor.

Principais funções:

- `COUNT()` → conta registros.
- `SUM()` → soma valores.
- `AVG()` → calcula a média.
- `MIN()` → retorna o menor valor.
- `MAX()` → retorna o maior valor.

---

### 🔹 GROUP BY:  
O `GROUP BY` agrupa linhas que possuem o **mesmo valor** em uma ou mais colunas.

Cada grupo gera **uma linha no resultado final**.

Regra importante:
> Toda coluna no `SELECT` que não estiver dentro de uma função agregada deve aparecer no `GROUP BY`.

---

### 🔹 HAVING:  
O `HAVING` filtra **após o agrupamento**.
Ele é usado para aplicar condições sobre resultados agregados.

Diferença essencial:
- `WHERE` filtra linhas.
- `HAVING` filtra grupos.

---

## 🧪 Exemplos práticos:  

#### 🔹 Contar registros. 
```sql
SELECT COUNT(*) AS total_clientes
FROM clientes;
```
Explicação:  
📌Conta o número total de clientes cadastrados.

#### 🔹 Somar valores. 
```sql
SELECT SUM(valor_total) AS faturamento_total
FROM pedidos;
```
Explicação:  
📌Retorna o valor total de vendas.  

### 🔹 Média de valores:  
```sql
SELECT AVG(valor_total) AS ticket_medio
FROM pedidos;
```
Explicação:  
📌Calcula o valor médio dos pedidos.  

#### 🔹 Agrupamento simples:  
```sql
SELECT status, COUNT(*) AS quantidade
FROM pedidos
GROUP BY status;
```  
Explicação:  
📌Conta quantos pedidos existem por status.  

#### 🔹 Agrupamento com soma:  
```sql
SELECT id_cliente, SUM(valor_total) AS total_gasto
FROM pedidos
GROUP BY id_cliente;
```
Explicação:  
📌Calcula quanto cada cliente gastou no total.  

#### 🔹 Agrupamento com filtro (HAVING):  
```sql
SELECT id_cliente, SUM(valor_total) AS total_gasto
FROM pedidos
GROUP BY id_cliente
HAVING SUM(valor_total) > 5000;
```
Explicação:  
📌Retorna apenas clientes com gasto total acima de 5000.  

#### 🔹 WHERE + GROUP BY + HAVING:
```sql
SELECT status, COUNT(*) AS quantidade
FROM pedidos
WHERE data_pedido >= '2024-01-01'
GROUP BY status
HAVING COUNT(*) > 10;
```
Explicação:  
📌Agrupa pedidos recentes por status e retorna apenas grupos com mais de 10 registros.  

## ⚠️ Erros comuns:  

Usar WHERE para filtrar valores agregados.  
Esquecer colunas no GROUP BY.  
Agrupar dados sem entender o objetivo da análise.  
Criar métricas sem validar os resultados.  
Não usar alias em colunas agregadas.    

### ✅ Boas práticas:  

Sempre use alias para funções agregadas.  
Valide resultados com consultas simples antes.  
Combine WHERE e HAVING corretamente.  
Mantenha consultas legíveis e bem formatadas.  
Documente métricas importantes.  

### 🌍 Ligação com o mundo real:  

Agrupamentos e funções são usados em relatórios financeiros, análises de negócio, BI e ciência de dados.  
Dominar esses recursos permite transformar grandes volumes de dados em informação útil e acionável.