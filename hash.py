#import hashlib

#login = input("Insira seu login: ")
#senha = hashlib.md5()

#h = hashlib.md5()
#h.update("uma frase qualquer")
#print h.hexdigest()

import os.path
import getpass
import hashlib

class User:

    def __init__(self, name, occupation):

        self.name = name
        self.occupation = occupation

    def __eq__(self, other):

        return self.name == other.name \
            and self.occupation == other.occupation

    def __str__(self):
        return f'{self.name} {self.occupation}'

    def cadastrar():
        
        existe = os.path.isfile('cadastros.txt')
        name = input("Insira seu nome: ")
        occupation = getpass.getpass("Insira sua ocupação: ") 

        if(existe):
            arquivo = open('cadastros.txt', 'r')
            conteudo = arquivo.readlines()
            conteudo.append("{}, {}\n".format(name, occupation))   # insira seu conteúdo
            arquivo = open('cadastros.txt', 'w') # Abre novamente o arquivo (escrita)
            arquivo.writelines(conteudo)    # escreva o conteúdo criado anteriormente nele.
            arquivo.close()
        else:
            arquivo = open('cadastros.txt', 'w')
            arquivo.write("{} , {}\n".format(name, occupation))
            arquivo.close()

        
       
       

    def checar(login, senha):
        if (u1 == u2):
            print('same user')
            print(f'{u1} == {u2}')
        else:
            print('different users')

valor = 0
while(valor <= 2 ):
    usuario = User.cadastrar()
    valor = valor + 1


