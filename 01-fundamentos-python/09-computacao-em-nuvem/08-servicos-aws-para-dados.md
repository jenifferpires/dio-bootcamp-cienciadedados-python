# 📊 Serviços AWS para Dados.  

A AWS oferece um conjunto robusto de serviços voltados para **armazenamento, processamento, análise e visualização de dados**.  
Esses serviços permitem construir arquiteturas escaláveis para **engenharia de dados, analytics e Machine Learning**.

Neste conteúdo, o foco é compreender **quais serviços são mais utilizados na área de dados** e em quais cenários cada um se encaixa.

---

## 🎯 Objetivo desta etapa:  

- Conhecer os principais serviços AWS voltados para dados.  
- Entender o papel de cada serviço em arquiteturas de dados.  
- Relacionar serviços AWS com pipelines e análises.  
- Criar visão de arquitetura orientada a dados.  

---

## 🗄️ Armazenamento de dados.  

### 🪣 Amazon S3 (Simple Storage Service):  

O **Amazon S3** é o serviço de armazenamento de objetos da AWS.

**Principais usos:**
- Data lakes
- Armazenamento de dados brutos
- Backups
- Logs
- Arquivos para análise

📌 É um dos serviços mais utilizados em projetos de dados.

---

## 🧠 Bancos de dados na AWS.  

### 🗃️ Amazon RDS:  

Serviço de banco de dados relacional gerenciado.

**Usos comuns:**
- Dados transacionais
- Bases estruturadas
- Aplicações analíticas leves

---

### 📦 Amazon DynamoDB:  

Banco de dados NoSQL totalmente gerenciado.

**Usos comuns:**
- Dados de alta escala
- Baixa latência
- Estruturas flexíveis

---

## ⚙️ Processamento de dados.  

### 🔄 AWS Glue:  

Serviço gerenciado para **ETL e catalogação de dados**.

**Principais funções:**
- Transformação de dados
- Catálogo de metadados
- Integração com S3 e outros serviços

📌 Muito utilizado em pipelines de engenharia de dados.

---

### ⚡ Amazon EMR:  

Plataforma para processamento distribuído.

**Usos comuns:**
- Big Data
- Processamento em larga escala
- Frameworks como Spark e Hadoop

---

## 📈 Análise de dados.  

### 🔍 Amazon Athena:  

Permite consultar dados diretamente no S3 usando SQL.

**Principais vantagens:**
- Sem necessidade de servidor
- Consulta sob demanda
- Ideal para análises exploratórias

---

### 📊 Amazon Redshift:  

Data warehouse da AWS.

**Usos comuns:**
- Análises analíticas complexas
- Grandes volumes de dados
- BI e relatórios corporativos

---

## 🤖 Machine Learning e Analytics avançado.

### 🧠 Amazon SageMaker:  

Plataforma completa para Machine Learning.

**Permite:**
- Treinar modelos
- Testar algoritmos
- Implantar modelos em produção

---

## ⚠️ Pontos de atenção.  

Ao trabalhar com serviços AWS para dados:

- Custos variam conforme uso.  
- Integração entre serviços exige planejamento.  
- Segurança e controle de acesso são fundamentais. 
- Monitoramento deve ser contínuo.  

---

## ✅ Boas práticas:  

- Utilizar S3 como base do data lake.  
- Separar ambientes (dev, test, prod).  
- Monitorar custos e desempenho.  
- Documentar arquitetura de dados.  
- Usar serviços gerenciados sempre que possível.  

---

## 🌍 Aplicação no mundo real.  

Esses serviços são utilizados em:

- Plataformas de dados corporativas.  
- Engenharia de dados em cloud.  
- Análises em larga escala.  
- Machine Learning em produção.  
- Dashboards e BI.  

Conhecer esses serviços permite desenhar **arquiteturas modernas e escaláveis**.

---

## 🧾 Observações finais:  

A AWS oferece flexibilidade para criar soluções de dados sob medida.  
O segredo está em **escolher os serviços certos para cada problema**, equilibrando custo, desempenho e simplicidade.  

Arquitetura de dados é decisão estratégica.  
