class User:
    idInicial = 0
    usuarios = {}
    log = {}

    def __init__(self, login, senha):
        User.idInicial += 1
        self.id = User.idInicial
        self.login = login
        self.senha = senha
        User.usuarios[login] = senha
        User.log[login] = senha
    
    @staticmethod
    def cadastrar():
        login = input("Escreva seu login\n")
        senha = input("Escreva sua senha\n")
        usuario = User(login, senha)
    
    @staticmethod
    def logar():
        login = input("Escreva seu login\n")
        senha = input("Escreva sua senha\n")
        if login in User.usuarios and User.usuarios[login] == senha:
            print("Logado!")
            User.alterar()
        else:
            print("Login não encontrado.")
    
    @staticmethod
    def alterar():
        ls = input("Trocar a senha ou o login?")
        if ls == "senha":
            senha = input("Digite a senha antiga")
            if User.usuarios[User.log] == senha:
                print("teste")
            
    
def cadLog():

    cl = input("Olá, seja bem vindo!\nEste é um sistema de login, deseja cadastrar ou logar?\nResposta: ")

    if cl.lower() == "cadastrar":
        User.cadastrar()
    else:
        User.logar()
    cl = input("Deseja acessar? s/n \n")
    if cl.lower() == "s":
        cadLog()

cadLog()

for usuario in User.usuarios:
    print(f"ID: {usuario.id}, Nome: {usuario.nome}, Login: {usuario.login}, Senha: {usuario.senha}")