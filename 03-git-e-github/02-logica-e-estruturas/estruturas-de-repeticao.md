# 📌 Estruturas de Repetição em Python

## 📖 Introdução
Estruturas de repetição permitem executar um bloco de código
várias vezes de forma controlada. Elas são essenciais para
processar listas, dados, arquivos e automatizar tarefas.

---

## 🎯 Quando usar no dia a dia
- Processar listas de dados
- Repetir tarefas automaticamente
- Percorrer arquivos e registros
- Executar ações enquanto uma condição for verdadeira
- Construir fluxos dinâmicos

---

## 🧠 Conceito
Em Python, as principais estruturas de repetição são:

- `for` → usado quando se sabe a quantidade de repetições  
- `while` → usado quando a repetição depende de uma condição  

Ambas ajudam a evitar repetição manual de código.

---

## 🧪 Exemplos práticos: 

#### Estrutura `for`.

```python 
for i in range(5):  
    print(i)
```    
📌 Executa o bloco 5 vezes, começando do zero.  

#### Percorrendo uma lista. 

```python  
nomes = ["Ana", "Bruno", "Carlos"]

for nome in nomes:
    print(nome)
```  

📌 Muito usado para percorrer coleções de dados.

#### Estrutura `while`.

```python 
contador = 0

while contador < 3:
    print(contador)
    contador += 1
```
📌 Executa enquanto a condição for verdadeira.

#### Laço com condição real.
```python
senha = ""

while senha != "1234":
    senha = input("Digite a senha: ")

print("Acesso permitido")
```
📌 Comum em sistemas de autenticação.

### ⚠️ Erros comuns:  

Erro 1: Loop infinito. 

```python
while True:
    print("Nunca termina")
```

Erro 2: Esquecer de atualizar a variável de controle.

```python
contador = 0
while contador < 5:
    print(contador)
```

### ✅ Boas práticas: 

Garantir condição de parada.    
Usar `for` quando possível.   
Evitar loops infinitos.   
Usar nomes claros para variáveis.   
Manter o código legível.   

### 🌍 Ligação com o mundo real.

Estruturas de repetição são usadas em:

Processamento de dados.  
Análise de grandes volumes de informação.  
ETL e automações. 
APIs e sistemas de backend.

São essenciais para transformar dados em informação.


