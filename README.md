# Exercicio3_de_modelagem

O projeto segue o padrão Clean Architecture, dividido em camadas:

Domain → Entidades principais (Conta e Cliente)
Use Cases → Regras de negócio (Criar conta, Depositar, Sacar)
Interfaces → Interface do repositório (DIP)
Infrastructure → Persistência em arquivo TXT
Main → Execução do sistema
Fluxo da Arquitetura
Main → UseCases → Interface Repository → Infrastructure → Domain

Isso aplica o princípio DIP – Dependency Inversion Principle, onde as regras de negócio não dependem da infraestrutura.

⚙️ Funcionalidades

O sistema permite:

Criar conta
Depositar dinheiro
Sacar dinheiro
Salvar contas em arquivo TXT
Buscar contas no arquivo
Persistência de dados

Os dados das contas são armazenados no arquivo:

contas.txt
▶️ Como executar o sistema

No terminal, dentro da pasta do projeto:

python main.py

O programa irá:

Criar uma conta
Depositar um valor
Realizar um saque
Salvar os dados no arquivo TXT
📝 Observação

Se o arquivo contas.txt não existir, ele será criado automaticamente ao salvar a primeira conta.
