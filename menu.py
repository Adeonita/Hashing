valor = 0
usuario = User()
table = usuario.create_table()

    
while(valor <= 1 ):

    valores = usuario.register()
    key = usuario.generate_key(valores)
    
    usuario.insert_table(valores, key, table)
    factor_of_ocupation = usuario.factor_of_ocupation(table)
    print("O fator de ocupação da tabela é de {}".format(factor_of_ocupation))

    valor = valor + 1
    usuario.authenticate(table)
    usuario.search_table(valores, table, key)
    usuario.show_table(table)
    usuario.delete_register_name(valores, table, key)
