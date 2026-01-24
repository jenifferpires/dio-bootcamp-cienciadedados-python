# RELATÓRIO DE IMPLEMENTAÇÃO DE SERVIÇOS AWS.  

Data: 24/01/2026  
Empresa: Abstergo Industries — Divisão Farmacêutica  
Responsável: Jeniffer Pires  

---

## Introdução:    
Este relatório apresenta o processo de implementação de serviços AWS na empresa Abstergo Industries, realizado por *Jeniffer Pires*.   


O objetivo do projeto foi propor uma arquitetura em nuvem utilizando serviços da AWS com foco em **redução de custos, escalabilidade e confiabilidade para uma plataforma de e-commerce farmacêutico**,aplicando conceitos fundamentais de computação em nuvem.

---

## Descrição do Projeto:  

A empresa atua no setor farmacêutico e deseja modernizar sua infraestrutura, migrando de um ambiente tradicional para a nuvem AWS.

Atualmente, a organização enfrenta altos custos com servidores físicos, dificuldades de escalabilidade e riscos relacionados à disponibilidade e segurança.

O projeto foi dividido em **3 etapas**, cada uma focada na adoção de um serviço AWS específico para resolver problemas reais do negócio.  

### Etapa 1 — Amazon EC2 (Elastic Compute Cloud).   

- **Foco da ferramenta:** Computação. 
- **Objetivo:** Hospedar a aplicação backend da farmácia.   
- **Descrição do caso de uso:**.   

O Amazon EC2 foi escolhido para executar a aplicação principal da plataforma virtual da farmácia.  
Esse serviço permite a criação de servidores virtuais sob demanda, eliminando a necessidade de aquisição e manutenção de servidores físicos.  

Com o EC2, a empresa passa a pagar apenas pelo tempo de uso da instância, reduzindo custos iniciais e possibilitando escalabilidade futura conforme o crescimento do negócio.    

### Etapa 2 — Amazon S3 (Simple Storage Service). 

- **Foco da ferramenta:** Armazenamento.  
- **Objetivo:** Armazenar imagens, documentos e arquivos estáticos.  
- **Descrição do caso de uso:**.  

O Amazon S3 foi escolhido como solução de armazenamento para imagens de produtos, receitas médicas digitalizadas e documentos do sistema da farmácia.  

Esse serviço oferece alta durabilidade, disponibilidade e baixo custo, permitindo que a empresa armazene grandes volumes de dados sem a necessidade de manter servidores dedicados, pagando apenas pelo espaço utilizado.    

### Etapa 3 — Amazon RDS (Relational Database Service).  

- **Foco da ferramenta:** Banco de Dados Relacional.  
- **Objetivo:** Armazenar dados transacionais da aplicação.  
- **Descrição do caso de uso:**.  

O Amazon RDS foi selecionado como banco de dados da plataforma da farmácia, sendo responsável por armazenar informações de clientes, produtos, pedidos e vendas.  

A escolha do RDS permite reduzir custos operacionais com administração de banco de dados, além de garantir segurança, backups automáticos e alta confiabilidade, atendendo às necessidades de uma aplicação real de e-commerce farmacêutico.    

## Conclusão:  
A implementação dos serviços AWS na empresa Abstergo Industries permite uma redução significativa de custos operacionais, ao mesmo tempo em que garante escalabilidade, segurança e alta disponibilidade.

A utilização do Amazon S3, EC2 e RDS oferece uma arquitetura sólida, modular e preparada para crescimento futuro, atendendo às necessidades de uma aplicação real de farmácia virtual.

Recomenda-se a continuidade do uso dos serviços propostos, bem como a evolução da arquitetura com monitoramento, automação e práticas avançadas de segurança.

Assinatura do Responsável pelo Projeto:  

Jeniffer Pires  



