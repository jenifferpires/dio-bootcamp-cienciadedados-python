# 📌 Boas Práticas em SQL. 

## 📖 Introdução:  
Boas práticas em SQL garantem consultas mais claras, seguras, performáticas e fáceis de manter.
Elas são essenciais para evitar erros críticos, melhorar a leitura do código e garantir que o banco de dados seja usado de forma eficiente.

SQL bem escrito não é apenas funcional, é confiável.

---

## 🎯 Como usar no dia a dia?
Você deve aplicar boas práticas em SQL quando:

- Escreve consultas para produção.
- Cria relatórios e dashboards.
- Trabalha com grandes volumes de dados.
- Compartilha consultas com outros times.
- Dá manutenção em código SQL existente.

---

## 🧠 Conceito.  
Boas práticas em SQL envolvem três pilares principais:

- **Legibilidade**: facilitar a leitura e entendimento.
- **Segurança**: evitar alterações ou vazamentos indevidos.
- **Performance**: reduzir custo de processamento.

Esses pilares devem ser considerados em qualquer consulta, simples ou complexa.

---

## 🧪 Exemplos práticos:  

### 🔹 Selecionar apenas colunas necessárias.  
```sql
SELECT nome, email
FROM clientes;
```
Explicação:  
📌Evita tráfego e processamento desnecessários causados por `SELECT *`.  

### 🔹 Validar antes de atualizar:  
```sql
SELECT *
FROM pedidos
WHERE status = 'PENDENTE';
```
```sql
UPDATE pedidos
SET status = 'CANCELADO'
WHERE status = 'PENDENTE';
```

Explicação:  
📌O `SELECT` permite validar o impacto antes do `UPDATE`.  

### 🔹 Usar alias para clareza:  
```sql
SELECT c.nome, p.valor_total
FROM clientes c
INNER JOIN pedidos p
    ON p.id_cliente = c.id_cliente;
```
Explicação:  
📌Alias tornam consultas com joins mais legíveis.  

### 🔹 Padronizar formatação:  
```sql
SELECT
    status,
    COUNT(*) AS total
FROM pedidos
GROUP BY status
ORDER BY total DESC;
```
Explicação:  
📌Consultas bem formatadas facilitam leitura e manutenção.  

## ⚠️ Erros comuns:  

Usar `SELECT *` em produção.  
Executar `UPDATE` ou `DELETE` sem `WHERE`.  
Não testar consultas antes de rodar em produção.  
Ignorar impacto de performance.  
Escrever SQL difícil de entender.  

## ✅ Boas práticas recomendadas:  

Use nomes claros para tabelas e colunas.  
Prefira clareza à “consulta curta”.  
Teste consultas com poucos dados antes.  
Use alias de forma consistente.  
Documente SQLs complexos.  
Revise queries críticas antes de executá-las.  

### 📝 Observações:  

Pequenas boas práticas evitam grandes problemas.  
SQL legível reduz dependência de quem escreveu.  
Performance importa, mas clareza vem primeiro.  
Segurança deve ser sempre considerada.  

## 🌍 Ligação com o mundo real:  

Em ambientes corporativos, SQL mal escrito pode causar:

Relatórios incorretos.  
Lentidão em sistemas.  
Incidentes em produção.  
Perda de confiança nos dados.  

Aplicar boas práticas demonstra maturidade técnica, responsabilidade e preparo para trabalhar com dados em ambientes profissionais.  


