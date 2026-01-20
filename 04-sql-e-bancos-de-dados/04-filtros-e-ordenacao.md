# 📌 Filtros e Ordenação em SQL.  

## 📖 Introdução:  
Filtros e ordenação permitem **refinar os dados retornados** por uma consulta SQL.  
Com eles, conseguimos buscar **apenas as informações relevantes** e organizá-las de forma clara para análise, relatórios ou validações.

Sem filtros, consultas retornam dados demais.    
Sem ordenação, os resultados podem não fazer sentido para quem analisa.  

---

## 🎯 Quando usar no dia a dia?   
Você usa filtros e ordenação quando precisa:

- Buscar registros específicos.  
- Aplicar regras de negócio em consultas.  
- Analisar subconjuntos de dados.  
- Organizar resultados para relatórios.  
- Investigar dados fora do padrão.  
- Preparar dados para dashboards.  

---

## 🧠 Conceito.  

### 🔹 WHERE — Filtro de registros:  
O `WHERE` define **condições** para selecionar apenas os dados desejados.

Operadores comuns:
- `=`, `!=`, `>`, `<`, `>=`, `<=`
- `IN`
- `BETWEEN`
- `LIKE`
- `IS NULL`

---

### 🔹 ORDER BY — Ordenação:  
O `ORDER BY` organiza o resultado da consulta.  

Tipos de ordenação:
- `ASC` → crescente (padrão)
- `DESC` → decrescente

---

## 🧪 Exemplos práticos:  

### 🔹 Exemplo 1 — Filtro simples:  
```sql
SELECT *
FROM clientes
WHERE cidade = 'São Paulo';
```
📌 Retorna apenas clientes da cidade informada.

### 🔹 Exemplo 2 — Filtro numérico: 
```sql
SELECT *
FROM pedidos
WHERE valor_total > 1000;
```
📌 Retorna pedidos acima de determinado valor.

### 🔹 Exemplo 3 — Filtro com múltiplas condições:  
```sql
SELECT *
FROM pedidos
WHERE valor_total > 500
  AND status = 'APROVADO';
```
📌 Ambas as condições precisam ser verdadeiras.  

### 🔹 Exemplo 4 — Filtro com IN:  
```sql
SELECT *
FROM clientes
WHERE estado IN ('SP', 'RJ', 'MG');
``` 
📌 Retorna clientes de estados específicos.  

### 🔹 Exemplo 5 — Filtro com intervalo: 
```sql
SELECT *
FROM pedidos
WHERE data_pedido BETWEEN '2024-01-01' AND '2024-12-31';
```
📌 Retorna pedidos dentro do período informado.  

### 🔹 Exemplo 6 — Ordenação simples:
```sql
SELECT nome, salario
FROM funcionarios
ORDER BY salario DESC;
```
📌 Lista funcionários do maior para o menor salário.  

### 🔹 Exemplo 7 — Filtro + ordenação:  
```sql
SELECT nome, salario
FROM funcionarios
WHERE salario > 3000
ORDER BY salario ASC;
```
📌 Filtra e organiza os resultados.  
 
## ⚠️ Erros comuns / armadilhas:  

❌ Esquecer o WHERE e retornar dados demais.  
❌ Usar LIKE quando = seria suficiente.  
❌ Comparar valores nulos com =  
❌ Ordenar dados sem entender o critério. 
❌ Criar filtros confusos ou difíceis de manter.  

## ✅ Boas práticas:  

✔️ Sempre valide filtros com poucos dados antes.  
✔️ Use AND / OR com cuidado.  
✔️ Prefira IN a múltiplos OR.  
✔️ Use ordenação apenas quando necessário.  
✔️ Mantenha condições claras e legíveis.  

### 📝 Observações:  

WHERE filtra antes da ordenação.  
Comparações com NULL devem usar IS NULL.  
Filtros mal definidos impactam desempenho.  

Leitura clara é mais importante que consultas “curtas”.  

## 🌍 Ligação com o mundo real:  

Filtros e ordenação são usados em:

Relatórios financeiros.  
Dashboards executivos.  
Auditorias de dados.  
Monitoramento de sistemas.  
Análises exploratórias.  

Dominar filtros significa extrair exatamente o dado certo, no momento certo.