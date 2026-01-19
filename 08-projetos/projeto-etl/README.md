# 📊 Projeto ETL com IA Generativa (Bootcamp DIO). 

## 📌 Visão Geral: 

Este projeto foi desenvolvido como parte do **Bootcamp de Ciência de Dados com Python da DIO**, com o objetivo de aplicar, de forma prática e didática, os conceitos fundamentais de **ETL (Extract, Transform, Load)** aliados ao uso **simulado de IA Generativa**.

A solução implementa um pipeline completo capaz de:

* Extrair dados de usuários a partir de um arquivo CSV.  
* Transformar esses dados, gerando mensagens personalizadas de marketing com apoio de lógica inspirada em IA Generativa.  
* Carregar o resultado final em um novo arquivo CSV.  

O projeto possui caráter **acadêmico, colaborativo e demonstrativo**, sendo voltado tanto para aprendizado quanto para portfólio.

---

## 🎯 Objetivo do Projeto:  

* Consolidar o entendimento do processo ETL.  
* Aplicar boas práticas de organização de código em Python.  
* Simular o uso de IA Generativa em um contexto de negócio.  
* Atender integralmente aos requisitos do desafio proposto no bootcamp.  

---

## 🧠 Conceitos Abordados no Bootcamp:  

* Fundamentos de Python.  
* Manipulação de dados com Pandas.  
* Estruturação de projetos em Python.  
* Pipeline ETL (Extract, Transform, Load).  
* Separação de responsabilidades.  
* Versionamento de código com Git e GitHub.  
* Boas práticas para projetos acadêmicos.  

---

## 🗂️ Estrutura do Projeto:  

```text
etl_ia_pipeline/
│
├── README.md
├── requirements.txt
├── main.py
│
├── data/
│   ├── input/
│   │   └── users.csv
│   └── output/
│       └── mensagens_marketing.csv
│
├── extract/
│   └── extract_users.py
│
├── transform/
│   └── generate_messages.py
│
└── load/
    └── save_results.py
```

---

## 🔄 Descrição do Pipeline ETL:  

### 1️⃣ Extract – Extração dos Dados.  

Responsável por:

* Ler o arquivo `users.csv`
* Validar a existência e o formato dos dados
* Retornar um DataFrame com as informações dos usuários

📄 Arquivo:

```text
extract/extract_users.py
```

---

### 2️⃣ Transform – Transformação com IA Generativa (Simulada).  

Responsável por:

* Processar os dados extraídos  
* Gerar mensagens personalizadas de marketing  
* Simular o uso de IA Generativa com base em regras e templates  

📄 Arquivo:

```text
transform/generate_messages.py
```

📌 Observação:

> O uso de IA Generativa é **simulado**, conforme escopo do desafio, não sendo utilizada nenhuma API externa.

---

### 3️⃣ Load – Carregamento dos Dados.  

Responsável por:

* Receber os dados transformados
* Persistir o resultado final no arquivo `mensagens_marketing.csv`

📄 Arquivo:

```text
load/save_results.py
```

---

## ▶️ Execução do Projeto.  

### Pré-requisitos:  

* Python 3.8+
* Biblioteca Pandas

### Instalação das dependências:  

```bash
pip install -r requirements.txt
```

### Execução do pipeline:  

No diretório `etl_ia_pipeline`, execute:

```bash
python main.py
```

---

## 📄 Resultado Esperado:  

Após a execução, será gerado o arquivo:

```text
data/output/mensagens_marketing.csv
```

Contendo:

* Dados dos usuários
* Mensagens personalizadas geradas

---

## 🧪 Exemplo de Saída:  

```csv
user_id,nome,conta,cartao,mensagem
1,Ana Silva,12345-6,**** 4321,"Olá Ana Silva, investir é uma excelente forma de planejar o seu futuro financeiro. Conte com o Santander para te apoiar nessa jornada!"
```

---

## 📚 Considerações Finais:  

Este projeto cumpre integralmente os objetivos propostos pelo desafio, demonstrando:

* Entendimento prático de pipelines ETL
* Organização e modularização de código
* Aplicação de conceitos aprendidos no bootcamp
* Clareza e didática na implementação

Trata-se de um projeto **educacional**, mas com estrutura próxima à utilizada em cenários reais de engenharia de dados.

---

## 👩‍💻 Autora:  

**Jeniffer Pires**
Projeto desenvolvido no contexto do **Bootcamp DIO – Ciência de Dados com Python**

---

## 🔗 Referências:  

* [DIO – Digital Innovation One](https://www.dio.me)
* Documentação oficial do Pandas
