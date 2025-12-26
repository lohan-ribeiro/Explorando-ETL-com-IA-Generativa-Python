# Explorando ETL Com IA Generativa

Implementação de um pipeline ETL inteligente em Python utilizando IA Generativa para transformar e enriquecer dados de forma automatizada.

## 🚀 Tecnologias Utilizadas

Python 3.13+ | 
[Requests](https://requests.readthedocs.io/en/latest/) | 
[OpenAI](https://platform.openai.com/docs/api-reference/introduction) | 
[Pandas](https://pandas.pydata.org/docs/getting_started/index.html) | 
[Dotenv](https://www.dotenv.org/docs/)    

## 🎯 Objetivo

Desenvolver um fluxo ETL(Extração, Transformação e Carregamento)  e utiliza IA Generativa para criar mensagens personalizadas para cada usuário.

#### Extração (E)
Ler o arquivo USERS.csv e carregar os IDs dos usuários.

#### Transformação (T)
Para cada usuário, gerar uma mensagem de marketing personalizada usando a API do ChatGPT (OpenAI).
A mensagem deve:

Falar sobre investimentos, ser amigável, ser personalizada conforme o perfil do cliente.

#### Carregamento (L)
Atualizar o arquivo USERS.csv, adicionando a nova coluna com as mensagens personalizadas geradas pela IA, substituindo o conteúdo anterior ou atualizando registros existentes.

## 📚 Estrutura do Projeto

```
web_crawler_hn/  
├── src/  
│   ├── main.py           Inicia o programa.
├── data/
|   ├── USERS.csv         Armazenamento dos IDs.
│   └── mock_users.json   Responsável por armazenar os dados.
├── requirements.txt      Requisitos para rodar o programa.
├── README.md  
├── .gitignore
├── .env                  Variáveis de Ambiente.
└── LICENSE
```

## 🔧 Como Executar
```
python -m venv venv  
source venv/bin/activate  # Linux/macOS  
venv\Scripts\activate     # Windows  

pip install -r requirements.txt  
python src/main.py
```
## ⚠️ Aviso

Todos os dados usando neste projeto são fictícios e utilizados apenas para fins educacionais. 