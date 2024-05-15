
#arquivo = open('C:\\Temp\\emack.csv', 'r')
arquivo = open('C:\\Users\\Pedro Gabriel\\Documents\\Mackenzie\\Materias\\1semestre\\Algoritmos e programação\Algoritmos-Projeto-2-Pedro\\emack.csv', 'r')
#conteudo = arquivo.read()
#inicialização das listas 
ids =[]
titles = []
prices = []
listPrices =[]
categories = []
isBestSeller = []
boughtLastMonth = []

#função contendo o menu
def menu():
    num = 0
    # faz a repetição do até o usuario escolher sair
    while(num != 7 ):
        #impresão da lista de opções
        print()
        print("[1] - Quantidade de Produtos por Categoria")
        print("[2] - Percentual de Produtos por Categoria")
        print("[3] - Proporçãode Best Sellers por Categoria")
        print("[4] - Os 10 produtos mais baratos e mais caros")
        print("[5] - Gerar relatório HTML de produtos por Categoria")
        print("[6] - Gerar relatório HTML com os Top 10 Best-sellers")
        print("[7] - Sair")
        print()

        #Recebe o input do usuario
        num = int(input("Digite a opção que deseja: "))
        #Para o loop 
        if(num == 7):
            break
        #Faz a checagem da opção inputada
        if(num == 1):
            #Opção um
            categoryCount(categories)
        elif(num == 2):
            #opção 2
            bestSelerCount(categories, isBestSeller)
            print()
        elif(num == 3):
            #opção 3
            print()
        elif(num == 4):
            #opção 4
            print()
        elif(num == 5):
            #opção 5
            print()
        elif(num == 6):
            #opção 6
            print()
        else:
            #se nemnhum opção for valida pede para o usuario digital algo valido
            print("Digite uma oção valida!!!")
#Função que faz a contagem das categorias
def categoryCount(categories):
    # inicialização das variaveis
    livros= 0
    moda=0
    casa=0
    esporte = 0
    elec=0
    #Faz a checagem de cada membro da lista de categorias e contabiliza elas pra cada categoria
    for n in categories:
        if(n == "Livros"):
            livros += 1
        if(n == "Moda"):
            moda += 1
        if(n == "Casa"):
            casa += 1
        if(n == "Esportes"):
            esporte += 1
        if(n == "EletrÃ´nicos"):
            elec += 1

    #Imprime os resultados de cada categoria
    print()
    print("Quantidade de itens livros: ", livros)
    print("Quantidade de itens Moda: ", moda)
    print("Quantidade de itens Casa: ", casa)
    print("Quantidade de itens esportes: ", esporte)
    print("Quantidade de itens eletronicos: " ,elec)

def bestSelerCount(categories, isBestSeller):
    # inicialização das variaveis
    livros= 0
    bestSellerLivro =0
    moda=0
    bestSellerModa = 0
    casa=0
    bestSellerCasa = 0
    esporte = 0
    bestSellerEsporte = 0
    elec=0
    bestSellerElec = 0

    #Faz a separação por categoria e depois checa se é bestseller ou não
    for i in range(len(categories)):
        if(categories[i] == "Livros"):
            livros += 1
            if(isBestSeller[i] == "true"):
                bestSellerLivro += 1
        if(categories[i] == "Moda"):
            moda += 1
            if(isBestSeller[i] == "true"):
                bestSellerModa += 1
        if(categories[i] == "Casa"):
            casa += 1
            if(isBestSeller[i] == "true"):
                bestSellerCasa += 1
        if(categories[i] == "Esportes"):
            esporte += 1
            if(isBestSeller[i] == "true"):
                bestSellerEsporte += 1
        if(categories[i] == "EletrÃ´nicos"):
            elec += 1
            if(isBestSeller[i] == "true"):
                bestSellerElec += 1

    #Imprime os resultados de cada categoria
    print()
    print("Quantidade de livros Best-Sellers por total de Livros: ", (bestSellerLivro*100)//livros, "%")
    print("Quantidade de artigos de moda Best-Sellers pelo total: ", (bestSellerModa*100)//moda, "%")
    print("Quantidade de artigos de Casa Best-Sellers  pelo total: ", (bestSellerCasa*100)//casa, "%")
    print("Quantidade de itens esportivos Best-Sellers pelo total: ", (bestSellerEsporte*100)//esporte, "%")
    print("Quantidade de eletronicos Best-Sellers  pelo total: ", (bestSellerElec*100)//elec, "%")


#Monta as lista de cada tipo com as infoirmações do arquivo
for linha in arquivo:
     linha = linha.split(",")
     #print(linha)
     ids.append(linha[0])
     titles.append(linha[1])
     prices.append(linha[2])
     listPrices.append(linha[3])
     categories.append(linha[4])
     isBestSeller.append(linha[5])
     boughtLastMonth.append(linha[6])

#Delata oa primeiros itens de cada lista
del(ids[0])
del(titles[0])
del(prices[0])
del(listPrices[0])
del(categories[0])
del(isBestSeller[0])
del(boughtLastMonth[0])


#Cham a função que faz o menu e loop
menu()
