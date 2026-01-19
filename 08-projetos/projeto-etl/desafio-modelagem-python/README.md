# 📊 Desafios de Lógica e Modelagem de Dados (Bootcamp DIO). 
## 📌 Visão Geral> 
Este diretório centraliza a resolução de desafios técnicos focados em logística e exportação de papel e celulose. O objetivo é aplicar conceitos de modelagem de dados e manipulação de estruturas em Python para resolver problemas reais de negócio.

## 🎯 Objetivos Estratégicos: 
Resolução de Problemas: Aplicação de lógica de programação para sumarização de grandes volumes de dados.

Modelagem de Dados: Validação de conhecimentos em bancos de dados Relacionais (SQL) e Não Relacionais (NoSQL).

Processamento Eficiente: Uso de dicionários e parsing de arquivos para simular um fluxo de dados profissional.

## 🧠 Conteúdos Consolidados: 
### 🐍 Lógica em Python.

Dicionários (Dict): Uso de estruturas chave-valor para agregação e acumulação dinâmica.  

Manipulação de Strings: Parsing e limpeza de dados brutos originados de arquivos CSV.  

Automação de Entrada: Scripts preparados para leitura de arquivos ou entrada manual (fallback).  

### 🗄️ Arquitetura de Dados: 
Relacional: Domínio de Cardinalidade, Joins (Inner, Left, Right, Full) e Subconsultas.  

NoSQL: Conceitos de bancos Chave-Valor e Documentos, com foco em comandos de atualização em massa (MongoDB updateMany).  

### 🏗️ Estrutura dos Desafios: 
#### 1. 🌍 Sistema de Exportação por País:  
Script voltado para o cálculo de toneladas exportadas, agrupando valores dinamicamente conforme o país de destino aparece na entrada.  

Destaque: Preservação da ordem de inserção original no relatório final.  

Arquivo: `desafio-exportacao/desafio_exportacao.py`

#### 2. 📦 Gestão de Embalagens: 
Cálculo de demanda por tipo de embalagem ("saco", "papelão ondulado" ou "papel kraft").

Destaque: Garantia de integridade para categorias com valor zero (Schema pré-definido).

Arquivo: `desafio_embalagem.py`

#### 🗂️ Organização de Arquivos: 
```Plaintext

desafio-modelagem-python/
│
├── desafio_embalagem.py       # Lógica de toneladas por tipo de embalagem
├── desafio-exportacao/        # Submódulo de exportação global
│   ├── desafio_exportacao.py
│   └── data/input/            # Massa de dados de teste (CSV)
└── data/input/                # Entradas para o desafio de embalagens
```

### 🧪 Como Testar: 
Os scripts estão configurados para buscar automaticamente os arquivos na pasta data/input/.
Para validar a lógica, basta executar:  

#### Para o desafio de embalagens
```bash
python desafio_embalagem.py
```

#### Para o desafio de exportação: 
```bash
python desafio-exportacao/desafio_exportacao.py
```
