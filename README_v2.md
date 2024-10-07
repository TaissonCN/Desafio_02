
# Sistema Bancário em Python

Este projeto implementa um sistema bancário simples, que permite o cadastro de usuários, criação de contas correntes e operações básicas como depósito, saque e extrato. O código é modularizado, garantindo fácil manutenção e expansão futura.

## Funcionalidades
1. **Cadastrar Usuário**: Permite o cadastro de usuários com informações como nome, sobrenome, data de nascimento, CPF, endereço e telefone.
2. **Listar Usuários**: Exibe a lista de todos os usuários cadastrados com suas respectivas informações.
3. **Remover Usuário**: Permite remover um usuário do sistema com base no CPF fornecido.
4. **Criar Conta Corrente**: Cria uma conta corrente vinculada a um usuário, com agência fixa "0001" e número de conta gerado sequencialmente.
5. **Depositar**: O usuário pode realizar depósitos em sua conta.
6. **Sacar**: O sistema permite saques, com limite diário de três saques e valor máximo de R$500 por saque.
7. **Extrato**: Exibe todas as transações realizadas, incluindo depósitos e saques, bem como o saldo atual.

## Regras e Restrições
- Não é possível cadastrar dois usuários com o mesmo CPF.
- Cada conta corrente pertence a um único usuário, mas um usuário pode ter mais de uma conta.
- Limite de três saques diários, com valor máximo de R$500 por saque.
- O CPF deve ser único e é armazenado sem pontuações.

## Como Rodar o Sistema
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/sistema-bancario-python.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd sistema-bancario-python
   ```
3. Execute o arquivo Python:
   ```bash
   python sistema_bancario.py
   ```

## Exemplo de Uso

No menu principal, você poderá escolher entre as seguintes opções:
- **Cadastrar Usuário**: Insira as informações solicitadas para adicionar um novo usuário.
- **Listar Usuários**: Exibe a lista de usuários cadastrados.
- **Remover Usuário**: Informe o CPF do usuário para removê-lo do sistema.
- **Abrir Conta Corrente**: Vincule um usuário já cadastrado a uma nova conta corrente.
- **Depositar**: Informe o valor a ser depositado na conta corrente.
- **Sacar**: Informe o valor do saque, respeitando o limite diário.
- **Extrato**: Consulte o saldo atual e as transações realizadas.
- **Sair**: Encerre o programa.

## Estrutura do Projeto
- **sistema_bancario.py**: Código principal que contém a lógica do sistema e funções para operações bancárias.
- **README.md**: Este arquivo, que descreve o projeto e como utilizá-lo.

## Melhorias Futuras
- Implementar autenticação de usuários com login e senha.
- Adicionar validação para campos como CPF e data de nascimento.
- Registrar data e hora de cada transação no extrato.
- Implementar operações de transferência entre contas.

---

Este projeto é um exemplo prático para entender como implementar um sistema bancário básico usando Python, com foco na modularização de funções e boas práticas de programação.
