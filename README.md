# Devameet Python

## Description
Este projeto  foi desenvolvido em Python , baseado numa fusao do Meet da Google com o Gather, o Devameet.
Os protótipos e regras do negocioestao nest link do figma:
 https://www.figma.com/file/mIXcu8SJWqi0ylVHtZn89a/Devameet-(Projeto-2023)

## Tecnologias

* Python
* FastAPI (framework web em Python)
* Docker (para empacotar e distribuir a aplicação)
* PostgreSQL (banco de dados relacional)
* WebSocket (para comunicação em tempo real)
* WebRTC (para streaming de áudio e vídeo)

## Features
* Cadastro de usuários
* Autenticação de usuários (login/logout)
* Criação, edição e exclusão de salas de reunião
  
## Instalation
1. Clone o repositório:
```
git clone <git@github.com:Elianehenri/Devameet_Python.git>
````
2. Navegue até o diretório do projeto:
 ````
   cd devameet
````
3. Crie e ative um ambiente virtual:
 ````
   python3 -m venv venv
   source venv/bin/activate
````
4. Instale as dependências:
 ````
   pip install -r requirements.txt
````
5. Execute o aplicativo:
````
   uvicorn main:app --reload
````
6. Executar o docker:
````
    docker-compose up -d
````
7. Fazer uma copia do arquivo `.env.example` e renomear o novo arquivo de `.env.local`
8. configurar as variáveis de ambiente no arquivo `.env.local`



### Autor
* **Eliane Henriqueta**
