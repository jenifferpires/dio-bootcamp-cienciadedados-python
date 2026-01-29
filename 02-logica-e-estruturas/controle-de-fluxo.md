# 📌 Controle de Fluxo em Python.

## 📖 Introdução: 
Controle de fluxo permite alterar o comportamento natural
de execução do código dentro de estruturas condicionais e
de repetição.   
Ele é usado para interromper, pular ou estruturar
melhor a execução dos loops.  

---

## 🎯 Quando usar no dia a dia:  
- Interromper loops quando uma condição for atingida.  
- Ignorar iterações específicas.  
- Criar estruturas de código temporárias.  
- Controlar execuções complexas.  

---

## 🧠 Conceito:  
Os principais comandos de controle de fluxo em Python são:

- `break` → encerra o loop imediatamente.  
- `continue` → pula para a próxima iteração.  
- `pass` → não executa nada (estrutura vazia).  

Eles são usados dentro de loops ou estruturas condicionais.  

---

## 🧪 Exemplos práticos:  

### Uso do `break`
```python
for numero in range(10):
    if numero == 5:
        break
    print(numero)
``` 

📌 O loop é interrompido ao atingir o valor 5.

### Uso do `continue`:  
```python
for numero in range(5):
    if numero == 2:
        continue
    print(numero)
```    
📌 O valor 2 é ignorado.

### Uso do `pass`: 
```python
for numero in range(3):
    if numero == 1:
        pass
    else:
        print(numero)
```
📌 `pass` é usado quando o bloco ainda será implementado.

Exemplo combinado: 
```python
for i in range(10):
    if i == 3:
        continue
    if i == 7:
        break
    print(i)
```    
📌 Demonstra controle total do fluxo de execução.

#### ⚠️ Erros comuns:
Erro 1: Uso excessivo de `break`. 
```python
while True:
    break
```
Erro 2: Uso desnecessário de `pass`. 
```python
if x > 10:
    pass
```

### ✅ Boas práticas: 

Usar `break` apenas quando necessário.  
Evitar lógica confusa em loops.  
Preferir condições claras.  
Usar `pass` apenas como placeholder.  
Manter o código simples e legível.  

### 🌍 Ligação com o mundo real.  
Controle de fluxo é usado em:

Processamento de dados.  
Validação de entradas.  
Sistemas de autenticação.  
Automação de tarefas.  
APIs e serviços backend.  

Ele permite criar fluxos inteligentes e eficientes.  


---


