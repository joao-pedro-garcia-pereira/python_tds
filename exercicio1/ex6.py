import requests #biblioteca para fazer reqisições HTTP

cep = input("Digite o CEP (Sómente numeros): ")
cep = cep.replace("-", "") #Vai retirar o tracinho se o usuario Digitar

if len(cep) != 8 or not cep.isdigit():
    print("CEP invalido!! Digite até 8 números.")
else:
    url = f"https://viacep.com.br/ws/{cep}/json"
    resposta = requests.get(url)
    dados = resposta.json()

if "erro" in dados:
    print("CEP não encontrado")
else:
    logradouro = dados.get("logradouro", "")
    complemento = dados.get("complemento", "")
    bairro = dados.get("bairro", "")
    cidade = dados.get("localidade", "")
    estado = dados.get("uf", "")

    print("\n --- Endereço encontrado")
    print( f"Logradouro: {logradouro}")
    print( f"Complemento: {complemento}")
    print( f"Bairro: {bairro}")
    print( f"Cidade: {cidade}")
    print( f"Estado: {estado}")