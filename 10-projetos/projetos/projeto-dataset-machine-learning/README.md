# 📊 Projeto — Dataset de Imagens para Machine Learning, com foco em Deep Learning aplicado à Visão Computacional(Cats vs Dogs). 

## 📌 Visão Geral:  

Este projeto faz parte do repositório **dio-bootcamp-cienciadedados-python** e tem como objetivo a **criação, validação e versionamento de um dataset de imagens** para problemas de **classificação supervisionada** em Visão Computacional, utilizando **Machine Learning / Deep Learning**.

O dataset final contém **240 imagens balanceadas**, sendo:

* 🐱 **120 imagens de gatos**
* 🐶 **120 imagens de cachorros**

Todo o pipeline foi construído com foco em **boas práticas profissionais**, garantindo reprodutibilidade, rastreabilidade e qualidade dos dados.

---

## 🎯 Objetivos do Projeto:  

* Criar um dataset balanceado para classificação binária (cats vs dogs).  
* Garantir qualidade visual das imagens (foco, centralização, resolução).  
* Padronizar nomes de arquivos e labels.  
* Implementar scripts automatizados de validação.  
* Versionar dataset e pipeline de forma organizada.  
* Preparar o projeto para uso real em treinamento de modelos.  

---

## 🧠 Contexto de Machine Learning:  

Este dataset pode ser utilizado em:

* Classificação de imagens com CNNs.  
* Transfer Learning (ResNet, VGG, MobileNet, EfficientNet).  
* Estudos de data preprocessing e data validation.  
* Exercícios de split treino/validação/teste.  
* Portfólio técnico para entrevistas em Data Science / ML.  

---

## 📁 Estrutura do Projeto:  

```
projeto-dataset-machine-learning/
│
├── README.md
└── dataset_cats_dogs/
    ├── dataset/
    │   ├── cats/          # cat_001.jpg ... cat_120.jpg
    │   ├── dogs/          # dog_001.jpg ... dog_120.jpg
    │   └── labels.csv
    │
    ├── raw/               # imagens intermediárias (processamento)
    │   ├── cats/
    │   ├── dogs/
    │   ├── cats_extra/
    │   └── dogs_extra/
    │
    ├── raw_collages/      # colagens originais geradas
    │   ├── cats/
    │   └── dogs/
    │
    ├── scripts/           # pipeline automatizado
    │   ├── passo1_setup_e_validacao.py
    │   ├── passo1_1_split_colagens.py
    │   ├── passo1_2_normalizar_120.py
    │   ├── passo2_renomear_e_labels.py
    │   ├── passo3_validacao_completa.py
    │   └── passo4_gerar_zip.py
    │
    └── dataset.zip        # dataset final compactado
```

---

## 🧪 Checklist de Qualidade do Dataset:  

✔ Imagens nítidas e centralizadas. 
✔ Apenas **1 animal por imagem**. 
✔ Resolução mínima ≥ **400x400** (dataset final ≥ 512x512). 
✔ Sem marca d’água, texto ou memes.
✔ Classes corretamente separadas (gato ≠ cachorro).
✔ Balanceamento perfeito entre classes.
✔ Nomenclatura sequencial padronizada.

>> As imagens utilizadas neste dataset foram obtidas de fontes públicas e abertas,
com finalidade exclusivamente educacional.


---

## 🏷️ Padronização de Nomes.  

### Gatos:  

```
cat_001.jpg
cat_002.jpg
...
cat_120.jpg
```

### Cachorros:  

```
dog_001.jpg
dog_002.jpg
...
dog_120.jpg
```

---

## 📄 Arquivo de Labels:  

O arquivo `labels.csv` segue o formato:

```csv
filename,label
cats/cat_001.jpg,cat
cats/cat_002.jpg,cat
...
dogs/dog_120.jpg,dog
```

Esse formato é compatível com **PyTorch**, **TensorFlow/Keras** e outras bibliotecas de ML.

---

## ⚙️ Pipeline Automatizado:  

O projeto conta com scripts que cobrem todo o ciclo de preparação do dataset:

1. **Setup e validação inicial**
2. **Split de colagens em imagens individuais**
3. **Normalização para exatamente 120 imagens por classe**
4. **Renomeação padronizada e geração de labels**
5. **Validação completa de sequência e consistência**
6. **Geração do dataset final compactado (`dataset.zip`)**

Todos os passos são reproduzíveis e documentados.

---

## 🚀 Como Usar o Dataset:  

1. Clone o repositório
2. Navegue até o projeto:

   ```bash
   cd 10-projetos/projetos/projeto-dataset-machine-learning
   ```
3. Extraia o dataset:

   ```bash
   unzip dataset_cats_dogs/dataset.zip
   ```
4. Use as imagens e `labels.csv` no seu pipeline de ML.  


---

## 👩‍💻 Autoria:  

Projeto desenvolvido por **Jeniffer Pires**, como parte do **DIO Bootcamp — Ciência de Dados com Python**, com foco em aprendizado prático e construção de portfólio profissional.

---

📌 *Este projeto demonstra domínio de organização de dados, automação de pipelines e boas práticas em Machine Learning aplicado a Visão Computacional.*
