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

    def __init__(self, name, occupation, password):

        self.name = name
        self.occupation = occupation
        self.password = password

    def __eq__(self, other):

        return self.name == other.name \
            and self.occupation == other.occupation

    def __str__(self):
        return f'{self.name} {self.occupation}'

    def register():
       
        name = input("Insira seu nome: ")
        occupation = input("Insira sua ocupação: ") 
        password = getpass.getpass("Insira a senha: ")
        
        value_name = 0
        value_password = 0
        for char in name:
            value_name = value_name + ord(char) 
        for char in password:
            value_password = value_password + ord(char) 
        
        key = value_name + value_password


        return key

    def hash(key):
        indice = key % 23
        print(indice)
        
    
    #def cadastrar():
        
    #    exist = os.path.isfile('cadastros.txt')
    #    name = input("Insira seu nome: ")
    #    occupation = input("Insira sua ocupação: ") 
    #    password = getpass.getpass("Insira a senha: ")
    #    key = name + password
    #    print(key)

    #    if(exist):
    #        arquivo = open('cadastros.txt', 'r')
    #        conteudo = arquivo.readlines()
    #        conteudo.append("{}, {}\n".format(name, occupation))   # insira seu conteúdo
    #        arquivo = open('cadastros.txt', 'w') # Abre novamente o arquivo (escrita)
    #        arquivo.writelines(conteudo)    # escreva o conteúdo criado anteriormente nele.
    #        arquivo.close()
    #    else:
    #        arquivo = open('cadastros.txt', 'w')
    #        arquivo.write("{} , {}\n".format(name, occupation))
    #        arquivo.close()

        
       
       

    def checar(name, occupation, password,):
        if (u1 == u2):
            print('same user')
            print(f'{u1} == {u2}')
        else:
            print('different users')

valor = 0
while(valor <= 2 ):
    usuario = User.register()
    hash = User.hash(usuario)
    
    valor = valor + 1


