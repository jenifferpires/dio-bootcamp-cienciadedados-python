# 📌 Filtros e Ordenação em SQL.  

## 📖 Introdução:  
Filtros e ordenação permitem refinar os dados retornados por uma consulta SQL.
Com eles, é possível buscar apenas informações relevantes e organizá-las de forma clara.

Sem filtros, consultas retornam dados em excesso.
Sem ordenação, os resultados podem perder sentido analítico.

---

## 🎯 Como usar no dia a dia?  
Você utiliza filtros e ordenação quando precisa:

- Buscar registros específicos.
- Aplicar regras de negócio em consultas.
- Analisar subconjuntos de dados.
- Organizar resultados para relatórios.
- Investigar dados fora do padrão.
- Preparar dados para dashboards.

---

## 🧠 Conceito.  

### 🔹 WHERE — Filtro de registros:  
O `WHERE` define condições que determinam quais linhas serão retornadas.

Principais operadores:

- Comparação: `=`, `!=`, `<>`, `>`, `<`, `>=`, `<=`.
- Conjuntos: `IN`.
- Intervalos: `BETWEEN`.
- Texto: `LIKE`.
- Valores nulos: `IS NULL`, `IS NOT NULL`.
- Lógicos: `AND`, `OR`, `NOT`.

---

### 🔹 ORDER BY — Ordenação:  
O `ORDER BY` organiza os resultados da consulta.

- `ASC`: ordem crescente (padrão).
- `DESC`: ordem decrescente.

A ordenação ocorre após a aplicação dos filtros.

---

## 🧪 Exemplos práticos:  

### 🔹 Filtro simples:  
```sql
SELECT *
FROM clientes
WHERE cidade = 'São Paulo';
```
Explicação:  
📌Retorna apenas clientes da cidade informada.  

### 🔹 Filtro numérico: 
```sql
SELECT *
FROM pedidos
WHERE valor_total > 1000;
```
Explicação:    
📌Retorna pedidos com valor acima de 1000.  

### 🔹 Filtro com múltiplas condições (AND):  
```sql
SELECT *
FROM pedidos
WHERE valor_total > 500
  AND status = 'APROVADO';
  ```
Explicação:  
📌 Ambas as condições precisam ser verdadeiras.

### 🔹 Filtro com OR:  
```sql
SELECT *
FROM pedidos
WHERE status = 'APROVADO'
   OR status = 'PENDENTE';
```
Explicação:  
📌Retorna pedidos aprovados ou pendentes.

### 🔹 Filtro com IN:  
```sql
SELECT *
FROM clientes
WHERE estado IN ('SP', 'RJ', 'MG');
``` 
Explicação:    
📌Retorna clientes localizados nos estados informados.  

### 🔹 Filtro por intervalo (BETWEEN):  
```sql
SELECT *
FROM pedidos
WHERE data_pedido BETWEEN '2024-01-01' AND '2024-12-31';
``` 
Explicação:  
📌Retorna pedidos dentro do período especificado.  

### 🔹 Filtro com LIKE:  
```sql
SELECT *
FROM clientes
WHERE email LIKE '%@gmail.com';
```
Explicação:  
📌Retorna clientes com e-mails do domínio Gmail.

### 🔹 Ordenação simples:  
```sql
SELECT nome, salario
FROM funcionarios
ORDER BY salario DESC;
```
Explicação:    
📌Ordena os funcionários do maior para o menor salário.  

### 🔹 Filtro combinado com ordenação:  
```sql
SELECT nome, salario
FROM funcionarios
WHERE salario > 3000
ORDER BY salario ASC;
```
Explicação:  
📌Filtra salários acima de 3000 e ordena do menor para o maior.  

### 🔹 Ordenação por múltiplas colunas:  
```sql
SELECT *
FROM pedidos
ORDER BY status ASC, data_pedido DESC;
```
Explicação:  
📌Ordena primeiro por status e, em seguida, pela data mais recente.  

## ⚠️ Erros comuns:  
Esquecer o `WHERE` e retornar dados em excesso.  
Comparar valores nulos usando =.  
Misturar `AND` e `OR` sem parênteses.  
Usar `LIKE` sem necessidade.  
Ordenar grandes volumes sem critério.  

### ✅ Boas práticas:  
Teste filtros com poucos registros antes de rodar consultas grandes.  
Use parênteses ao combinar condições lógicas.  
Prefira clareza à complexidade.  
Evite `SELECT *` em consultas finais.  
Padronize a formatação do SQL.  

## 🌍 Ligação com o mundo real:  
Filtros e ordenação são usados em relatórios, dashboards, auditorias e análises.  
Dominar esses recursos evita interpretações erradas e melhora a qualidade das decisões baseadas em dados.  