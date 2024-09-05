# Projeto  fastAPI
## Descrição do Projeto
Este projeto faz parte da disciplina Desenvolvimento Rápido de Aplicações (RAD) e consiste no desenvolvimento de um sistema monolítico utilizando o framework FASTAPI em Python. O projeto tem como objetivo criar uma aplicação robusta e escalável, seguindo as melhores práticas de desenvolvimento. Além disso, o Docker será utilizado para facilitar a configuração e o ambiente de desenvolvimento, garantindo a portabilidade da aplicação.

# Funcionalidades
Autenticação e Autorização: Sistema de login e controle de acesso.
CRUD Completo: Operações de Create, Read, Update, e Delete para gerenciamento de recursos.
Validação de Dados: Uso de Pydantic para garantir a integridade dos dados.
Documentação Automática: Geração automática da documentação da API com Swagger e Redoc.
Banco de Dados Relacional: Integração com [Nome do Banco de Dados, e.g., PostgreSQL].
Containerização com Docker: Ambientes de desenvolvimento e produção configurados via Docker.
Testes Automatizados: Utilização de Pytest para garantir a qualidade do código.
#Tecnologias Utilizadas
Python 3.10+
FASTAPI
Uvicorn
SQLAlchemy
Pydantic
Alembic
Pytest
Docker & Docker Compose
PostgreSQL

# Instalação e Configuração
## 1. Clonando o Repositório

`git clone https://github.com/seu-usuario/seu-repositorio.git` <br>
`cd seu-repositorio`

## 2. Configuração com Docker
Certifique-se de ter o Docker e o Docker Compose instalados na sua máquina. Para iniciar o ambiente de desenvolvimento:

`docker-compose up --build`

Isso irá construir a imagem do Docker e iniciar os containers definidos no docker-compose.yml.

## 3. Acessando a Aplicação
A aplicação estará disponível em http://127.0.0.1:8000. A documentação da API estará disponível em http://127.0.0.1:8000/docs para Swagger e http://127.0.0.1:8000/redoc para Redoc.

## 4. Executando Migrações de Banco de Dados
Após subir os containers, execute as migrações para configurar o banco de dados:

`docker-compose exec web alembic upgrade head`
# Uso
Descreva aqui como utilizar a API, incluindo exemplos de endpoints, payloads de requisição e respostas esperadas.

## Exemplo de Requisição

`curl -X POST "http://127.0.0.1:8000/items/" -H "Content-Type: application/json" -d '{"name": "item1", "description": "A simple item"}'`
## Exemplo de Resposta

`{
  "id": 1,
  "name": "item1",
  "description": "A simple item"
}`

# Contribuição
Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto.
2. Crie uma branch para a sua feature (git checkout -b feature/AmazingFeature).
3. Faça commit das suas alterações (git commit -m 'Add some AmazingFeature').
4. Envie para o repositório remoto (git push origin feature/AmazingFeature).
5. Abra um Pull Request.
# Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.
