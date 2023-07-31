#Programando do básico e melhorando
#Após realizar operações metodos, e depois orientado objetos
#Versão linha de comando, versão web, versão mobile
#Escrever 90% de cobertura de testes unitarios e de simulação

#Lista de produto iniciando vazio
lista_produto = []

#Flag para executar o menu repetidas vezes
rodar_programa = True

#Executando enquanto variável for True
while rodar_programa: 

    #Lista de Menu
    print("#########################\n","Digite seu Escolha",end ="\n\n")
    print("1 - Cadastrar Produto")
    print("2 - Lista Produto")
    print("3 - Excluir lista inteira Produtos")
    print("4 - Excluir produto selecionado")
    print("5 - Atualizar Produto")
    print("6 - Sair", end="\n\n")

    #Escolha do usuário - Observo que o retorno é tipo string
    escolha = input("Digite sua escolha : ")

    #Lembra de usar corretamente tratar o erro
    try:
        #Tentando converter tipo string para int
        escolha_numero = int(escolha)

    except:
        print("Digite um valor dentro das opções!",end="\n\n")
        continue
    
    #Condição para cadastrar Produto -- Programar para evitar itens duplicados
    if(escolha_numero == 1):
        print("Cadastro Produto",end="\n")
        #Recebendo do usuário o nome do produto
        nome_produto = input("Digite o nome do Produto:")
        #Adicionado o nome do produto a lista
        lista_produto.append(nome_produto)
        print("Nome do Produto cadastrado:", nome_produto,"\n")

    #COndição para lista Produtos
    elif(escolha_numero == 2):
        if not lista_produto:
            print('Lista vazia !\n')

        else:
            print("Listar Produtos",end="\n\n")
            #listando todos os produtos da lista
            for indice,produto_elemento in enumerate(lista_produto):
                print("Código",indice,"Produto :",produto_elemento)

    #COndição para excluir Produto
    elif(escolha_numero == 3):
        print("Excluir Produto",end="\n\n")
        #limpando a lista
        lista_produto.clear()
        print("Lista Limpa !")
    
    #COndição para excluir produto selecionado
    #Verificar a duplicidade de código e como orientado a objetos ou funções ajudam 
    elif(escolha_numero == 4):
        if not lista_produto:
            print("Lista Vazia !")

        else: 
            print("Excluir Produto Selecionado",end="\n\n")
            #Lista produto
            for indice, produto in enumerate(lista_produto):
                print("Código do Produto:",indice,"Nome do Produto:",produto)
            
            #Recebendo valor em string do código do produto
            codigo_produto_excluido = input("Digite o código do produto que você deseja excluir :")
            
            #Tentando converter tipo string para int 
            try:
                codigo_produto_excluido_inteiro = int(codigo_produto_excluido)

            #Tratamento para coódigo em string ou outro caracter diferente !!!! EU sei que devemos tratar o erros, apenas testes
            except:
                print("Digite um código válido")
                continue

            else:
                #Verifica se o código do produto recebido é maior do que a lista
                if codigo_produto_excluido_inteiro > len(lista_produto):
                    print("Valor não existe na lista")   

                else:
                    #Adicionando indice para ajudar na removoção e evitar erros de digitação 
                    for indice, produto in enumerate(lista_produto):
                        
                        #Procurador por valor na lista e removendo
                        if codigo_produto_excluido_inteiro == indice:
                            lista_produto.remove(lista_produto[indice])
                            print("Item removido")

    #Condição para atualizar produto
    elif(escolha_numero == 5):
       
        #Verificando se a lista esta vazia   
         if not lista_produto:
            print("lista vazia")
         else:
            #listando todos os produtos 
            for indice, produto in enumerate(lista_produto):
                print("codigo:", indice,"nome do produto:", produto)
            print("Atualizar Produto",end="\n\n")
            
            #recebendo codigo do produto que deseja alterar 
            codigo_do_produto = input("digite o valor do codigo que deseja aleterar:")
            try: 

                #convertendo valor do string para inteiro
                codigo_produto_inteiro= int(codigo_do_produto)
            except:
                print("digite algum valor correto")
                continue 
            #verificando se o valor do indice existe
            if codigo_produto_inteiro > len(lista_produto):
                print("valor codigo não existe")

            else:
                #realizando alteração do nome do produto pelo indice
                for indice, produto in enumerate(lista_produto):
                    if indice == codigo_produto_inteiro:
                        lista_produto[indice] = input("digite o novo nome:")

    #COndição para sair
    elif(escolha_numero == 6):
        print("Sair",end="\n\n")
        rodar_programa = False
    
    #COndição digitados fora do esperado
    else:
        print("Digite um valor dentro das opções !",end="\n\n")
