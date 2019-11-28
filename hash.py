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
    
    def register():
       
        name = input("Insira seu nome: ")
        occupation = input("Insira sua ocupação: ") 
        password = getpass.getpass("Insira a senha: ")
        
        return [name, password, occupation]

    def generate_key():

        valores = User.register()
        name = valores[0]
        password =  valores[1]
        print(valores)

        value_name = 0
        value_password = 0
        for char in name:
            value_name = value_name + ord(char) 
        for char in password:
            value_password = value_password + ord(char) 
        
        key = value_name + value_password
        
        return key

#####################################################
##Funções da tabela
    def hash(key):
       indice = key % 23
       return indice

    def create_table():
        table = [None]*23
        return table
    
    def insere(user, key, table):
        pos = User.hash(key)
        
        if(table[pos] == None): 
            table.insert(pos,user)
            print(" Inserido HASH {}".format(pos))
        else: 
            print("-> Ocorreu uma colisao na posicao {}" .format(pos))      
       

valor = 0
while(valor <= 1 ):
    usuario = User()
    key = User.generate_key()
    hash = User.hash(key)
    table = User.create_table()
    User.insere(usuario, key, table)
    valor = valor + 1


