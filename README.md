# API de Gerenciamento de Livros 📚

Uma API simples desenvolvida com Flask para disponibilizar funcionalidades de **consulta**, **criação**, **edição** e **exclusão** de livros.

## Objetivo
Facilitar o aprendizado no desenvolvimento de APIs RESTful utilizando Python e Flask.

## Endpoints Disponíveis

| Método | Endpoint              | Descrição                          |
|--------|-----------------------|------------------------------------|
| GET    | `/livros`             | Retorna todos os livros.          |
| GET    | `/livros/<int:id>`    | Retorna um livro pelo ID.         |
| POST   | `/livros`             | Adiciona um novo livro.           |
| PUT    | `/livros/<int:id>`    | Atualiza as informações de um livro pelo ID. |
| DELETE | `/livros/<int:id>`    | Remove um livro pelo ID.          |

## Recursos
Os recursos disponíveis na API são **livros**, contendo as seguintes propriedades:
- `id`: Identificação única do livro (inteiro).
- `título`: Título do livro (texto).
- `autor`: Autor do livro (texto).

## Como Executar

1. **Clonar o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/api-gerenciamento-livros.git
   cd api-gerenciamento-livros
2. **Instalar dependências: Certifique-se de ter o Python instalado e execute**:
   ```bash
   pip install flask
3. **Execute a aplicação**:
   ```bash
   python app.py

