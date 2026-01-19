# 📌 Fluxo de Trabalho com Git.
## 📖 Introdução: 

O fluxo de trabalho com Git define como o código evolui ao longo do tempo, desde a criação de uma funcionalidade até sua integração à versão principal do projeto.
Seguir um fluxo bem definido é essencial para evitar conflitos, retrabalho e erros em ambientes colaborativos.

## 🎯 Quando usar no dia a dia.

Desenvolvimento em equipe.  
Criação de novas funcionalidades.  
Correção de bugs.  
Organização de versões.  
Projetos versionados no GitHub.  

## 🧠 Conceito.  

Um fluxo de trabalho com Git normalmente envolve:  

1️⃣ Uma branch principal (main).   
2️⃣ Branches auxiliares para novas funcionalidades ou correções.  
3️⃣ Commits pequenos e frequentes.  
4️⃣ Integração controlada das alterações.  

Esse modelo permite que várias pessoas trabalhem no mesmo projeto sem sobrescrever o trabalho umas das outras.  

## 🧪 Exemplos práticos:  
🔹 Fluxo básico de desenvolvimento:

1️⃣ Criar uma nova branch a partir da principal.
```bash
git checkout -b feature-nova-funcionalidade
```

2️⃣ Trabalhar normalmente no código.  
3️⃣ Verificar alterações. 
```bash
git status
```

4️⃣ Adicionar arquivos.
```bash
git add .
```

5️⃣ Criar um commit.
```bash
git commit -m "feat: adiciona nova funcionalidade"
```

6️⃣ Enviar a branch para o repositório remoto.
```bash
git push origin feature-nova-funcionalidade
``` 

7️⃣ Integrar a branch à main (merge).
```bash
git checkout main
git pull origin main
git merge feature-nova-funcionalidade
```

### ⚠️ Erros comuns / armadilhas: 

❌ Trabalhar diretamente na branch main.  
❌ Fazer commits grandes e genéricos.  
❌ Não atualizar a branch principal antes do merge.  
❌ Ignorar conflitos de código.  
❌ Não testar antes de integrar mudanças.  

## ✅ Boas práticas: 

✔️ Criar uma branch por funcionalidade ou correção.  
✔️ Commits pequenos e com mensagens claras.  
✔️ Atualizar a branch principal com frequência.  
✔️ Revisar alterações antes do merge.  
✔️ Testar o código localmente.  

## 🌍 Ligação com o mundo real: 

Esse fluxo é amplamente utilizado em:

Times de desenvolvimento corporativos.  
Projetos open source.  
Ambientes com CI/CD.  
Versionamento de dados e pipelines em ciência de dados.  

Dominar esse processo demonstra maturidade técnica e organização, dois pontos muito valorizados por recrutadores.  

#### 🧾 Observações finais:

Este arquivo foca no fluxo, não nos detalhes técnicos de merge ou conflitos. 
Esses tópicos são aprofundados no próximo conteúdo do módulo.

