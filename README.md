# Projeto de Registro de Gastos Pessoais

Este é um projeto Django para o registro e consulta de despesas pessoais, com suporte para conversão de moedas.

## Funcionalidades

- Registro de Despesas: Adicione, edite e exclua despesas, especificando a descrição, valor, categoria e data.
- Categorias: Organize suas despesas em diferentes categorias.
- Conversão de Moeda: Converta o valor das despesas para diferentes moedas usando uma API de taxas de câmbio.
- Importação de Taxas de Câmbio: Atualize as taxas de câmbio automaticamente a partir de uma API.

## Instalação

### Pré-requisitos

- Python 3.8 ou superior
- Django 5.1 ou superior
- Requests (biblioteca para fazer requisições HTTP)

### Passo a Passo

```bash
1. Clone o repositório:
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

2. Crie e ative um ambiente virtual:
python -m venv env
source env/bin/activate  # No Windows, use `env\Scripts\activate`

3. Instale as dependências:
pip install -r requirements.txt

4. Execute as migrações do banco de dados:
python manage.py migrate

5. Inicie o servidor de desenvolvimento:
python manage.py runserver

6. Acesse o projeto no seu navegador em `http://127.0.0.1:8000/`.
```

## Estrutura do Projeto

- `models.py`: Contém as definições dos modelos `Categoria`, `Despesa` e `TaxaDeCambio`.
- `forms.py`: Contém os formulários para `Categoria` e `Despesa`.
- `views.py`: Contém as views para listagem, criação, atualização e exclusão de despesas e categorias, além da importação de taxas de câmbio.
- `templates/`: Contém os templates HTML para exibição das páginas.
  - `index.html`: Página inicial.
  - `despesa_list.html`: Listagem de despesas com suporte para conversão de moeda.
  - `despesa_form.html`: Formulário para criação e edição de despesas.
  - `categoria_list.html`: Listagem de categorias.
  - `categoria_form.html`: Formulário para criação e edição de categorias.

## Utilização

### Adicionando Despesas

1. Na página de listagem de despesas, clique em "Nova Despesa".
2. Preencha o formulário com a descrição, valor, categoria e data.
3. O valor é armazenado em USD (dólar).

### Convertendo Moedas

1. Na listagem de despesas, insira o código da moeda desejada (por exemplo, `BRL` para Real Brasileiro).
2. Clique em "Converter" para ver as despesas na moeda selecionada.

### Importando Taxas de Câmbio

Acesse a URL `/importar_taxas/` para importar as taxas de câmbio mais recentes via API.
