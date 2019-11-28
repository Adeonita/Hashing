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
    
    def insert_table(user, key, table):

        pos = User.hash(key)
        if(table[pos] == None): 
            table.insert(pos,user)
            print("\nInserindo HASH {} \n".format(pos-1))
        else: 
            print("\nOcorreu uma colisao na posicao {}" .format(pos-1)) 
        
    def search_table(table, key):
        
        key = int(input("\nDigite um numero para buscar na tabela\n"))
        if(table[key] != None):
            print("\nDado não encontrado\n")
        else:
            print("{}\n".format(User())) #Ver como pegar os atributos


    def delete_register(table, key):

        key = int(input("\nDigite um numero para deletar da tabela\n"))
        if(table[key] != None):
            print("\nImpossível remover, dado não encontrado\n")
        else:
            del(key)
            print("\nRemovido com sucesso\n")




    def show_table(table):
        number = 0
        for line in table:
            print("{}: {} \n".format(number, line))        
            number = number + 1
            
       

valor = 0
table = User.create_table()
while(valor <= 1 ):
    usuario = User()
    key = User.generate_key()
    hash = User.hash(key)
    User.insert_table(usuario, key, table)
    valor = valor + 1
#User.search_table(table, key)
#User.delete_register(table, key)




