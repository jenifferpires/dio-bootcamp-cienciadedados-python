# 🗄️ Módulo 04 — SQL e Bancos de Dados.  

## 📖 Introdução:  
Este módulo introduz os **fundamentos de SQL e bancos de dados relacionais**, essenciais para armazenar, consultar, analisar e transformar dados de forma estruturada.  

SQL é a linguagem padrão para comunicação com bancos de dados e está presente em praticamente todos os ambientes corporativos, produtos digitais e pipelines de dados. 

---

## 🎯 Quando usar no dia a dia?  
SQL é utilizado constantemente em cenários como:

- Consulta e análise de dados.  
- Criação de relatórios e dashboards.  
- Integração de sistemas.  
- Validação de informações.  
- Construção de pipelines de dados.  
- Suporte à tomada de decisão.  

---

## 🧠 Conceitos abordados no módulo:  

### 🔹 Bancos de Dados Relacionais:  
Estruturam dados em **tabelas**, compostas por linhas e colunas, com relações bem definidas.

Exemplos comuns:
- MySQL
- PostgreSQL
- SQL Server
- Oracle
- SQLite

---

### 🔹 SQL (Structured Query Language).  
Linguagem usada para:  
- Consultar dados (`SELECT`)
- Inserir dados (`INSERT`)
- Atualizar dados (`UPDATE`)
- Remover dados (`DELETE`)
- Definir estruturas (`CREATE`, `ALTER`, `DROP`)

---

### 🔹 Modelagem de Dados
Processo de definir:
- Entidades (tabelas)
- Atributos (colunas)
- Relacionamentos
- Chaves primárias e estrangeiras

---

## 🧪 Exemplos práticos

### 🔸 Consulta simples
```sql
SELECT nome, email
FROM clientes;
```
📌 Retorna os nomes e e-mails da tabela clientes.  

#### 🔸 Filtro com condição: 
```sql
SELECT *
FROM pedidos
WHERE valor_total > 1000;
```
📌 Retorna pedidos acima de um determinado valor.  

#### 🔸 Ordenação:
```sql
SELECT *
FROM produtos
ORDER BY preco DESC;
```
📌 Lista produtos do mais caro para o mais barato.  

### ⚠️ Erros comuns / armadilhas:  

❌ Usar SELECT * sem necessidade.  
❌ Esquecer filtros em consultas grandes.  
❌ Não entender o impacto de JOIN incorreto.  
❌ Misturar lógica de negócio direto no SQL.  
❌ Não validar dados antes de atualizar ou deletar.  

### ✅ Boas práticas:  

✔️ Selecionar apenas as colunas necessárias.  
✔️ Usar aliases para melhorar legibilidade.  
✔️ Testar consultas com SELECT antes de UPDATE ou DELETE.  
✔️ Entender bem os relacionamentos entre tabelas.  
✔️ Documentar consultas complexas.  

### 🌍 Ligação com o mundo real:  

SQL é essencial em:

Análise de dados.  
Engenharia de dados.  
Ciência de dados.  
Backend e APIs.  
Sistemas corporativos.  

Dominar SQL demonstra: 

Capacidade analítica.  
Organização lógica.  
Leitura e interpretação de dados.  
Maturidade técnica para ambientes profissionais.  

#### 📌 Conteúdos deste módulo:  

`01-o-que-e-sql.md`

`02-modelagem-de-dados.md` 

`03-consultas-basicas.md`  

`04-filtros-e-ordenacao.md`

`05-joins.md`

`06-agrupamentos-e-funcoes.md`

`07-subqueries-e-views.md`

`08-boas-praticas-sql.md`

### 🧾 Observação final:  
SQL não é apenas uma linguagem de consulta — é uma ferramenta estratégica para transformar dados em decisões.
