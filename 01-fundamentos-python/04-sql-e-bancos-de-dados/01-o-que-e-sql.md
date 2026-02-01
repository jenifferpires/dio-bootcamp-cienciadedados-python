# 📌 O que é SQL?

## 📖 Introdução: 
SQL (Structured Query Language) é a linguagem padrão para **consultar e manipular dados** em bancos de dados relacionais.  
Com SQL, conseguimos **buscar informações**, **filtrar resultados**, **organizar dados** e também **inserir/atualizar/remover registros**.

SQL é uma habilidade essencial para áreas como **Dados, Backend, BI e Produto**, porque a maior parte das empresas armazena dados em bancos relacionais.

---

## 🎯 Quando usar no dia a dia? 
Você usa SQL quando precisa:

- Consultar dados para relatórios ou análises.   
- Validar informações (ex: pedidos duplicados, valores inconsistentes).   
- Extrair dados para dashboards (Power BI, Looker, Tableau).   
- Investigar problemas em produção (ex: falha em cadastro, pedido não criado).   
- Cruzar dados de tabelas relacionadas (clientes x pedidos).   
- Preparar dados para pipelines (ETL/ELT).    

---

## 🧠 Conceito:  
SQL é uma linguagem declarativa: você descreve **o que quer** e o banco decide **como obter**.

Em bancos relacionais, os dados ficam em **tabelas** (linhas e colunas).  

O SQL permite trabalhar nesses dados com comandos agrupados em categorias:  

### 🔹 DQL — Data Query Language (Consulta):   
- `SELECT` (buscar dados)

### 🔹 DML — Data Manipulation Language (Manipulação):   
- `INSERT` (inserir)
- `UPDATE` (atualizar)
- `DELETE` (remover)

### 🔹 DDL — Data Definition Language (Definição de estrutura):  
- `CREATE` (criar tabela, view…)
- `ALTER` (alterar estrutura)
- `DROP` (remover estrutura)

### 🔹 DCL — Data Control Language (Permissões):  
- `GRANT` (conceder)
- `REVOKE` (revogar)

> 📌 Na prática do dia a dia, o mais usado inicialmente é `SELECT`.

---

## 🧪 Exemplos práticos:  

### 🔹 Exemplo 1 — Buscar dados (SELECT):  
```sql
SELECT nome, email
FROM clientes;
```

✅ Retorna apenas as colunas nome e email da tabela clientes.

### 🔹 Exemplo 2 — Buscar com filtro (WHERE):
```sql
SELECT id_pedido, valor_total
FROM pedidos
WHERE valor_total > 1000;
```
✅ Retorna pedidos com valor acima de 1000.  

### 🔹 Exemplo 3 — Ordenar resultados (ORDER BY):  
```sql
SELECT nome, preco
FROM produtos
ORDER BY preco DESC;
```
✅ Lista produtos do mais caro para o mais barato.  

### 🔹 Exemplo 4 — Inserir dados (INSERT):  
```sql
INSERT INTO clientes (nome, email)
VALUES ('Ana Souza', 'ana@email.com');
```
✅ Insere um novo registro na tabela clientes.  

## ⚠️ Erros comuns / armadilhas: 

❌ Usar SELECT * sempre (traz colunas desnecessárias e pode pesar performance).  
❌ Esquecer o WHERE em UPDATE/DELETE (risco de alterar/remover tudo).  
❌ Não entender diferença entre NULL e string vazia.  
❌ Confundir INNER JOIN com LEFT JOIN e gerar resultados errados.  
❌ Rodar comandos em produção sem validar antes.  

## ✅ Boas práticas:  

✔️ Prefira selecionar colunas específicas ao invés de SELECT *.  
✔️ Antes de UPDATE ou DELETE, faça um SELECT com o mesmo WHERE.  
✔️ Use aliases para melhorar legibilidade:
```sql
SELECT c.nome, p.valor_total
FROM clientes c
JOIN pedidos p ON p.id_cliente = c.id;
```

✔️ Padronize nomes e formatação do SQL (facilita manutenção)  
✔️ Tenha cuidado com dados sensíveis (LGPD)  

### 📝 Observações:  

SQL varia um pouco entre bancos (MySQL, PostgreSQL, SQL Server), mas os fundamentos são praticamente os mesmos.    
Saber SQL não é decorar comandos — é entender lógica de consulta e relacionamento entre tabelas.      

Se você domina **SELECT**, **WHERE**, **JOIN** e **GROUP BY**, você já resolve grande parte do mundo real.

### 🌍 Ligação com o mundo real:  

No dia a dia, SQL é ferramenta central para:

investigar bugs e inconsistências.  
Gerar relatórios de negócio.  
Montar pipelines de dados.  
Apoiar decisões com dados reais.  

Em entrevistas, SQL costuma ser avaliado por:

clareza do raciocínio.  

domínio de joins e agregações.  

cuidado com performance e filtros.  

atenção a detalhes (NULL, duplicidade, cardinalidade).  