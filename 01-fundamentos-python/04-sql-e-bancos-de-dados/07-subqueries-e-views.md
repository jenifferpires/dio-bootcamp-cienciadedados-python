# 📌 Subqueries e Views em SQL.  

## 📖 Introdução:  
Subqueries e views permitem **organizar consultas complexas** e **reaproveitar lógica SQL**.
Elas ajudam a tornar o código mais legível, reutilizável e fácil de manter.

Enquanto subqueries são consultas dentro de outras consultas, views funcionam como **consultas salvas** que podem ser reutilizadas como tabelas virtuais.

---

## 🎯 Como usar no dia a dia?
Você utiliza subqueries e views quando precisa:

- Resolver consultas que dependem de outros resultados.
- Simplificar SQLs longos e difíceis de ler.
- Reutilizar regras de negócio em várias consultas.
- Criar camadas de abstração para relatórios.
- Facilitar o acesso a dados por times de negócio.

---

## 🧠 Conceito.  

### 🔹 Subquery.  
Uma subquery é uma consulta SQL **dentro de outra consulta**.
Ela pode aparecer em diferentes partes do SQL, como:

- `WHERE`
- `FROM`
- `SELECT`

* A subquery é executada primeiro, e seu resultado é usado pela consulta principal.

---

### 🔹 View.  
Uma view é uma **consulta armazenada no banco de dados**.
Ela não guarda dados, apenas a lógica da consulta.

Vantagens das views:

- Reutilização de SQL.
- Melhor organização.
- Mais segurança (controle de acesso).
- Facilidade para relatórios.

---

## 🧪 Exemplos práticos:  

### 🔹 Subquery no WHERE:   
```sql
SELECT nome
FROM clientes
WHERE id_cliente IN (
    SELECT id_cliente
    FROM pedidos
    WHERE valor_total > 5000
);
```
Explicação:  
📌Retorna clientes que possuem pedidos acima de 5000.  

### 🔹 Subquery com agregação:  
```sql
SELECT nome
FROM clientes
WHERE id_cliente = (
    SELECT id_cliente
    FROM pedidos
    GROUP BY id_cliente
    ORDER BY SUM(valor_total) DESC
    LIMIT 1
);
```

Explicação:  
📌Retorna o cliente que mais gastou.  

### 🔹 Subquery no FROM:  
```sql
SELECT status, total
FROM (
    SELECT status, COUNT(*) AS total
    FROM pedidos
    GROUP BY status
) AS resumo_pedidos;
```

Explicação:  
📌Cria uma tabela temporária com pedidos agrupados por status.  

### 🔹 Criando uma view:  
```sql
CREATE VIEW vw_total_pedidos_cliente AS
SELECT id_cliente, SUM(valor_total) AS total_gasto
FROM pedidos
GROUP BY id_cliente;
```
Explicação:  
📌Cria uma view com o total gasto por cliente.  

### 🔹 Consultando uma view:  
```sql 
SELECT *
FROM vw_total_pedidos_cliente
WHERE total_gasto > 3000;
```
Explicação:  
📌Consulta a view como se fosse uma tabela.  

## ⚠️ Erros comuns:  

Criar subqueries quando um JOIN seria mais simples.  
Usar subqueries muito complexas e difíceis de manter.  
Esquecer alias em subqueries no FROM.  
Tratar views como tabelas físicas.  
Não documentar a finalidade das views.  

## ✅ Boas práticas:  

Use views para regras reutilizáveis.  
Use subqueries apenas quando fizerem sentido.  
Nomeie views de forma padronizada.  
Revise o impacto de performance.  

### 🌍 Ligação com o mundo real:  

Subqueries e views são amplamente usadas em relatórios corporativos, BI e sistemas analíticos.   
Elas permitem encapsular regras de negócio, reduzir erros e facilitar a colaboração entre times técnicos e de dados.  