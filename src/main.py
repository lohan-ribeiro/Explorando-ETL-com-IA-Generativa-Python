
import pandas as pd
import json
import requests
from openai import OpenAI
import os


# URL dos dados iníciais.
url = "https://digitalinnovationone.github.io/santander-dev-week-2023-api/mocks/find_one.json"

# Verifica se o arquivo mock_users existe, antes de cria-lo, para não sobreescrever o arquivo.
if not os.path.exists("data/mock_users.json"):
  print("mock_users.json não foi encontrado. Baixando mock_users... ")
  response = requests.get(url)
  dados = response.json()

  with open("data/mock_users.json", "w", encoding="utf-8") as arquivo:
    json.dump([dados], arquivo, indent=4, ensure_ascii=False)
else:
   print("mock_users.json já existe. Mantendo dados locais.")

# Lista de iDs
df = pd.read_csv("data/USERS.csv")
user_ids = df["UserID"].tolist()
print(user_ids)

# Função para retornar o usuário pelo ID.
def get_user(id):
    
  with open("data/mock_users.json", "r", encoding="utf-8") as arquivo:
    users = json.load(arquivo)
    
  for user in users:
        if user["id"] == id:
            return user
  return None

# Buscando os usuários da minha lista de IDs.
users = [user for id in user_ids if (user := get_user(id)) is not None]
print(json.dumps(users, indent=2))


# Cria o cliente da API usando a chave armazenada na variável de ambiente.
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

# Função para gerar as mensagens personalizadas por IA para cada cliente.
def generate_ai_news(user):
  completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
      {
          "role": "system",
          "content": "Você é um especialista em marketing bancário."
      },
      {
          "role": "user",
          "content": f"Crie uma mensagem para {user['name']} sobre a importância dos investimentos (máximo de 100 caracteres)"
      }
    ]
  )
  return completion.choices[0].message.content.strip('\"')

for user in users:
  news = generate_ai_news(user)
  print(news)
  user['news'].append({
      "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
      "description": news
  })

# Função responsável por atualizar o arquivo JSON com todos os usuários de uma única vez.
# Isso evita sobrescrever o arquivo repetidamente.
def update_user(users):
  with open("data/mock_users.json", "w", encoding="utf-8") as arquivo:
     json.dump(users, arquivo, indent=4, ensure_ascii=False)
  return True


success = update_user(users)
print(f"Usuário {user['name']} foi atualizado? {success}!")