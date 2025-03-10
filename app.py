from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados iniciais de exemplo
livros = [
    {
        'id': 1,
        'título': 'Iludidos pelo acaso',
        'autor': 'Nassim Taleb'
    },
    {
        'id': 2,
        'título': 'As regras de ouro',
        'autor': 'Napoleon Hill'
    },
    {
        'id': 3,
        'título': 'Hábitos atômicos',
        'autor': 'James Clear'
    }
]

# Endpoint para consultar todos os livros
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros), 200

# Endpoint para consultar um livro por ID
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro), 200
    return jsonify({'erro': 'Livro não encontrado'}), 404

# Endpoint para editar um livro por ID
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice]), 200
    return jsonify({'erro': 'Livro não encontrado'}), 404

# Endpoint para criar um novo livro
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    if 'id' not in novo_livro or 'título' not in novo_livro or 'autor' not in novo_livro:
        return jsonify({'erro': 'Dados inválidos'}), 400
    livros.append(novo_livro)
    return jsonify(novo_livro), 201

# Endpoint para excluir um livro por ID
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            return jsonify({'mensagem': 'Livro excluído com sucesso'}), 200
    return jsonify({'erro': 'Livro não encontrado'}), 404

# Executar o aplicativo
if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
