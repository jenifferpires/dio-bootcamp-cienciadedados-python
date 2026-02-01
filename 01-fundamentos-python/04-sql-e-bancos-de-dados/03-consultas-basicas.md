# 📌 Consultas Básicas em SQL.

## 📖 Introdução:
Consultas básicas são o **ponto de partida do SQL**.  
Elas permitem **buscar, visualizar e entender os dados** armazenados em um banco de dados, sendo essenciais para análises, validações e tomadas de decisão.

O comando central desse processo é o `SELECT`.

---

## 🎯 Quando usar no dia a dia:  
Você utiliza consultas básicas quando precisa:

- Visualizar dados de uma tabela.  
- Validar informações inseridas no banco.  
- Criar relatórios simples.  
- Apoiar análises exploratórias.  
- Investigar erros ou inconsistências.  
- Conferir dados antes de alterações (`UPDATE` ou `DELETE`).  

---

## 🧠 Conceito:  
A estrutura básica de uma consulta SQL é composta por:

```text
SELECT → o que quero ver
FROM   → de onde vem o dado
```
Com isso, conseguimos acessar dados de forma clara e objetiva.

### 🔹 SELECT:  
Define quais colunas serão retornadas.  

### 🔹 FROM:  
Define qual tabela será consultada.  

### 🧪 Exemplos práticos:  
🔹 Exemplo 1 — Selecionando todas as colunas:
```sql
SELECT *
FROM clientes;
```
📌 Retorna todos os dados da tabela clientes.  

🔹 Exemplo 2 — Selecionando colunas específicas:  
```sql
SELECT nome, email
FROM clientes;
```
📌 Retorna apenas os nomes e e-mails dos clientes.  

🔹 Exemplo 3 — Renomeando colunas (alias):  
```sql
SELECT nome AS nome_cliente, email AS email_cliente
FROM clientes;
```
📌 Melhora a legibilidade do resultado, especialmente em relatórios.  

🔹 Exemplo 4 — Consulta com limite de registros:  
```sql
SELECT *
FROM pedidos
LIMIT 10;
```
📌 Retorna apenas os 10 primeiros registros (útil para inspeção rápida).  

🔹 Exemplo 5 — Removendo duplicidades: 
```sql
SELECT DISTINCT cidade
FROM clientes;
``` 
📌 Retorna apenas valores únicos da coluna cidade.  

## ⚠️ Erros comuns / armadilhas:  

❌ Usar SELECT * sem necessidade.  
❌ Consultar tabelas erradas por nomes semelhantes.  
❌ Não limitar consultas em tabelas grandes.  
❌ Confundir alias com nome real da coluna.  
❌ Esquecer que SQL é sensível à estrutura do banco.  

## ✅ Boas práticas:  

✔️ Selecione apenas as colunas necessárias.  
✔️ Use alias para deixar o resultado mais claro.  
✔️ Teste consultas com LIMIT antes de rodar em produção.  
✔️ Leia os dados antes de alterá-los.  
✔️ Padronize formatação do SQL.  

### 📝 Observações:  

SELECT * é útil para exploração inicial, mas não para produção.  

Alias não altera a estrutura da tabela, apenas o resultado.  

O desempenho das consultas depende muito do volume de dados.  

Consultas simples bem feitas evitam erros mais à frente.  

## 🌍 Ligação com o mundo real:  

Consultas básicas são usadas constantemente em:

Análise de dados.  
Validação de informações.  
Suporte técnico.  
Monitoramento de sistemas.  
Criação de relatórios simples.  

Dominar SELECT é o primeiro grande passo para:  
Trabalhar com dados. 
Evoluir para joins e agregações.  
Resolver problemas reais com SQL.