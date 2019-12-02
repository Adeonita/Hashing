from hashing import Hash

def menu():
    table = User.create_table()

    value = int(input("\nDigite uma das opções abaixo\n\n 1 - Inserir\n 2 - Exibir\n 3 - Procurar\n 4 - Deletar: \n 0 - Sair \n"))
   
    while(value != 0):
        usuario = User()
        if(value == 1):
            key = User.generate_key()
            hash = User.hash(key)
            User.insert_table(usuario, key, table)
        elif(value == 2):
            User.show_table(table)
        elif(value == 3):
            User.search_table(table, key)
        elif(value == 4):
            User.delete_register(table, key)
        elif(value == 0):
            return
        
        
        
menu()