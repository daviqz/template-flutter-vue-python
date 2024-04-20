from flask import request, jsonify

def register_account():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    password_confirm = request.form.get('passwordConfirm')
    if not username or not email or not password or not password_confirm:
        return jsonify({'error': 'Todos os campos são obrigatórios'}), 400

    if password != password_confirm:
        return jsonify({'error': 'As senhas não coincidem'}), 400

    # Se todos os dados estiverem corretos, você pode retornar uma resposta de sucesso
    return jsonify({'message': 'Usuário registrado com sucesso'}), 200