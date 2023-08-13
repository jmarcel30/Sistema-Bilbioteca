cadastro_usuarios = ['thel','marcel', 12345566]
with open('cadastro_usuarios.txt','wt+') as arquivo:
    for valor in cadastro_usuarios:
        arquivo.write(str(cadastro_usuarios)+'\n')