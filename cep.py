import requests

cep= input("Digete seu cep: ").strip()
url=f'https://viacep.com.br/ws/{cep}/json/'

response: requests= requests.get(url)

if response.status_code == 200:
    data = response.json()
    if "erro" not in data:
        print("CEP encontrado!")
        infcep={
            "cep": data.get("cep"),
            "logradouro": data.get("logradouro"),
            "complemento": data.get("complemento"),
            "unidade": data.get("unidade"),
            "bairro": data.get("bairro"),
            "localidade": data.get("localidade"),
            "uf": data.get("uf"),
            "estado": data.get("estado"),
            "regiao": data.get("regiao"),
            "ibge": data.get("ibge"),
            "gia": data.get("gia"),
            "ddd": data.get("ddd"),
            "siafi": data.get("siafi")
        }
else:
    print("Erro:", response.status_code)

for chave, intem in infcep.items():
    print(f'{chave}: {intem}')