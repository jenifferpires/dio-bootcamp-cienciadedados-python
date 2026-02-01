# 🧠 Módulo 02 — Lógica e Estruturas em Python.

## 📖 Introdução: 
Este módulo aborda os **fundamentos da lógica de programação**, essenciais para escrever código correto, legível e eficiente.  
Aqui aprendemos **como tomar decisões, controlar o fluxo de execução e repetir ações**, que são a base de qualquer sistema, script ou pipeline de dados.

Sem lógica bem definida, não existe código confiável — apenas tentativas. 

---

## 🎯 Quando usar no dia a dia? 
A lógica de programação está presente em praticamente todos os cenários, como:

- Validação de dados de entrada. 
- Tomada de decisão baseada em regras de negócio. 
- Controle de execução de scripts.  
- Processamento condicional de dados.  
- Repetição de tarefas automatizadas.  
- Construção de pipelines e fluxos de dados.  

---

## 🧠 Conceitos abordados no módulo:  

### 🔹 Estruturas Condicionais:  
Permitem **executar blocos diferentes de código** com base em condições lógicas.

Exemplos:  
- `if`  
- `elif`  
- `else`  

Uso comum:  
- Validações.  
- Regras de negócio.  
- Fluxos alternativos.  

---

### 🔹 Estruturas de Repetição:  
Permitem **executar um bloco de código várias vezes**, de forma controlada.  

Exemplos:  
- `for`  
- `while`  

Uso comum:  
- Processar listas de dados.  
- Iterar sobre arquivos.  
- Executar tarefas repetitivas.  

---

### 🔹 Controle de Fluxo:  
Define **como e quando o código avança, interrompe ou continua** sua execução.  

Exemplos:  
- `break`  
- `continue`  
- `pass`  

Uso comum:  
- Interromper loops.  
- Pular iterações.  
- Controlar execução condicional.  

---

## 🧪 Exemplos práticos:  

### 🔸 Estrutura condicional simples:  
```python
idade = 18

if idade >= 18:
    print("Acesso permitido")
else:
    print("Acesso negado")
``` 
📌 O código executa blocos diferentes com base na condição avaliada.  

#### 🔸 Estrutura de repetição com `for`  
```python
for numero in range(1, 6):
    print(numero)
```
📌 Executa o bloco para cada valor da sequência.  

##### 🔸 Controle de fluxo com break:  
```python
for numero in range(10):
    if numero == 5:
        break
    print(numero)
```
📌 Interrompe o loop quando a condição é atendida.  

### ⚠️ Erros comuns / armadilhas:  

❌ Condições mal definidas (== vs =).  
❌ Loops infinitos por falta de condição de parada.  
❌ Uso excessivo de if aninhado.  
❌ Falta de clareza na lógica.  
❌ Não tratar cenários alternativos.  

### ✅ Boas práticas:  

✔️ Manter condições simples e legíveis.  
✔️ Usar nomes claros para variáveis.  
✔️ Evitar lógica complexa em um único bloco.  
✔️ Preferir clareza a “código esperto”.  
✔️ Testar fluxos alternativos.  

### 🌍 Ligação com o mundo real.

####  A lógica de programação é usada em:  

Sistemas corporativos.  
Automação de processos.  
Análise e tratamento de dados.  
Machine Learning e regras de decisão.  
APIs e serviços backend.  

Dominar lógica demonstra:  

Raciocínio estruturado.  
Capacidade analítica.  
Maturidade técnica.  
Base sólida para evoluir em qualquer área da tecnologia.  

### 📌 Conteúdos deste módulo:  

`estruturas-condicionais.md`

`estruturas-de-repeticao.md`

`controle-de-fluxo.md`

### 🧾 Observação final:  
Antes de aprender novas linguagens ou frameworks, domine a lógica.  
Ela é o verdadeiro diferencial entre quem apenas escreve código e quem resolve problemas.  