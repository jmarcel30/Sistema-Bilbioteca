# Linha 
def linha (tam = 42):
    return '-' * tam


#texto cabeçalho
def cabeçalho(txt):
    print(txt.center(42))
    print(linha())


# Menu_entrar
def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leia_int('Sua Opção:')
    return opc
# menu cadastrar 
def identificador(id):
    c = 1 
    for item in id:
        print(f' Id {c}')
        c += 1
        

#Validar menu leia int

def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            cabeçalho('\033[31mERRO por favor, digite um numero válido.\033[m')
            continue
        except(KeyboardInterrupt):
            cabeçalho("\033[31Entrada de dados interrompida pelo usuario\033[m")
            return 0
        else:
            return n 


#Validar menu leia int

def leia_float(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO por favor, digite um numero válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print("\033[31Entrada de dados interrompida pelo usuario\033[m")
            return 0
        else:
            return n     
        


    


def cadastrar(nome, cpf ):
     
     with open('lista.txt','a') as arquivo:
                for valor in cadastrar:
                    arquivo.write(str(cadastrar)+'\n')
       

# pesuisa de livro 
def pesquisar_palavra_arquivo(nome_arquivo, palavra_pesquisa):
    try:
        with open('livros.txt', 'r') as arquivo:
            conteudo = arquivo.read()
            palavras_encontradas = [palavra for palavra in conteudo.split() if palavra.lower() == palavra_pesquisa.lower()]

            if palavras_encontradas:
                print(f"A palavra '{palavra_pesquisa}' foi encontrada {len(palavras_encontradas)} vez(es) no arquivo.")
            else:
                print(f"A palavra '{palavra_pesquisa}' não foi encontrada no arquivo.")
    
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print("Ocorreu um erro ao ler o arquivo:", e)


# contador

def ler_contador():
    try:
        with open("contador.txt", "r") as arquivo:
            return int(arquivo.read())
    except FileNotFoundError:
        return 0

def salvar_contador(contador):
    with open("contador.txt", "w") as arquivo:
        arquivo.write(str(contador))


# Menu - cadastro de livro

def cabeçalho_livro():
    livro_menu = """ 
    Deseja cadastrar um novo livro:

    Sim - [1]
    Não - [2]

"""
    return print(livro_menu)

# Menu psquisa
def cabeçalho_pesquisa():
    pesquisa_menu = """ 
    Deseja fazer uma pesquisa:

    Sim - [1]
    Não - [2]

"""
    return print(pesquisa_menu)


# menu cadastro 

def cabeçalho_cadastroo():
    usuario = """ 
    Deseja fazer um cadastro:

    Sim - [1]
    Não - [2]

"""
    return print(usuario)

def emprestar_menu():
    livro_livro ="""
    Deseja emprestar livros:
    Sim [1]
    Não [2]
    """
    return print(livro_livro)

# menu sair do sistema
def sair_sistema():
    sair = """
    Deseja sair do sistema

    Sim [1]
    Não [2]
  """
    return print(sair)

def menu_genero():
    categoria = """ 
    
    Qual a gênero do livro:
    Romance             [1]
    Fantasia            [2]
    Ficção científica   [3]
    Distopia            [4]
    Ação e aventura     [5]
    Ficção Policial     [6]
    Horror              [7]
    Thriller e Suspense [8]
    Ficção histórica    [9]
    Novela              [10]
    Outra Opção         [11]
                          """
    return print(categoria)



def  qual_sexo():
     sexo = '''
    Qual o Sexo do usuário :

    Masculino [1]
    Feminino  [2]
    Outro     [3]
                '''
     
     return print(sexo)




    
       
    
