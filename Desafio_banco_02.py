# Listas para armazenar usuários e contas
usuarios = []
contas = []

# Função para cadastrar usuário
def cadastrar_usuario(nome, sobrenome, data_nascimento, cpf, endereco, telefone):
    # Verifica se o CPF já está cadastrado
    cpf = ''.join(filter(str.isdigit, cpf))  # Remove pontuações do CPF
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("CPF já cadastrado!")
            return None
    
    # Cria o novo usuário
    novo_usuario = {
        "nome": nome,
        "sobrenome": sobrenome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco,
        "telefone": telefone
    }
    
    # Adiciona o usuário à lista
    usuarios.append(novo_usuario)
    print(f"Usuário {nome} cadastrado com sucesso!")

# Função para listar todos os usuários
def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        print("\n===== Lista de Usuários =====")
        for usuario in usuarios:
            print(f"Nome: {usuario['nome']} {usuario['sobrenome']}")
            print(f"Data de Nascimento: {usuario['data_nascimento']}")
            print(f"CPF: {usuario['cpf']}")
            print(f"Endereço: {usuario['endereco']}")
            print(f"Telefone: {usuario['telefone']}\n")
        print("=============================")

# Função para remover um usuário
def remover_usuario(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))  # Remove pontuações do CPF
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuarios.remove(usuario)
            print(f"Usuário com CPF {cpf} removido com sucesso!")
            return
    print("Usuário não encontrado.")

# Função para criar uma conta corrente
def criar_conta_corrente(cpf):
    # Filtrar o usuário pelo CPF
    cpf = ''.join(filter(str.isdigit, cpf))
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuario_encontrado = usuario
            break
    
    if not usuario_encontrado:
        print("Usuário não encontrado!")
        return None
    
    # Criação da conta
    numero_conta = len(contas) + 1
    nova_conta = {
        "agencia": "0001",
        "numero_conta": numero_conta,
        "usuario": usuario_encontrado
    }
    
    # Adiciona a conta à lista de contas
    contas.append(nova_conta)
    print(f"Conta {numero_conta} criada com sucesso para o usuário {usuario_encontrado['nome']}!")

# Função de saque (keyword only)
def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    if valor > saldo:
        print("Não há saldo suficiente para realizar o saque.")
    elif valor > limite:
        print(f"O valor do saque excede o limite de R$ {limite:.2f}.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Você atingiu o limite de saques diários.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("O valor do saque deve ser positivo.")
    return saldo, extrato

# Função de depósito (positional only)
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("O valor do depósito deve ser positivo.")
    return saldo, extrato

# Função de extrato (positional and keyword only)
def exibir_extrato(saldo, /, *, extrato):
    print("\n========== EXTRATO ==========")
    if extrato:
        print(extrato)
    else:
        print("Nenhuma movimentação realizada.")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=============================\n")

# Exemplo de uso das funções
def main():
    menu = """
    [c] Cadastrar usuário
    [l] Listar usuários
    [r] Remover usuário
    [a] Abrir conta corrente
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(menu)

        if opcao == "c":
            nome = input("Nome: ")
            sobrenome = input("Sobrenome: ")
            data_nascimento = input("Data de Nascimento: ")
            cpf = input("CPF: ")
            endereco = input("Endereço (logradouro - bairro - cidade/sigla estado): ")
            telefone = input("Telefone: ")
            cadastrar_usuario(nome, sobrenome, data_nascimento, cpf, endereco, telefone)

        elif opcao == "l":
            listar_usuarios()

        elif opcao == "r":
            cpf = input("Informe o CPF do usuário a ser removido: ")
            remover_usuario(cpf)

        elif opcao == "a":
            cpf = input("Informe o CPF do usuário: ")
            criar_conta_corrente(cpf)

        elif opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "q":
            print("Saindo do sistema...")
            break

        else:
            print("Operação inválida, por favor selecione novamente.")

if __name__ == "__main__":
    main()
