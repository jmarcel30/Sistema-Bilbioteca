

from validate_email import validate_email
import datetime
import time
from funcoes import *
import pyodbc


dados_conexao = (
    "Driver = {SQL Server};"
    "Server= DESKTOP-J81F335;"
    "Database='dbBibliotecaOnline;")
conexao = pyodbc.connect(dados_conexao)
print('Conexão ok')





    # Menu Principal 

while True:
    
    resposta = menu(['EMPRESTAR  LIVRO', 'CADASTAR   LIVRO', 'PESQUISAR  LIVRO', 'CADASTRAR  LEITOR', 'SAIR DO SISTEMA'])
    
    
    # CADASTRO DE LEITOR 
    
    if resposta == 4:
        
        while True:
            cabeçalho_cadastroo()
            opção = leia_int('Digite sua opção:')
            if opção == 2:
                break
            elif opção == 1:
      
                cabeçalho('***Realizando Operação***')
                time.sleep(2)
                lista_cadstro = []

                nome_cadaastro = (input('Nome do usuário:'))
                lista_cadstro.append(f'None do usuário:{nome_cadaastro}')

                
                #Validação do sexo 
                qual_sexo()
                opção =  leia_int('Qual sua opção:')
                
                if opção == 1:
                    meu_sexo = 'Masculino'
                elif opção == 2:
                    meu_sexo = 'Feminino' 
                elif opção == 3:
                    meu_sexo = 'Outro'       

                meu_sexo 
                lista_cadstro.append(f'Sexo do usuário é {meu_sexo}')
                #CPF usuario
                cpf_usuario = leia_int('Digite se cpf: ')
                lista_cadstro.append(f'CPF do usuário:{cpf_usuario}')
                #TElefone usuária
                telefone = leia_int("Digite seu telefone: ")
                lista_cadstro.append(f'Telefone do usuário:{telefone}')

                #validação do email
                while True:
                    email_usuario = (input("Digite um email: "))
                    if  validate_email(email_usuario):
                        print('Email Válido') 
                        break
                    else:
                        print ('[Email inavalido] Por favor, Digite um email valido')        
                lista_cadstro.append(f'Email do usuário:{email_usuario}')
        
                with open('lista.txt', 'a') as arquivo:
                    for valor in lista_cadstro:
                        arquivo.write(str(valor) + '\n')
                cabeçalho('***Realizando Operação***')
                time.sleep(2)
                cabeçalho('***Salvando cadastro***')
                time.sleep(2)
                cabeçalho('***Cadastro salvo com sucesso***')
                cabeçalho(f"""
                 Nome do usuáro:{nome_cadaastro}
                 Sexo: {meu_sexo}
                 CPF: {cpf_usuario}
                 Telefone: {telefone}
                 Email: {email_usuario} """)
                 
    

    
    # PESQUISA DE LIVRO 
    
    elif resposta == 3:
        while True:
            cabeçalho_pesquisa()
            opção = leia_int('Sua opção:')
            if opção == 2:
                break
            elif opção == 1:
                time.sleep(2)

                arquivo_pesquisa = "livros.txt"
                palavra_pesquisa = input("Digite o nome do livro que deseja pesquisar: ")
                pesquisar_palavra_arquivo(arquivo_pesquisa, palavra_pesquisa)
        

        
        
    
    # CADASTRO LIVRO 

    elif resposta == 2:
        while True:
            cabeçalho_livro()
            opção = leia_int('Sua opção: ')
            if opção == 2:
                break
                
            elif opção == 1:

                cabeçalho('***Realizando Operação***')
                time.sleep(2)
                #Contador de livros 
                contador = ler_contador()
                #print(f"Contagem atual: {contador}")g

                for i in range(contador + 1, contador + 2):
                #print(i)
                    contador = i

                salvar_contador(contador)

                # cadastro de livros 
    
                
                cadastro_livro = []
                menu_genero()
                opção = leia_int('Sua Opção:')
                if opção == 1:
                    categoria = 'Romance'
                elif opção == 2:
                    categoria = "Fantasia"
                elif opção == 3:
                    categoria = 'Ficção científica'
                elif opção == 4:
                    categoria = 'Distopia' 
                elif opção == 5:
                    categoria = 'Ação e aventura'
                elif opção == 6:
                    categoria = 'Ficção Policial'
                elif opção == 7:
                    categoria = 'Horror'
                elif opção == 8:
                    categoria = 'Thriller e Suspense' 
                elif opção == 9:
                    categoria = 'Ficção histórica'
                elif opção == 10:
                    categoria = 'Novela'     
                elif opção == 11:
                    categoria = input('Digite outra opção:')
                   



                print(f'Categoria do livro: {categoria}')
                nome_livro = (input('Nome do livro: '))
                nome_autor = (input('Autor:' ))
                cabeçalho('O livro tem Co autor  Sim - [1] Não - [2]')
                opção = leia_int('Digite sua opção:')
                if opção == 1:
                    co_auotor = str(input('Co autor:'))
                    
                data_cadastro = datetime.datetime.now()    
                cadastro_livro.append(f'id:{contador}')
                categoria = ''
                co_auotor = ''
                cadastro_livro.append(f'Livro cadastrado:{nome_livro}')
                cadastro_livro.append(f'Nome do autor:{nome_autor}')
                cadastro_livro.append(f'Categoria do livro:{categoria}')
                cadastro_livro.append(f'Co autor do livro:{co_auotor}')
                cadastro_livro.append(f'Data do cadastro:{data_cadastro}')
                
                

                with open('livros.txt', 'a') as arquivo:
                    for valor in cadastro_livro:
                        arquivo.write(str(valor) + '\n')
                
                cabeçalho(f'''Nome do livro:{nome_livro}
                              Nome Autor:{nome_autor}
                              Nome Co autor:{co_auotor}
                              Data de cadastro:{data_cadastro}
                              Cadastro do livro: nº{contador}
                              
                              ''')
                time.sleep(2)
                cabeçalho('***Realizando Operação***')
                time.sleep(2)
                cabeçalho('***Salvando livro***')
                time.sleep(2)
                cabeçalho('***Livro cadastrado com sucesso***')


# EMPRESTIMO DE LIVRO  
    elif resposta == 1:
        while True:
            emprestar_menu()
            opção = leia_int('Digite sua opção:')
            if opção == 2:
                break
           
            elif opção == 1:
                emprestimo = []
                data = datetime.datetime.now()
                emprestimo.append(input('Nome do usuário:'))
                emprestimo.append(input('Nome do livro:'))
                emprestimo.append(f'{data}')

                cabeçalho(f"Data do emprestimo n/ {data}")
                cabeçalho(f'')

                cabeçalho('***SALVANDO NO SISTEMA***')
                time.sleep(2)
                cabeçalho('***OPERAÇÃO CONCLUIÍA***')

        

        

     



# SAIR DO SISTEMA  

    if resposta == 5:
        sair_sistema()
        sair = leia_int('sua opção:')
        
        if sair == 1:
            cabeçalho('***Realizando Operação***')
            time.sleep(2)
            cabeçalho('***Saindo do sistema***')
            time.sleep(3)
 
            break
        elif sair == 2:
            time.sleep(2)
            cabeçalho('Voltando ao sistema')
            time.sleep(2)


        
        
 
   
 

        

       
    
        
        
    
        

      

      
           

   
        
    

               

    
        
                      

                       

                              
                                
                                
                        



                               
            
            
        
        
        









      
      
          
    

    
    

    
    

    

    
   

    


    
    
        

    
        
        
        

   




    

    

    


        



   
   

    
   
        