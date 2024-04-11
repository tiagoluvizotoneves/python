# VotingApp - Aplicação de Enquetes com Django

## Sobre o Projeto

`VotingApp` é uma aplicação web desenvolvida com o framework Django, que permite aos usuários criar, votar e ver os resultados de enquetes. Este projeto faz parte do meu portfólio de projetos Python, demonstrando o uso do Django para desenvolvimento web e a integração com um banco de dados MySQL.

## Funcionalidades

- **Criação de Enquetes:** Os usuários podem criar enquetes com várias opções de resposta.
- **Votação:** Os usuários podem votar nas enquetes disponíveis.
- **Resultados:** Após votar, os usuários podem ver os resultados das enquetes.

## Tecnologias Utilizadas

- **Django:** Framework web para o desenvolvimento do backend.
- **MySQL:** Sistema de gerenciamento de banco de dados.
- **Bootstrap/Materialize CSS:** Para estilização das páginas web.

## Como Executar

Para rodar esta aplicação localmente, siga os passos abaixo:

1. **Clone o Repositório:**
git clone deste repositório
cd python/VotingApp

2. **Configure o Ambiente Virtual:**
python3 -m venv env
source env/bin/activate

3. **Instale as Dependências:**
pip install -r requirements.txt

4. **Crie e Configure o Banco de Dados:**
- Certifique-se de que o MySQL está instalado e rodando.
- Crie um banco de dados MySQL e atualize as configurações em `voting_project/settings.py`.

5. **Execute as Migrações:**
python manage.py migrate

6. **Crie um Superusuário (opcional):**
python manage.py createsuperuser

7. **Inicie o Servidor de Desenvolvimento:**
python manage.py runserver

8. **Acesse a Aplicação:** Abra um navegador e visite `http://127.0.0.1:8000/`.

Para acessar o admin http://127.0.0.1:8000/admin/ (use o superuser)

## Contribuições

Contribuições são sempre bem-vindas! Por favor, leia o guia de contribuições para saber como começar.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
