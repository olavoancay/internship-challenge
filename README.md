# Salutho - Desafio Desenvolvimento de Software

Este é um projeto simples de uma calculadora de MMC (Mínimo Múltiplo Comum) desenvolvida usando React para o frontend que inteerage com uma API Django para calcular o menor número inteiro divisível por todos os números dentro de um intervalo determinado pelo usuário.

## Requisitos de Instalação

Para executar este projeto localmente, você precisará das seguintes ferramentas:

- [Node.js](https://nodejs.org/en/download/package-manager)
- npm (geralmente instalado automaticamente com o Node.js)
- Python (3.6 ou superior) [Windows](https://python.org.br/instalacao-windows/) [Mac](https://python.org.br/instalacao-mac/) [Linux](https://python.org.br/instalacao-linux/) 
- pip (geralmente instalado automaticamente com o Python)

## Instalação

Siga estas etapas para configurar o ambiente de desenvolvimento:

#### 1. Abra o terminal, cmd ou powershell

#### 2. Clone este repositório em sua máquina local: 
`git clone https://github.com/olavoancay/internship-challenge.git`

#### 3. Navegue até o diretório backend do projeto: 
`cd internship-challenge/backend/calcula-mmc`

#### 4. Crie um ambiente virtual para o Django: 
`python -m venv venv`

#### 5. Ative o ambiente virtual:

  No Windows: 
`venv\Scripts\activate`

  No macOS/Linux: 
`source venv/bin/activate`

#### 6. Instale as dependências: 
`pip install -r requirements.txt`

#### 7. Navegue até o diretório calcula mmc 
`cd calcula-mmc`

#### 8. Inicie o servidor de desenvolvimento do backend: 
`python manage.py runserver`

#### 9. Abra um novo terminal e navegue até o diretório frontend 
`cd ./frontend`

#### 10. Instale as dependências do frontend: 
`npm install`

#### 11. Inicie o servidor de desenvolvimento do frontend: 
`npm start`

## Utilização

Acesse http://localhost:3000 em seu navegador para interagir com a aplicação. Insira os números no formulário e clique em "Calcular" para obter o MMC.

## Testes

Para executar os testes automatizados do frontend e do backend, você pode usar os seguintes comandos:

#### Testes do frontend:
(Navegue até a pasta 'internship-challenge/frontend' para poder executar os testes)

`npm test`

#### Testes do backend:
(navegue até a página internship-challenge/backend/calcula_mmc para executar o projeto)

`python manage.py test`

#### Para testar backend independentemente

Rode o seguinte código dentro do terminal

`` curl 'http://localhost:8000/api/calcula-mmc-intervalo/?x=1&y=10' ``

# Contato

Se tiver qualquer dúvida, estou a disposição para ajudar

[Linkedin](https://www.linkedin.com/in/olavoancay/)

[Email](olavoancay@hotmail.com)