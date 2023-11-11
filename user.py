import requests

prompt = "quem é você?"

url = "http://localhost:5000/pergunta"

resposta = requests.get(url, json=prompt)

if resposta.status_code == 200:
    print(resposta.json())
else:
    print(f"Erro ao fazer a requisição: {resposta.status_code}")
