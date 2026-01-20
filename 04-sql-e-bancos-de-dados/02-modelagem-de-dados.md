# 📌 Modelagem de Dados.

## 📖 Introdução: 
Modelagem de dados é o processo de **organizar e estruturar informações** de forma lógica antes de armazená-las em um banco de dados.  
Uma boa modelagem garante **consistência, desempenho, escalabilidade e facilidade de manutenção**.

Em outras palavras:  
👉 **um banco bem modelado evita retrabalho, erros e dados duplicados.**

---

## 🎯 Quando usar no dia a dia?  
A modelagem de dados é usada quando:  

- Criamos um banco de dados do zero.  
- Precisamos entender dados de um sistema legado.  
- Vamos integrar sistemas diferentes.  
- Precisamos garantir integridade e qualidade dos dados.  
- Projetamos relatórios e análises confiáveis.  
- Estruturamos dados para aplicações, APIs ou pipelines.  

---

## 🧠 Conceito:  
Modelar dados significa definir:  

- **Entidades** → o que será armazenado (tabelas).  
- **Atributos** → características das entidades (colunas).  
- **Relacionamentos** → como as entidades se conectam.  
- **Regras** → o que é obrigatório, único ou permitido.  

### 🔹 Entidades:  
Representam objetos do mundo real.

Exemplos:
- Cliente
- Pedido
- Produto
- Pagamento

Cada entidade normalmente vira uma **tabela** no banco.

---

### 🔹 Atributos:  
São as propriedades de uma entidade.

Exemplo — entidade `cliente`:
- id_cliente
- nome
- email
- data_cadastro

Cada atributo vira uma **coluna**.

---

### 🔹 Chave Primária (Primary Key):  
Identifica **unicamente** cada registro da tabela.

Exemplo:
```text
id_cliente
```
Regras:

Não pode ser nula. 
Não pode se repetir.  
Deve ser estável. 

### 🔹 Chave Estrangeira (Foreign Key). 

Cria o relacionamento entre tabelas.

Exemplo:

Um pedido pertence a um cliente. 
```text
pedido.id_cliente → cliente.id_cliente
```
### 🔹 Relacionamentos: 

Os principais tipos são:

*  `1 : 1` → um para um

* `1 : N` → um para muitos

* `N : N` → muitos para muitos (exige tabela intermediária). 

Exemplo:

* Um cliente pode ter vários pedidos → `1:N`.

## 🧪 Exemplos práticos: 
#### 🔹 Exemplo 1 — Tabela de clientes. 
```sql
CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100),
    data_cadastro DATE
);
```

#### 🔹 Exemplo 2 — Tabela de pedidos com relacionamento.
```sql
CREATE TABLE pedidos (
    id_pedido INT PRIMARY KEY,
    id_cliente INT,
    valor_total DECIMAL(10,2),
    data_pedido DATE,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);
```
📌 Aqui temos:

Chave primária em `id_pedido`
Chave estrangeira ligando pedido ao cliente.

### ⚠️ Erros comuns / armadilhas:

❌ Criar tabelas sem chave primária.  
❌ Misturar informações diferentes em uma única tabela.  
❌ Duplicar dados desnecessariamente.  
❌ Ignorar relacionamentos entre entidades.  
❌ Não pensar em crescimento futuro.  

### ✅ Boas práticas:  

✔️ Normalizar dados (evitar duplicidade).  
✔️ Usar nomes claros e padronizados.  
✔️ Definir chaves primárias corretamente.  
✔️ Criar relacionamentos explícitos.  
✔️ Pensar primeiro no modelo, depois no SQL.  

#### 📝 Observações:  

Modelagem vem antes das consultas SQL.  

Alterar um modelo ruim depois costuma ser caro.  

Diagramas (DER) ajudam muito no entendimento.  

Nem sempre o modelo perfeito existe — existe o modelo adequado ao contexto.  

### 🌍 Ligação com o mundo real. 

Modelagem de dados é fundamental em:

Sistemas corporativos.  
ERPs e CRMs.  
Bancos financeiros.  
Plataformas de e-commerce.  
Pipelines de dados e BI.  

Dominar modelagem demonstra:
Visão sistêmica.  
Organização lógica.  
Capacidade de antecipar problemas.  
Maturidade técnica. 