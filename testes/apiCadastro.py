import jwt, mysql.connector
from flask import Flask, jsonify, request
from flask_cors import CORS

nicknamesCadastrados = []
tokensCadastrados = []

app = Flask(__name__)
CORS(app)

def rodarComandosECommit(comando):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='gai_register'
    )

    cursor = conexao.cursor()
    cursor.execute(comando)
    conexao.commit()
    conexao.close()
    cursor.close()

def adicionarUsuarioNoBanco(nome:str, nickname:str, token:str):
    comando = f'INSERT INTO usuarios (nomeUsuario, nickUsuario, tokenUsuario) VALUES ("{nome}", "{nickname}", "{token}")'
    rodarComandosECommit(comando)

def lerBanco(nomeParaSerCadastrado, tokenGerado="nada"):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='gai_register'
    )

    cursor = conexao.cursor()

    comando = 'SELECT * FROM usuarios'
    cursor.execute(comando)
    resultados = cursor.fetchall()

    for resultado in resultados:
        if resultado[2] == nomeParaSerCadastrado or resultado[3] == tokenGerado:
            conexao.close()
            cursor.close()
            return True
        else:
            conexao.close()
            cursor.close()
            return False
@app.route('/registro', methods=['POST'])
def registro():
    dados_recebidos = request.get_json(force=True)
    if dados_recebidos:
        nome = dados_recebidos.get('nome')
        nickname = dados_recebidos.get('nickname')
        if nickname in nicknamesCadastrados:
            return  jsonify({'message': "Nickname já cadastrado"})
        nicknamesCadastrados.append(nickname)
        if nome in [None, False, "", " "] or nickname in [None, False, "", " "]:
            print(f"Nome: {nome}, Nickname: {nickname}")
            return jsonify({'message': 'Nome e/ou nickname não encontrado.'}), 400
        else:
            token = jwt.encode({'nome': nome, 'nickname': nickname+nome}, nickname, algorithm='HS256')
            if token in tokensCadastrados:
                return jsonify({'message': "Este nickname já foi cadastrado ou é invalido {token exception}"})
            tokensCadastrados.append(token)
            if lerBanco(nickname,token):
                adicionarUsuarioNoBanco(nome, nickname, token[-300:])
                return jsonify({'token': token}), 200
            else:
                adicionarUsuarioNoBanco(nome, nickname, token[-300:])
                return jsonify({'token': token}), 200
                #return jsonify({"message": "Erro exclusivo!!"})
    else:
        return jsonify({'message': 'Erro ao processar os dados recebidos'}), 400

@app.route('/alterNickname', methods=['POST'])
def alterNickname():
    dados_recebidos = request.get_json(force=True)
    if dados_recebidos:
        novoNick = dados_recebidos.get("novoNick")
        tokenInformado = dados_recebidos.get("token")
        comando = f'UPDATE usuarios SET nickUsuario = "{novoNick}" WHERE tokenUsuario = "{tokenInformado}"'
        rodarComandosECommit(comando)

        return jsonify({'message': "Nickname alterado!"})

@app.route('/deletarUsuario', methods=['POST'])
def deletarUsuario():
    dados_recebidos = request.get_json(force=True)
    if dados_recebidos:
        tokenParaDeletar = "dados_recebidos.get("token")"

        comando = f'DELETE FROM usuarios WHERE tokenUsuario = "{tokenParaDeletar}"'
        rodarComandosECommit(comando)

        return jsonify({'message': "Usuario deletado com sucesso!"})

if __name__ == '__main__':
    app.run(port=5000, host="localhost", debug=True)
