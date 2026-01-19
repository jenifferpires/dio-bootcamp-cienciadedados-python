# 📌 Fluxo de Trabalho com Git e GitHub.
## 📖 Introdução: 

O fluxo de trabalho com Git e GitHub define como as alterações no código são organizadas, versionadas e compartilhadas entre pessoas e ambientes.  
Seguir um fluxo bem definido evita conflitos, retrabalho e perda de código.

## 🎯 Quando usar no dia a dia:

Trabalhar em equipe no mesmo projeto.      
Desenvolver novas funcionalidades com segurança.      
Corrigir bugs sem afetar a versão principal.      
Manter histórico organizado e rastreável.    
Publicar projetos no GitHub.    

## 🧠 Conceito:  

O fluxo de trabalho mais comum envolve:

1️⃣ Branch principal (main) – versão estável do projeto.   
2️⃣ Branches de desenvolvimento – novas funcionalidades ou correções.    
3️⃣ Commits frequentes – registro de pequenas evoluções.    
4️⃣ Push para o GitHub – envio do código para o repositório remoto.    
5️⃣ Merge – integração das mudanças à branch principal.    

Esse modelo é amplamente usado em empresas e projetos open source.  

## 🧪 Exemplos práticos: 
🔹 Criando uma nova branch:  
```bash
git branch nova-feature
git checkout nova-feature
```
Ou de forma simplificada:
```bash
git checkout -b nova-feature
```
🔹 Trabalhando na branch:
```bash
git status
git add .
git commit -m "feat: adiciona nova funcionalidade"
```
As alterações ficam isoladas da branch principal.

🔹 Enviando a branch para o GitHub: 
```bash
git push origin nova-feature
```
Publica a branch no repositório remoto.

🔹 Atualizando a branch principal: 
```bash
git checkout main
git pull origin main
```
Garante que você está trabalhando com a versão mais recente.

🔹 Fazendo merge das alterações: 
```bash
git merge nova-feature
```
Integra as mudanças da branch ao código principal.

🔹 Resolvendo conflitos.

Quando dois arquivos são alterados no mesmo ponto:
O Git sinaliza o conflito.
O desenvolvedor ajusta manualmente o código.  
Um novo commit finaliza a correção.  

### ⚠️ Erros comuns:  

❌ Trabalhar diretamente na branch main.  
❌ Fazer commits grandes demais.  
❌ Não atualizar a branch antes do merge.  
❌ Ignorar conflitos de merge.  
❌ Fazer push sem testar o código.  

### ✅ Boas práticas: 

✔️ Criar branches por funcionalidade ou correção.  
✔️ Commits pequenos e frequentes.  
✔️ Mensagens padronizadas (feat, fix, docs).  
✔️ Atualizar a branch principal com frequência.  
✔️ Testar antes de fazer merge.  

### 🧾 Ligação com o mundo real:

Empresas utilizam esse fluxo para:

Controlar versões em produção. 
Trabalhar com múltiplos desenvolvedores.    
Reduzir erros em deploys.  
Garantir rastreabilidade de mudanças.   

Esse modelo reflete exatamente o que acontece em times profissionais.