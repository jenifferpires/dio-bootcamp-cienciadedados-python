# 📌 Merge e Resolução de Conflitos no Git.  

## 📖 Introdução:  
Ao trabalhar com múltiplas branches, em algum momento será necessário unir alterações diferentes no mesmo projeto.    
O processo de *merge* permite integrar essas mudanças, mas pode gerar conflitos quando o Git não consegue decidir automaticamente qual versão do código manter.  

Saber lidar com merges e conflitos é essencial em ambientes colaborativos e projetos reais.  

---

## 🎯 Quando usar no dia a dia?  
- Integração de funcionalidades desenvolvidas em branches.  
- Correção de bugs em paralelo.  
- Atualização de código entre versões diferentes.  
- Trabalho em equipe com múltiplos desenvolvedores.  
- Recuperação de problemas causados por merges mal resolvidos.  

---

## 🧠 Conceito:  

### 🔹 O que é merge?  
Merge é o processo de combinar alterações de uma branch em outra, geralmente integrando uma branch de funcionalidade à branch principal (`main`).  

### 🔹 O que são conflitos?  
Conflitos ocorrem quando:  
- Duas branches alteram a mesma linha de um arquivo.  
- O Git não consegue identificar automaticamente qual alteração manter.  

---

## 🧪 Exemplos práticos:  

### 🔹 Realizando um merge simples:  
```bash
git checkout main
git pull origin main
git merge feature-ajuste-relatorio
```
Se não houver conflitos, o merge é realizado automaticamente.

### 🔹 Exemplo de conflito de merge:  

Ao tentar um merge, o Git pode exibir:  
```text
CONFLICT (content): Merge conflict in arquivo.py
```
O arquivo conterá marcações como:
```text

<<<<<<< HEAD
codigo_da_branch_principal
=======  
codigo_da_feature
>>>>>>> feature-ajuste-relatorio 
```
### 🔹 Resolvendo um conflito passo a passo:  

1️⃣ Abrir o arquivo com conflito.  
2️⃣ Escolher ou combinar o código correto.  
3️⃣ Remover as marcações do Git.  
4️⃣ Adicionar o arquivo corrigido.  

```bash
git add arquivo.py
```

5️⃣ Finalizar o merge: 
```bash
git commit -m "fix: resolve conflito de merge"
```

## 🛠️ Comandos úteis em cenários reais de conflito: 
#### 🔹 Verificar o estado do repositório:  
```bash
git status
```
Mostra arquivos em conflito e orienta os próximos passos.

#### 🔹 Abortar um merge com problemas:
```bash
git merge --abort
```
Cancela o merge e retorna o repositório ao estado anterior.

#### 🔹 Reverter para o último commit estável:
```bash
git reset --hard HEAD
```
⚠️ Remove alterações não commitadas.   
Usar com cautela.  

#### 🔹 Atualizar branch local antes de tentar novo merge:
```bash
git pull --rebase origin main
```
Reduz conflitos ao manter o histórico linear.

#### 🔹 Restaurar arquivos ou pastas específicas:
```bash
git restore caminho/do/arquivo
```
Ou a partir de um commit específico:
```bash
git restore --source=<hash> caminho/do/arquivo
```
#### 🔹 Recuperar arquivos de commits anteriores: 
```bash 
git checkout <hash> -- caminho/do/arquivo
```
Muito útil quando algo foi removido por engano após um merge.

#### 🔹 Investigar histórico de um arquivo:
```bash
git log -- caminho/do/arquivo
```
Ajuda a identificar quando e onde ocorreu o problema.  

### ⚠️ Erros comuns / armadilhas:  

❌ Fazer merge sem atualizar a branch principal.  
❌ Resolver conflitos sem entender o impacto no código.  
❌ Apagar código importante por engano.  
❌ Usar git reset indiscriminadamente.  
❌ Commits genéricos após conflitos.  
❌ Tentar “consertar tudo” em um único commit confuso.  

### ✅ Boas práticas:  

✔️ Atualizar a branch principal antes do merge.  
✔️ Resolver conflitos com calma e atenção.  
✔️ Testar o código após resolver conflitos.  
✔️ Commits claros e objetivos.  
✔️ Usar branches pequenas e com propósito definido.  
✔️ Criar commits frequentes para facilitar rollback.  

### 🌍 Ligação com o mundo real. 

Conflitos de merge são comuns em:

Times grandes.  
Projetos com alta frequência de mudanças.  
Ambientes corporativos e open source.  

Saber resolver conflitos demonstra:

Capacidade de análise.  
Organização.  
Comunicação técnica.  
Maturidade profissional.  

#### 🧾 Observações finais:  

Conflitos não são erros, mas parte natural do trabalho colaborativo.  
O diferencial está em saber diagnosticá-los, resolvê-los e recuperar o projeto com segurança, exatamente como ocorre em ambientes profissionais.  

