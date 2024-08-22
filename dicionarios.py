dicionario = {
    "nome": "Marcela",
    "sobrenome": "Freitas",
    "idade": 7
}

# mostrando valor por valor contido em uma chave
print(dicionario["nome"]) #retorna >>> Marcela
print(dicionario["sobrenome"]) #retorna >>> Freitas

# mostrando apenas as chaves que contém dentro do dicionário
for chave in dicionario:
    print(dicionario [chave])


# mostrando apenas o valor contido dentro de uma chave
for valor in dicionario.values():
    print(valor)

# mostrando a chave e o valor contido nela
for chave, valor in dicionario.items():
    print(chave + '-' + str(valor))

# verificando se uma chave existe no dicionário
if "nome" in dicionario:
    print("nome existe")

if "pais" in dicionario:
    print('pais não existe')


# informa quantos itens contém no dicionário
print(len(dicionario))

# criando um dicionário e adicionando valores quando necessário
dicionario2 = {}
dicionario2["marca"] = "Mercedes"
dicionario2["modelo"] = "Classe A"
print(dicionario2)

# excluindo alguma chave e o valor contido dentro de um dicionário
dicionario2.pop("modelo")
print(dicionario2)

# criando chaves dentro de outra chave
contatos = {
    "Flavia": {
        "nome": "Flavia",
        "telefone": "(11) 91234-5678",
        "email": "flavia@aluno.faculdadeimpacta.com.br" #ultimo item não precisa de vírgula no final
    }, #finaliza a chave com vírgula para adicionar outra chave
    "Daniela Sato": {
        "nome": "Daniela Sato",
        "telefone": "(11) 98765-4321",
        "email": "daniela.sato@faculdadeimpacta.com.br",
        "empresa": "Enterprises"
    }
}