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

## ✅ Boas práticas:  

Antes de rodar filtros em massa, teste com `LIMIT` para validar o resultado.    
  
Use `IN` quando fizer sentido, em vez de vários `OR`.    

Ao misturar `AND` e `OR`, use parênteses para explicitar a lógica.    

Selecione apenas colunas necessárias, em vez de `SELECT *`, quando for consulta “de verdade”.    

Padronize a formatação para facilitar leitura e revisão.    

### 📝 Observações: 

`WHERE` filtra linhas; 
`ORDER BY` apenas organiza o resultado.  

Em bancos diferentes, pequenos detalhes podem variar (por exemplo, != vs <>), mas a lógica é a mesma.  
  
Filtros e ordenações são comuns em relatórios e análises, então clareza é prioridade.  

## 🌍 Ligação com o mundo real:  

Filtros e ordenação aparecem em praticamente tudo: relatórios financeiros, dashboards, auditorias, monitoramento e investigações de incidentes.   
Saber montar filtros corretos (principalmente com `AND/OR` e `NULL`) evita conclusões erradas e retrabalho.