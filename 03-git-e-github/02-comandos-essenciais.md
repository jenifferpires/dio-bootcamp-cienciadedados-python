# 📌 Comandos Essenciais do Git. 
## 📖 Introdução: 

O Git funciona a partir de comandos que permitem controlar versões do código, acompanhar mudanças e trabalhar de forma segura, individualmente ou em equipe.
Conhecer os comandos essenciais é fundamental para evitar erros, perda de código e conflitos desnecessários.

## 🎯 Quando usar no dia a dia. 

Iniciar o versionamento de um projeto.   
Acompanhar alterações no código.  
Salvar versões estáveis.  
Corrigir erros sem perder histórico.  
Trabalhar em times de desenvolvimento.  

## 🧠 Conceito:  

O Git trabalha com três áreas principais:

1️⃣ Working Directory – arquivos locais.  
2️⃣ Staging Area – arquivos preparados para commit.  
3️⃣ Repository – histórico versionado.  

Os comandos permitem mover arquivos entre essas áreas de forma controlada.

### 🧪 Exemplos práticos: 

🔹 Inicializando um repositório:
```bash
git init
```
Cria um repositório Git na pasta atual.

🔹 Verificando o estado dos arquivos: 
```bash
git status
```
Mostra arquivos modificados, adicionados ou prontos para commit.

🔹 Adicionando arquivos para versionamento:
```bash
git add arquivo.md
git add .
```
git add arquivo.md: adiciona um arquivo específico.  
git add . : adiciona todos os arquivos modificados.  

🔹 Salvando uma versão (commit):
```bash
git commit -m "mensagem clara e objetiva".
```
Cria um ponto no histórico com as alterações adicionadas.

🔹 Visualizando histórico:
```bash
git log
```
Mostra todos os commits realizados no repositório.

🔹 Comparando alterações:
```bash
git diff
```
Exibe diferenças entre o estado atual e o último commit.

🔹 Desfazendo alterações locais:
```bash
git restore arquivo.md
```
Descarta mudanças que ainda não foram commitadas.

🔹 Ajustando commits (com cuidado):
```bash
git reset --soft HEAD~1
```
Remove o último commit, mantendo os arquivos na staging area.

### ⚠️ Erros comuns: 

❌ Usar git add . sem revisar o que será versionado.  
❌ Fazer commits com mensagens genéricas como “update”.  
❌ Alterar histórico compartilhado com reset.  
❌ Não verificar o git status antes de commitar.  

### ✅ Boas práticas: 

✔️ Commits pequenos e frequentes.    
✔️ Mensagens claras e descritivas.    
✔️ Usar git status constantemente.   
✔️ Revisar alterações com git diff.    
✔️ Evitar reescrever histórico em branches compartilhadas.  

### 🧾 Ligação com o mundo real.

No ambiente corporativo, esses comandos são usados diariamente para:

Trabalhar em times distribuídos.  
Revisar código.    
Criar rastreabilidade de mudanças.   
Garantir segurança e estabilidade das entregas.  

Dominar esses comandos é um pré-requisito básico para qualquer desenvolvedor ou cientista de dados.