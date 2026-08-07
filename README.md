# Explorando ETL Com IA Generativa

Implementação prática de um pipeline de dados **ETL (Extract, Transform, Load)** inteligente. O projeto extrai dados de clientes, utiliza a API de IA Generativa da OpenAI para criar mensagens de marketing ultra-personalizadas com base no perfil de cada usuário e atualiza a base de dados final.
<br></br>

## 🚀 Tecnologias Utilizadas

Python 3.13+ | 
[Requests](https://requests.readthedocs.io/en/latest/) | 
[OpenAI](https://platform.openai.com/docs/api-reference/introduction) | 
[Pandas](https://pandas.pydata.org/docs/getting_started/index.html) | 
[Dotenv](https://www.dotenv.org/docs/)    
<br></br>

## 🎯 Objetivo

Desenvolver um fluxo ETL(Extração, Transformação e Carregamento)  e utiliza IA Generativa para criar mensagens personalizadas para cada usuário.
<br></br>

## 🎯 O Fluxo ETL
```mermaid
graph TD
    A[Extração: CSV/JSON] --> B[Transformação: Prompt OpenAI]
    B --> C[Carregamento: Salvar de volta no CSV]
````

### Extração (Extract)
O pipeline lê os dados brutos a partir de um arquivo USERS.csv ou mock_users.json, mapeando informações cruciais como:
- ID do Usuário
- Nome
- Perfil de Investidor (ex: Conservador, Moderado, Arrojado)
- Saldo em Conta

### Transformação (Transform)
Para cada usuário extraído, o sistema monta um prompt dinâmico e faz uma requisição à API do ChatGPT (OpenAI). A IA gera um conselho de investimento personalizado e amigável:

> "Olá [Nome], vimos que você tem um perfil [Perfil]. Que tal conhecer nossas opções de..."

### Carregamento (Load)
Os dados transformados (mensagens personalizadas) são injetados de volta no arquivo USERS.csv, gerando uma nova coluna contendo o retorno enriquecido pela IA.
<br></br>

## 📚 Estrutura do Projeto
```
etl-ia-generativa-python/  
├── src/  
│   └── main.py           # Script principal que executa o fluxo ETL
├── data/
│   ├── USERS.csv         # Base de dados de usuários final (atualizada pelo pipeline)
│   └── mock_users.json   # Dados fictícios para testes locais
├── .env.example          # Exemplo de configuração das variáveis de ambiente
├── .gitignore            # Proteção para não subir a API Key e venv
├── requirements.txt      # Dependências do projeto
└── README.md             # Documentação do projeto
```

## 🔧 Como Executar

### Pré-requisitos
Antes de começar, você precisará ter o Python 3.13+ instalado e uma API Key da OpenAI.

1. Clonar o repositório
````bash
git clone https://github.com/seu-usuario/etl-genai-python.git
````

2. Configurar Variáveis de Ambiente
Crie um arquivo .env na raiz do projeto baseado no .env.example e adicione sua chave de API da OpenAI:

````env
OPENAI_API_KEY=sua_chave_aqui_projeto
````

3. Configurar o Ambiente Virtual (Virtualenv)
```bash
# Criar o ambiente virtual
python -m venv venv
 
# Ativar o ambiente

# No Linux/macOS:
source venv/bin/activate

# No Windows (PowerShell):
venv\Scripts\Activate.ps1
# No Windows (bash):
venv\Scripts\activate
```

4. Instalar as Dependências
````bash
pip install -r requirements.txt
````

5. Executar o Pipeline
````bash
python src/main.py
````

## ⚠️ Aviso

Todos os dados usando neste projeto são fictícios e utilizados apenas para fins educacionais. 
