import getpass
import hashlib

class User:
    
    
    def register():
       
        name = input("Insira seu nome: ")
        occupation = input("Insira sua ocupação: ") 
        password = getpass.getpass("Insira a senha: ")
        
        return [name, password, occupation]
    
    def generate_hash(valores):
        password = valores[1]
        hash_password = hashlib.md5(password.encode('utf-8'))

        return hash_password.hexdigest()
    
   
    def authenticate(table):
        authenticate_name = input("Insira seu Login: ")
        authenticate_password = input("Insira sua senha: ")

        for n in table:
            if n != None:
                if n[0] == authenticate_name and User.generate_hash(n[1]) == User.generate_hash(authenticate_password):                    
                    print("\nUsuário autenticado\n")
                else:
                    print("\nUsuário não autenticado\n")



    def generate_key(valores):

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
    
    def insert_table(valores, key, table):
        pos = User.hash(key)
            
        if(table[pos] == None): 
            table.insert(pos,valores)
            print("\nInserindo HASH {} \n".format(pos))
        else: 
            print("\nOcorreu uma colisao na posicao {}" .format(pos)) 
        
        
    def search_table(valores, table, key):
        #valores = User.register()
        name = valores[0]
        occupation = valores[2]
        key = int(input("\nDigite um numero para buscar na tabela\n"))
        
        if(table[key] != None):
            print("\nDado não encontrado\n")
        else:
            print("{} - {}\n".format(name, occupation)) 

    def delete_register_name(values, table, name):
        name = valores[0]
        search_name = input("Digite um nome para deletar da tabela: ")

        for n in table:
            if n != None:
                if n[0] == search_name:
                    del(n)
                    print("\nRemovido com sucesso\n")
                else:
                    print("\nImpossível remover. Não há registros com esse índice\n")


    def delete_register_key(valores, table, name):
        key = int(input("\nDigite um numero para deletar da tabela\n"))
        if(table[key] == None):
            print("\nImpossível remover. Não há registros com esse índice\n")
        else:
            del(key)
            print("\nRemovido com sucesso\n")


    def show_table(table):
        number = 0
        for line in table:
            print("{}: {} \n".format(number, line))        
            number = number + 1
    
    def factor_of_ocupation(table):
        occupied_spaces = 0
        size = len(table)
        
        number = 0
        for line in table:
            if(line != None):
                occupied_spaces = occupied_spaces + 1
        factor_of_ocupation = occupied_spaces/size

        return factor_of_ocupation   
                




valor = 0
table = User.create_table()

    
while(valor <= 1 ):
    usuario = User()
    valores = User.register()
    key = User.generate_key(valores)
    
    #hash = User.hash(key)
    User.insert_table(valores, key, table)
    valor = valor + 1
    User.authenticate(table)
#User.search_table(table, key)
#User.show_table(table)
#User.delete_register_name(valores, table, key)
#factor_of_ocupation = User.factor_of_ocupation(table)
#print("O fator de ocupação da tabela é de {}".format(factor_of_ocupation))
#print("A quantidade de acessos é {}".format(acess))





