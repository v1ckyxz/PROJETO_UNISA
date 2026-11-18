import json

senha_admin = "admin123"

try:
    with open("paciente.json", "r", encoding="utf-8") as arquivo:
        pacientes = json.load(arquivo)
except (FileNotFoundError, json.JSONDecodeError):
    pacientes = []

def ordenar_pacientes(registros, chave):
    lista = registros[:]
    n = len(lista)
    for i in range(n - 1):
        trocou = False
        for j in range(n - 1 - i):
            if lista[j][chave] > lista[j + 1][chave]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
        if not trocou:
            break
    return lista

def telefone():
    while True:
        telefone_paciente = input("Digite o seu telefone com DDD: ")
        telefone_digito = "".join([char for char in telefone_paciente if char.isdigit()])
        if len(telefone_digito) == 11:
            ddd = telefone_digito[:2]
            parte1 = telefone_digito[2:7]
            parte2 = telefone_digito[7:]
            return f"(+55) {ddd} {parte1}-{parte2}"
        else:
            print("Telefone incorreto. Insira novamente.")

def obter_data_nascimento():
    while True:
        data_digitada = input("Qual é a sua data de nascimento (apenas números)? ").strip().lower()
        data_digito = "".join([c for c in data_digitada if c.isdigit()])
        if len(data_digito) == 8:
            dia = data_digito[:2]
            mes = data_digito[2:4]
            ano = data_digito[4:8]
            data_formatada = f"{dia}/{mes}/{ano}"
            return data_formatada
        else:
            print("Data incorreta! Digite exatamente 8 números.")

def cpf():
    while True:
        cpf_digitado = input("CPF: ")
        cpf_digito = "".join([c for c in cpf_digitado if c.isdigit()])
        if len(cpf_digito) == 11:
            primeiro = cpf_digito[:3]
            segundo = cpf_digito[3:6]
            terceiro = cpf_digito[6:9]
            quarto = cpf_digito[9:11]
            return f"{primeiro}.{segundo}.{terceiro}-{quarto}"
        else:
            print("CPF incorreto. Digite novamente.")

senha = input("Digite a senha: ")
while senha != senha_admin:
    print("Senha incorreta.")
    senha = input("Digite novamente: ")

print("\nSeja bem-vindo(a)!")

while True:
    adicionar_paciente = input("\nGostaria de adicionar os dados de um paciente? (sim/não): ").strip().lower()

    if adicionar_paciente == "sim":
        nome = input("Nome: ").strip().lower()
        sobrenome = input("Sobrenome: ").strip().lower()
        data_nascimento = obter_data_nascimento()
        telefone_paciente = telefone()
        adicionar_cpf = cpf()
    
        alergia = input("Possui alergia a algum remédio? (sim/não): ").strip().lower()
        if alergia == "sim":
            remedio_alergia = input("Qual remédio? ").strip().lower()
        else:
            remedio_alergia = "-"

        ficha_paciente = {
            "nome": nome,
            "sobrenome": sobrenome,
            "data_nascimento": data_nascimento,
            "cpf": adicionar_cpf,
            "telefone": telefone_paciente,
            "alergia": alergia,
            "remedio_alergia": remedio_alergia
        }

        pacientes.append(ficha_paciente)
        pacientes = ordenar_pacientes(pacientes, "nome")
    
        with open("paciente.json", "w", encoding="utf-8") as arquivo:
            json.dump(pacientes, arquivo, indent=4, ensure_ascii=False)

        print("\nPACIENTE SALVO COM SUCESSO!")
    
    elif adicionar_paciente == "não" or adicionar_paciente == "nao":
        
        quer_pesquisar = input("\nGostaria de pesquisar algum paciente? (sim/não): ").strip().lower()
        
        if quer_pesquisar == "sim":
            termo = input("\nDigite o nome, sobrenome ou CPF: ").strip().lower()
            encontrou = False

            largura = 50

            for p in pacientes:
                if termo == p['nome'] or termo == p['sobrenome'] or termo == p['cpf']:
                    print() 
                    print(" PACIENTE ENCONTRADO ".center(largura, "-"))
                    print(f"NOME: {p['nome'].title()} {p['sobrenome'].title()}".center(largura))
                    print(f"CPF: {p['cpf']}".center(largura))
                    print(f"Tel: {p['telefone']}".center(largura))
                    print(f"Alergia: {p['remedio_alergia']}".center(largura))
                    print("-" * largura) 
                    encontrou = True

            if encontrou == False:
                print("Paciente não encontrado.")
            
        elif quer_pesquisar == "não" or quer_pesquisar == "nao":
            print("\nEncerrando cadastros e buscas...")
            break
            
        else:
            print("Opção inválida.")
            
    else:
        print("Opção inválida. Digite 'sim' ou 'não'.")

print("\n--- LISTA DE PACIENTES CADASTRADOS ---")

if len(pacientes) > 0:
    for p in pacientes:
        nome_completo = f"{p['nome'].title()} {p['sobrenome'].title()}"
        print(f"Nome: {nome_completo:<30.30}  | Nasc: {p['data_nascimento']:<12.12}  | CPF: {p['cpf']:<14.14}  | Tel: {p['telefone']:<15.15}  | Alergia: {p['remedio_alergia']:<25.25}")
else:
    print("Nenhum paciente cadastrado.")