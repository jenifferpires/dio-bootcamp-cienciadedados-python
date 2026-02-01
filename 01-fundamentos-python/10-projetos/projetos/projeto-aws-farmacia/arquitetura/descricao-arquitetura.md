# 🏗️ Descrição da Arquitetura AWS — Farmácia Virtual. 

## 📌 Visão Geral:  

A arquitetura proposta foi desenhada para suportar uma **plataforma de farmácia virtual**, permitindo acesso de clientes via navegador, processamento de pedidos e armazenamento seguro de dados.

O foco principal é:
- Baixo custo inicial
- Escalabilidade sob demanda
- Serviços gerenciados
- Facilidade de manutenção

---

## 🧱 Componentes da Arquitetura:  

### 🌐 Frontend
- **Amazon S3 + CloudFront**
- Hospedagem de site estático
- Alta disponibilidade e baixo custo

### ⚙️ Backend
- **AWS Lambda**
- Execução sob demanda
- Redução de custos com servidores ociosos

### 🔄 API
- **Amazon API Gateway**
- Gerenciamento de endpoints REST
- Controle de autenticação e requisições

### 🗄️ Banco de Dados
- **Amazon DynamoDB**
- Banco NoSQL totalmente gerenciado
- Escalável e com pagamento por uso

### 📊 Monitoramento:  
- **Amazon CloudWatch**
- Monitoramento de logs, métricas e alarmes

---

## 🔐 Segurança:  

- Controle de acesso via IAM
- Princípio do menor privilégio
- Comunicação segura entre serviços

---

## 📈 Escalabilidade:  

A arquitetura é **altamente escalável**, permitindo crescimento automático conforme aumento da demanda, sem necessidade de reconfiguração manual.

---  

## 🖼️ Diagrama da Arquitetura:   

O diagrama abaixo representa visualmente a arquitetura proposta para a farmácia virtual na AWS, evidenciando o fluxo de dados, os serviços utilizados e sua integração.    

📄 Arquivo: `arquitetura/diagrama.png`  

`📊 Infográfico — Projeto Final AWS (Resumo Visual)`: 
```text
👤 Usuário
   │
   ▼
🌐 CloudFront
   │  (CDN | performance + custo)
   ▼
🗂 Amazon S3
   │  (Frontend estático | baixo custo)
   ▼
🔌 API Gateway
   │  (Entrada segura de requisições)
   ▼
⚙️ AWS Lambda
   │  (Backend serverless | paga por uso)
   ▼
🗄 DynamoDB
   │  (Banco NoSQL escalável)
   ▼
📈 CloudWatch
   (Logs, métricas e monitoramento)
```

---

## 📝 Considerações Finais:  
 
Essa arquitetura atende ao cenário proposto de uma farmácia virtual de pequeno a médio porte, com possibilidade de evolução futura.  

