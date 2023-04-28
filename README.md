# Rent.io - aluguel de imóveis

## Projeto TCC sobre mercado imobiliário

### Colaboradores

- [João Manoel](https://github.com/JoaoManoelFontes/)
- [Cauã Alexandre](https://github.com/cauaalexandrefs/)

### Tecnologias utilizadas

- Python
- Django
- HTML
- CSS

#### Como rodar o projeto

- Clone o repositório `git clone https://github.com/JoaoManoelFontes/Rent.io.git`
- Crie um ambiente virtual `python -m venv venv` e ative ele
- Instale as dependências `pip install -r requirements.txt`
- Crie um arquivo .env com as seguintes variáveis de ambiente (de acordo com as suas preferências e seu banco de dados):
  - SECRET_KEY
  - DEBUG
  - ENGINE
  - NAME
  - USER
  - PASSWORD
  - HOST
  - PORT
- Rode as migrações `python manage.py migrate`
- Rode o servidor `python manage.py runserver`
