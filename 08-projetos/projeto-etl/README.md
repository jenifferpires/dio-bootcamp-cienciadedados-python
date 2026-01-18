# Projeto ETL com IA Generativa – Bootcamp Santander DIO.

## 📌 Contexto: 

Este projeto foi desenvolvido como parte do **Bootcamp Santander 2025 – Ciência de Dados com Python**, promovido pela **Digital Innovation One (DIO)**.  
O desafio tem como objetivo aplicar, de forma prática, os conceitos fundamentais de **ETL (Extract, Transform, Load)**, integrando **Python**, **manipulação de dados** e **Inteligência Artificial Generativa** em um cenário inspirado em problemas reais do mercado.

Ao longo do bootcamp, foram abordados temas como:
- Fundamentos de Python
- Manipulação e análise de dados
- Bancos de dados SQL e NoSQL
- Conceitos de ETL
- Boas práticas de versionamento com Git e GitHub
- Aplicações práticas de Ciência de Dados

Este projeto consolida esses aprendizados em uma solução prática e organizada.

---

## 🎯 Objetivo do Projeto: 

Construir um **pipeline ETL completo** utilizando Python, simulando um fluxo de dados onde:

1. Dados de usuários são **extraídos** a partir de um arquivo CSV  
2. Esses dados são **transformados** com o apoio de IA Generativa para criação de mensagens personalizadas  
3. Os dados transformados são **carregados** em um novo arquivo, representando a entrega final do pipeline  

O foco principal não está na ferramenta em si, mas no **entendimento do fluxo de dados entre as etapas do ETL**, conforme proposto no desafio.

---

## 🧩 Descrição do Pipeline ETL: 

### 🔹 Extract (Extração)
Os dados dos usuários são extraídos de um arquivo CSV contendo informações básicas como:
- Identificador do usuário
- Nome
- Conta
- Cartão (mascarado)

Essa etapa simula a obtenção de dados a partir de uma fonte externa, como APIs ou bases de dados.

### 🔹 Transform (Transformação): 
Na etapa de transformação, os dados extraídos são enriquecidos com **mensagens personalizadas de marketing**, simulando o uso de **IA Generativa (ChatGPT/OpenAI)**.

Devido à possível indisponibilidade da API utilizada no desafio original, foi adotada uma abordagem alternativa, conforme sugerido no próprio desafio, mantendo o foco no aprendizado de Python e ETL.

### 🔹 Load (Carregamento)
Por fim, os dados transformados são salvos em um novo arquivo CSV, representando o carregamento das informações para consumo posterior por outros sistemas ou análises.

---

## 🗂️ Estrutura do Projeto: 

```text
projeto-etl/
│
├── README.md
│
├── etl_ia_pipeline/
│   ├── README.md
│   ├── requirements.txt
│   ├── main.py
│   │
│   ├── data/
│   │   ├── input/
│   │   │   └── users.csv
│   │   └── output/
│   │       └── mensagens_marketing.csv
│   │
│   ├── extract/
│   │   └── extract_users.py
│   │
│   ├── transform/
│   │   └── generate_messages.py
│   │
│   └── load/
│       └── save_results.py
│
└── .gitignore
```
Essa organização reflete boas práticas de projetos em Python e facilita a compreensão do fluxo ETL.

### ▶️ Como Executar o Projeto: 

Clone este repositório: 

```bash
git clone https://github.com/jenifferpires/dio-bootcamp-cienciadedados-python.git
```

Acesse a pasta do projeto:
```bash 
cd 08-projetos/projeto-etl/etl_ia_pipeline
```

Instale as dependências:
```bash 
pip install -r requirements.txt
```

Execute o pipeline ETL:
```bash 
python main.py
```

Ao final da execução, o arquivo com as mensagens geradas estará disponível em:
```bash 
data/output/mensagens_marketing.csv
```

## 📚 Aprendizados Consolidado neste Projeto:  

Estruturação de um pipeline ETL completo. 
Leitura e escrita de arquivos CSV com Python. 
Organização de projetos em camadas (Extract, Transform, Load).  
Simulação de uso de IA Generativa aplicada a dados. 
Boas práticas de versionamento com Git e GitHub. 

Desenvolvimento de projetos com foco educacional e colaborativo

#### 🤝 Considerações Finais: 

Este projeto faz parte de um repositório maior, construído ao longo do Bootcamp Santander DIO, e tem caráter educacional, servindo como evidência prática do aprendizado adquirido durante a jornada de formação em Ciência de Dados.