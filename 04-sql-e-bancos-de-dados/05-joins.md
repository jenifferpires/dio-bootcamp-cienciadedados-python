# 📌 Joins em SQL.  

## 📖 Introdução:  
Joins são utilizados para **combinar dados de duas ou mais tabelas** em uma única consulta.
Eles são fundamentais em bancos de dados relacionais, pois permitem analisar informações que estão distribuídas entre tabelas relacionadas.

Sem joins, os dados ficam isolados e perdem valor analítico.  

---

## 🎯 Como usar no dia a dia?
Você utiliza joins quando precisa:

- Relacionar clientes com pedidos.
- Cruzar produtos com vendas.
- Unir dados financeiros e cadastrais.
- Construir relatórios completos.
- Analisar informações que dependem de múltiplas tabelas.

---

## 🧠 Conceito.  
Um join funciona a partir de **uma condição de relacionamento**, geralmente baseada em:

- Chave primária de uma tabela.
- Chave estrangeira de outra tabela.

A cláusula central é o `ON`, que define **como as tabelas se conectam**.

---

## 🧩 Tipos de JOIN.  

### 🔹 INNER JOIN:  
Retorna apenas os registros que existem **nas duas tabelas**.

```sql
SELECT c.nome, p.valor_total
FROM clientes c
INNER JOIN pedidos p
    ON p.id_cliente = c.id_cliente;
```
Explicação:  
📌Retorna somente clientes que possuem pedidos associados.

#### 🔹 LEFT JOIN
Retorna todos os registros da tabela da esquerda e os correspondentes da direita.
Quando não houver correspondência, os valores da direita serão NULL.

```sql
SELECT c.nome, p.valor_total
FROM clientes c
LEFT JOIN pedidos p
    ON p.id_cliente = c.id_cliente;
```
Explicação:  
📌Retorna todos os clientes, mesmo aqueles sem pedidos.  

#### 🔹 RIGHT JOIN
Retorna todos os registros da tabela da direita e os correspondentes da esquerda.  

```sql
SELECT c.nome, p.valor_total
FROM clientes c
RIGHT JOIN pedidos p
    ON p.id_cliente = c.id_cliente;
```     
Explicação:  
📌Retorna todos os pedidos, mesmo que não exista um cliente associado.

#### 🔹 FULL JOIN
Retorna todos os registros de ambas as tabelas.  
Quando não houver correspondência, os campos ficam como NULL.  

```sql
SELECT c.nome, p.valor_total
FROM clientes c
FULL JOIN pedidos p
    ON p.id_cliente = c.id_cliente;
```
Explicação:  
📌Combina todos os clientes e pedidos, associados ou não.  

## 🧪 Exemplos práticos: 
#### 🔹 Join com filtro.  
```sql
SELECT c.nome, p.valor_total
FROM clientes c
INNER JOIN pedidos p
    ON p.id_cliente = c.id_cliente
WHERE p.valor_total > 1000;
``` 
Explicação:  
📌Retorna clientes com pedidos acima de 1000.  

#### 🔹 Join com ordenação.  
```sql
SELECT c.nome, p.data_pedido
FROM clientes c
INNER JOIN pedidos p
    ON p.id_cliente = c.id_cliente
ORDER BY p.data_pedido DESC;
```
Explicação:  
📌Lista pedidos do mais recente para o mais antigo.  

## ⚠️ Erros comuns: 

Esquecer a condição do ON.  
Usar INNER JOIN quando deveria usar LEFT JOIN.  
Criar joins sem entender a cardinalidade.  
Gerar duplicidade de registros sem perceber.  
Usar nomes de colunas sem alias em joins complexos.  

## ✅ Boas práticas:  
Sempre use alias para tabelas.  
Entenda o relacionamento antes de escrever o join.  
Valide o resultado com poucos registros.  
Evite joins desnecessários.  
Prefira clareza à complexidade.  

### 🌍 Ligação com o mundo real:  
Joins são amplamente usados em relatórios corporativos, análises de negócio, BI e pipelines de dados.  
Dominar joins significa saber conectar informações, transformar dados brutos em conhecimento e evitar análises incorretas.  