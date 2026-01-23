# Projeto – Criação de Dataset para Machine Learning.  

## 📌 Objetivo:  
Este projeto tem como objetivo a criação de um **dataset de imagens** para o treinamento de um algoritmo de **Inteligência Artificial baseado em Redes Neurais Artificiais**, conforme proposto na atividade da trilha de Machine Learning da DIO.

O dataset criado neste projeto servirá como base para projetos futuros de **classificação de imagens**, utilizando bibliotecas e frameworks amplamente adotados no mercado, como TensorFlow e PyTorch.

---

## 🧠 Contexto:  
Em problemas de Visão Computacional, o desempenho de um modelo de Machine Learning depende diretamente da **qualidade e organização do dataset** utilizado para treinamento.

Neste projeto, foi criada uma base de dados contendo **duas classes distintas**, cada uma com no mínimo **100 imagens**, respeitando critérios mínimos de qualidade e resolução.

---

## 📁 Estrutura do Projeto:  

```text
projeto-dataset-machine-learning/
│
├── README.md
│
├── dataset/
│   ├── classe_1/
│   │   ├── img_001.jpg
│   │   ├── img_002.jpg
│   │   └── ...
│   │
│   ├── classe_2/
│   │   ├── img_001.jpg
│   │   ├── img_002.jpg
│   │   └── ...
│   │
│   └── scripts/
│       └── validacao_dataset.py
```

Cada pasta representa uma classe de objetos, sendo o nome da pasta utilizado como rótulo (label) durante o treinamento do modelo.

## 🖼️ Dataset: 
#### Classes:  

**Classe 1:** `classe_1`

**Classe 2:** `classe_2`

> As classes podem representar objetos, animais, pessoas, expressões faciais ou qualquer outro conceito visual, desde que sejam distintas entre si.

#### Requisitos das Imagens:  

Quantidade mínima: **100 imagens por classe.**  

Resolução mínima recomendada: **400x400 pixels.**   

Imagens nítidas e bem iluminadas.  

Formatos comuns: `.jpg`, `.jpeg` ou `.png`.  

As imagens podem ser:

Capturadas com câmera própria.  
Obtidas de bases públicas ou da internet, respeitando qualidade visual.  

### 🔎 Validação do Dataset:  

O diretório `scripts` contém um script opcional (`validacao_dataset.py`) que pode ser utilizado para:

Verificar a quantidade de imagens por classe.  
Conferir formatos suportados.  
Auxiliar na validação antes do treinamento do modelo.  

### 🚀 Aplicações Futuras:  

Este dataset poderá ser utilizado em:

Treinamento de classificadores de imagens.  
Redes Neurais Convolucionais (CNN).  
Projetos de Visão Computacional.  
Estudos sobre balanceamento de classes e pré-processamento de imagens.  

#### 📝 Observações:  

Este projeto faz parte de uma sequência de projetos desenvolvidos ao longo da trilha de **Ciência de Dados e Machine Learning**, com foco em boas práticas, organização e clareza na documentação.  