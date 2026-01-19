# 📌 Merge e Resolução de Conflitos no Git.
## 📖 Introdução: 

Ao trabalhar com múltiplas branches, em algum momento será necessário unir alterações diferentes no mesmo projeto.  
O processo de merge permite integrar essas mudanças, mas pode gerar conflitos quando o Git não consegue decidir automaticamente qual versão do código manter.

Saber lidar com merges e conflitos é essencial em ambientes colaborativos.

## 🎯 Quando usar no dia a dia? 

Integração de funcionalidades desenvolvidas em branches.  
Correção de bugs em paralelo.    
Atualização de código entre diferentes versões.    
Trabalho em equipe com múltiplos desenvolvedores.    

## 🧠 Conceito:  
#### 🔹 O que é merge?    

Merge é o processo de combinar alterações de uma branch em outra, geralmente integrando uma branch de funcionalidade à branch principal (main).  

#### 🔹 O que são conflitos?  

Conflitos ocorrem quando:

Duas branches alteram a mesma linha de um arquivo.  
O Git não consegue identificar automaticamente qual alteração manter.  

## 🧪 Exemplos práticos:  
🔹 Realizando um merge simples: 
```bash
git checkout main
git pull origin main
git merge feature-ajuste-relatorio
```

Se não houver conflitos, o merge é realizado automaticamente.  

#### 🔹 Exemplo de conflito de merge:  

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


#### 🔹 Resolvendo o conflito.

1️⃣ Abrir o arquivo com conflito.  
2️⃣ Escolher ou combinar o código correto.  
3️⃣ Remover as marcações do Git.  
4️⃣ Adicionar o arquivo corrigido.  

```bash
git add arquivo.py
```

5️⃣ Finalizar o merge
```bash
git commit -m "fix: resolve conflito de merge"
```

## ⚠️ Erros comuns / armadilhas.

❌ Fazer merge sem atualizar a branch principal.  
❌ Resolver conflitos sem entender o impacto no código.  
❌ Apagar código importante por engano.  
❌ Usar git reset para “resolver” conflitos.  
❌ Commits genéricos após conflito.  

## ✅ Boas práticas: 

✔️ Atualizar a branch principal antes do merge.  
✔️ Resolver conflitos com calma e atenção.  
✔️ Testar o código após resolver conflitos.  
✔️ Commits claros após resolução.  
✔️ Usar branches curtas para reduzir conflitos.  

## 🌍 Ligação com o mundo real: 

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
O importante é saber identificá-los e resolvê-los corretamente.  