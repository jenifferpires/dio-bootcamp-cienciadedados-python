# 📌 Boas Práticas em Python.  

## 📖 Introdução:  
Boas práticas em Python ajudam a tornar o código mais legível, organizado,
manutenível e profissional. Elas facilitam o trabalho em equipe, reduzem erros
e tornam o código mais fácil de evoluir ao longo do tempo.

---

## 🎯 Quando usar no dia a dia?  
- Desenvolvimento de projetos profissionais.  
- Trabalho em equipe.  
- Manutenção de sistemas existentes.  
- Criação de scripts reutilizáveis.  
- Construção de portfólio e código público.  

---

## 🧠 Conceito:  
Boas práticas envolvem padrões de escrita, organização e comportamento do código.
Em Python, a principal referência é o **PEP 8**, guia oficial de estilo da linguagem.

---

## 🧪 Exemplos práticos:  

### Nomes de variáveis claros.  

```python
# Ruim
x = 10
y = 5

# Bom
total_itens = 10
itens_por_caixa = 5
``` 
📌 Código claro evita erros e facilita a leitura.

### Uso correto de indentação: 
```python
if total_itens > 0:
    print("Há itens disponíveis")
```
📌 Python depende da indentação para funcionar corretamente.  

### Conversão explícita de tipos:  
```python
idade = int(input("Digite sua idade: "))
```
📌 Evita erros de tipo e comportamentos inesperados.  

### Uso de f-strings:  
```python
nome = "Jeniffer"
print(f"Bem-vinda, {nome}!")
```
📌 Mais legível e moderna que concatenação tradicional.

## ⚠️ Erros comuns:  

**Erro 1: Código confuso e sem padrão.**
```python
a=10;b=20;print(a+b)
``` 

**Erro 2: Repetição de código.**
```python
print("Bem-vindo")
print("Bem-vindo")
print("Bem-vindo")
```

## ✅ Boas práticas recomendadas:  

Usar nomes de variáveis descritivos.  
Manter funções pequenas e objetivas.  
Evitar código duplicado.  
Comentar apenas quando necessário.  
Seguir o padrão PEP 8.  
Testar o código sempre que possível.  

## 🌍 Ligação com o mundo real.  

Boas práticas são exigidas em:

Empresas de tecnologia.  

Projetos open source.  

Times ágeis.  

Revisões de código (code review).  

Elas demonstram maturidade técnica e profissionalismo.