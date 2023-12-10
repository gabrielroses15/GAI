class Usuarios:
    def __init__(self,nome,idade,informaçoes_importantes,nmu,mmu,personalidade,tipo_de_escrita,outros):
        self.nome = nome
        self.idade = idade
        self.informaçoes_importantes = informaçoes_importantes
        self.nmu = nmu
        self.mmu = mmu
        self.personalidade = personalidade
        self.tipo_de_escrita = tipo_de_escrita
        self.outros = outros


    def Perguntar(self):
        import Codigo
        Codigo.Mensagem()


usuario = Usuarios('Vini',12,'Estudante','Sla','Sla','Legal','Sla','Sla')
usuario.Perguntar()