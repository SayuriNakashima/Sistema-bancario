# Define o menu que será exibido para o usuário
menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
"""

# Inicializa as variáveis principais do sistema bancário
saldo = 0                     # Saldo inicial da conta
limite = 500                 # Limite máximo permitido por saque
extrato = ""                 # Registro de transações (depósitos e saques)
numero_saque = 0             # Contador de saques realizados
LIMITE_SAQUES = 3            # Número máximo de saques por sessão

# Lista de operações simuladas: cada item é uma tupla (opcao, valor)
# Ex: ("1", 1000) = opção 1 (depósito), valor R$1000
operacoes_simuladas = [
    ("1", 1000),   # Depositar R$1000
    ("2", 200),    # Sacar R$200
    ("2", 600),    # Tentar sacar acima do limite (erro)
    ("2", 100),    # Sacar R$100
    ("2", 50),     # Sacar R$50
    ("2", 50),     # Tentar sacar acima do limite de 3 saques (erro)
    ("3", None),   # Ver extrato
    ("4", None)    # Sair do sistema
]

# Inicia o loop para percorrer as operações simuladas
for opcao, valor in operacoes_simuladas:
    # Exibe o menu no console
    print(menu)
    print(f">>> Opção escolhida: {opcao}")

    # OPÇÃO 1 – DEPÓSITO
    if opcao == "1":
        print(f"Simulando depósito de R$ {valor:.2f}")
        if valor > 0:
            saldo += valor  # Adiciona o valor ao saldo
            extrato += f"Depósito: R$ {valor:.2f}\n"  # Registra no extrato
        else:
            print("Operação falhou! O valor informado é inválido.")

    # OPÇÃO 2 – SAQUE
    elif opcao == "2":
        print(f"Simulando saque de R$ {valor:.2f}")

        # Verificações antes de permitir o saque
        excedeu_saldo = valor > saldo                     # Verifica se tem saldo suficiente
        excedeu_limite = valor > limite                   # Verifica se o valor excede o limite de saque
        excedeu_saques = numero_saque >= LIMITE_SAQUES    # Verifica se passou do número de saques permitidos

        # Lógicas de erro, nesta ordem de prioridade:
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor                        # Subtrai o valor do saldo
            extrato += f"Saque: R$ {valor:.2f}\n"  # Registra no extrato
            numero_saque += 1                      # Incrementa o contador de saques
        else:
            print("Operação falhou! O valor informado é inválido.")

    # OPÇÃO 3 – EXIBIR EXTRATO
    elif opcao == "3":
        print("\n========= EXTRATO ========")
        # Se não houve transações, mostra mensagem padrão
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("=============================\n")

    # OPÇÃO 4 – SAIR DO SISTEMA
    elif opcao == "4":
        print("Encerrando operação... Obrigado por usar nosso banco!\n")
        break  # Encerra o loop (fim do programa)

    # QUALQUER OUTRA OPÇÃO INVÁLIDA
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
