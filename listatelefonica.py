# Cabeçalho
print("-"*22)
print("-"*6, "CONTATOS", "-"*6)
print("-"*22)

# Criando o dicionário
contatos = {}
comando = "continue" 

# Criando a seleção do comando
while comando != "sair":
    comando = input("Digite o comando: (novo, pesquisa, sair):")

    # Comando "novo" para adicionar valor a uma chave
    if comando == "novo":
        nome = input('Nome: ').strip() # Comando ".strip()" para evitar erro por espaço em branco
        telefone = input("Telefone: ").strip()
        email = input("E-mail: ").strip()
        # Comando ".lower()" para guardar a informação sem em minúsculo
        contatos[nome.lower()] = {
           "nome": nome,
           "telefone": telefone,
            "email": email
        }

        # Comando "pesquisa" para fazer consultas dentro de chaves existentes
    if comando == "pesquisa":
        nome = input("Nome: ").lower() # Comando ".lower()" para guardar a informação sem em minúsculo
        if nome in contatos:
            print(contatos[nome])
        else:
            print('Este contato não existe')