# Pipeline ETL com IA Generativa – Implementação Técnica.  

## 📌 Visão Geral:  

Este módulo contém a implementação técnica do **pipeline ETL (Extract, Transform, Load)** desenvolvido como parte do desafio **Explorando IA Generativa em um Pipeline de ETL com Python**, do **Bootcamp Santander 2025 – Ciência de Dados com Python (DIO)**.

O pipeline foi construído de forma modular, separando claramente cada etapa do processo, seguindo boas práticas de organização de código e facilitando a leitura, manutenção e reaproveitamento.

---

## 🧠 Arquitetura do Pipeline:  

O fluxo do pipeline segue a seguinte ordem:

Arquivo CSV (dados brutos).   
↓
[Extract] Leitura dos dados.   
↓
[Transform] Geração de mensagens com IA Generativa (simulada).  
↓
[Load] Persistência dos dados transformados.  

Cada etapa está isolada em seu respectivo módulo.

## 🗂️ Estrutura Técnica:  

```text
etl_ia_pipeline/
│
├── main.py
├── requirements.txt
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

### 🔹 Etapa 1 – Extract (Extração):  

Arquivo: `extract/extract_users.py`  

Responsável por extrair os dados dos usuários a partir de um arquivo CSV.

**Função principal:** 

Ler os dados da fonte.    
Retornar os dados em uma estrutura manipulável `(DataFrame)`.  
Essa etapa simula a extração de dados a partir de uma API ou base externa, conforme apresentado nas aulas do bootcamp.  

### 🔹 Etapa 2 – Transform (Transformação):  

Arquivo: `transform/generate_messages.py` 

Nesta etapa ocorre o enriquecimento dos dados com mensagens personalizadas, simulando o uso de IA Generativa para marketing direcionado.  

O que acontece nesta fase:  

Cada usuário recebe uma mensagem personalizada.  
A lógica simula chamadas a uma IA (ChatGPT/OpenAI).   
A abordagem segue a orientação do desafio para casos em que a API esteja indisponível.  

O foco está no conceito de transformação de dados, e não na dependência de uma ferramenta externa.

### 🔹 Etapa 3 – Load (Carregamento):  

Arquivo: `load/save_results.py`

Responsável por persistir os dados transformados em um novo arquivo CSV.  

**Objetivo:**   

Salvar os dados finais.  
Representar a entrega do pipeline ETL.  
Simular o carregamento em um sistema de destino.  

### 🔹 Orquestração do Pipeline:  

Arquivo:`main.py`

O arquivo `main.py` é o ponto de entrada do projeto e tem como função:

Executar a etapa de extração.   

Encaminhar os dados para transformação.  

Finalizar com o carregamento dos dados.  

Essa separação reflete uma prática comum em pipelines reais de dados.  

**⚙️ Dependências:** 

As dependências do projeto estão listadas no arquivo `requirements.txt`.  

Atualmente, o projeto utiliza:  

`pandas` para manipulação de dados tabulares

#### ▶️ Execução do Pipeline:

A execução do pipeline é feita a partir do diretório `etl_ia_pipeline`:
```bash
python main.py
```

Após a execução, o arquivo de saída estará disponível em:
```bash
data/output/mensagens_marketing.csv
```


### 📚 Conceitos Aplicados do Bootcamp:  

Este projeto aplica diretamente os seguintes conceitos trabalhados ao longo do bootcamp:

Fundamentos de Python.   
Manipulação de dados com Pandas.   
Conceito de ETL (Extract, Transform, Load).   
Organização de projetos em Python.    
Versionamento com Git e GitHub.  
Uso conceitual de IA Generativa aplicada a dados.  
Adaptação a cenários reais (API indisponível).  

### 🧪 Observações Importantes:  

Os dados utilizados são fictícios e têm finalidade exclusivamente educacional.  

A IA Generativa foi simulada conforme orientação do desafio, garantindo que o foco permaneça no aprendizado de ETL.  

O projeto foi desenvolvido com foco acadêmico e colaborativo, servindo como material de estudo e portfólio.  