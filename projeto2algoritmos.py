'''
Trabalho 2 - Algoritmo e Programação
Integrantes:
Felipe Bertacco Haddad
Pedro Gabriel
'''

arquivo = open("C:/Users/Felipe/Desktop/Faculdade/Algoritmo e Programação I/Prática/Trabalho 2/emack.csv", 'r')
#arquivo = open('C:\\Users\\Pedro Gabriel\\Documents\\Mackenzie\\Materias\\1semestre\\Algoritmos e programação\Algoritmos-Projeto-2-Pedro\\emack.csv', 'r')
# para abrir no PC do Haddad: "C:/Users/Felipe/Desktop/Faculdade/Algoritmo e Programação I/Prática/Trabalho 2/emack.csv"
#conteudo = arquivo.read()
#inicialização das listas 
ids =[]
titles = []
prices = []
listPrices =[]
categories = []
isBestSeller = []
boughtLastMonth = []

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

arquivo.close()

#Deleta oa primeiros itens de cada lista
del(ids[0])
del(titles[0])
del(prices[0])
del(listPrices[0])
del(categories[0])
del(isBestSeller[0])
del(boughtLastMonth[0])
boughtLastMonth = [item[:-1]for item in boughtLastMonth]


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
            categorypercent(categories)
            print()
        elif(num == 3):
            #opção 3
            bestSelerCount(categories, isBestSeller)
            print()
        elif(num == 4):
            #opção 4
            func3(prices, titles)
            print()
        elif(num == 5):
            relatorioHTML(categories, titles)
            #opção 5
            print()
        elif(num == 6):
            relatorioHTML2(boughtLastMonth, titles, isBestSeller, categories)
            #opção 6
            print()
        else:
            #se nemnhum opção for valida pede para o usuario digital algo valido
            print("Digite uma oção valida!!!")

#item a
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


#Item b)
def categorypercent(categories):
    # Utiliza-se o mesmo loop do item a) para conseguir a quantidade
    # de produtos em cada categoria
    livros= 0
    moda=0
    casa=0
    esporte = 0
    elec=0
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
    #Estabelece um total que será utilizado para calcular a porcentagem
    total = livros+moda+casa+esporte+elec
    # Ja da print convertendo os números em porcentagem
    print("livros:",(livros/total)*100,"%\nModa:",(moda/total)*100,"%\nCasa:",
          (casa/total)*100,"%\nEsportes:",(esporte/total)*100,"%\nEletrônicos:",
          (elec/total)*100,"%")

#item c
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

#Item d)
def func3(prices, titles):
    #Lista das Categorias dos produtos mais caros
    tipocaros = []
    #Lista das Categorias dos produtos mais baratos
    tipobaratos = []
    #Lista dos números dos Produtos mais caros
    nomecaros = []
    #Lista dos números dos Produtos mais caros
    nomebaratos = []
    
    #Lista dos 10 primeiros preços da lista de preços
    maiscaros = [4583.44, 2572.77, 116.25, 3852.24, 3644.64, 2433.12, 4856.16, 
                3874.23, 1495.57, 3836.43]
    #Lista dos 10 primeiros preços da lista de preços
    maisbaratos = [4583.44, 2572.77, 116.25, 3852.24, 3644.64, 2433.12, 4856.16, 
                3874.23, 1495.57, 3836.43]
    
    #Loops servem para Listar os maiores e menores preços das listas
    for i in range (len(prices)):
        for a in range (len(maiscaros)):
            #Define a lista dos mais caros
            if float(prices[i]) > float(maiscaros[a]):
                maiscaros[a] = prices[i]
                break
            #Define a lista dos mais baratos
            if float(prices[i]) < float(maisbaratos[a]):
                maisbaratos[a] = prices[i]
                break
    #Define o número e categoria dos produtos mais caros
    for i in range (len(maiscaros)):
        pos = prices.index(maiscaros[i])
        nomecaros.append(titles[pos])
        tipocaros.append(categories[pos])
    #Define o número e categoria dos produtos mais baratos
    for i in range (len(maisbaratos)):
        pos = prices.index(maisbaratos[i])
        nomebaratos.append(titles[pos])
        tipobaratos.append(categories[pos])
    print(nomecaros)
    print(maiscaros)
    print(nomebaratos)
    print(maisbaratos)
    print(tipocaros)
    print(tipobaratos)

#item e)
def relatorioHTML(categories, produtos):
     aux= ""
     while(aux != "Livros" and aux != "Moda" and aux != "Casa" and aux != "Esportes" and aux != "EletrÃ´nicos"):
          aux = input("Digite uma categoria(Livros, Moda, Casa, Esportes,EletrÃ´nicos)")
          
     caminho =  f"C:\\Temp\\Algoritmos-Projeto-2-Pedro\\Algoritmos-Projeto-2-Pedro\\relatorio_produtos_{aux}.html"
     #caminho =  f"C:\\Users\\Pedro Gabriel\\Documents\\Mackenzie\\Materias\\1semestre\\Algoritmos e programação\Algoritmos-Projeto-2-Pedro\\relatorio_produtos_{aux}.html"
     relatorio = open(caminho, 'w')
     
     relatorio.write("<html>")
     relatorio.write("<head>")
     relatorio.write(f"<title> Relatorio Produtos {aux} </title>")
     relatorio.write("</head>")
     relatorio.write("<body>")
     relatorio.write("<div>")
     relatorio.write(f"<h1>Relatorio Produtos {aux}</h1>")
     relatorio.write("<ul>")
     relatorio.write(f"{aux}")
     for i in range(len(categories)):
        if(categories[i] == aux):
            relatorio.write(f"<li> {produtos[i]} </li> <br\> ")
            

            relatorio.write("\n")

     relatorio.write("</ul>")
     relatorio.write("</div>")
     relatorio.write("</body>")
     relatorio.write("</html>")

     relatorio.close()

#item f)
def relatorioHTML2(boughtLastMonth, titles, isBestSeller, categories):
    #livros
    dic1 = {}
    dic2 = {}
    dic3 = {}
    dic4 = {}
    dic5 = {}
    livrotop10 = []
    modatop10 = []
    casatop10 = []
    esportetop10 = []
    eletronicotop10 = []
    categ = ["Livros","Moda","Casa","Esportes","EletrÃ´nicos"]
    listas1 = [livrotop10, modatop10, casatop10, esportetop10, eletronicotop10]
    dics = [dic1, dic2, dic3, dic4, dic5]
    def func1(categ):
        for i in range (len(categories)):
            # Define a lista que ele esta fazendo
            for d in range(5):
                if categories[i] == categ[d] and isBestSeller[i] == "true":
                    if len(listas1[d]) < 10:
                        listas1[d].append(boughtLastMonth[i])
                    else:
                        #Definição menor numero
                        menor = (listas1[d][0])                        
                        for b in range(10):
                            if int(listas1[d][b]) < int(menor):
                                menor = listas1[d][b]  
                        # Substituição do menor numero pelo numero externo
                        if int(boughtLastMonth[i]) > int(menor):
                            indicemenor = listas1[d].index(menor)
                            listas1[d][indicemenor] = boughtLastMonth[i]
                            break 
        for i in listas1:
            i.sort(reverse=True)
            
    func1(categ)
    
    def func2(listas1):
        # loop pra fazer os 5 dicionários
        for c in range(5):
            # loop para colocar os 10 elementos dentro do dicionário
            for v in listas1[c]:
                pos = boughtLastMonth.index(v)
                dics[c][f"{titles[pos]}"] = v
                
    func2(listas1)
    

    for produto in dic1:
        print(produto)
     
    relatorio = open('C:\\Temp\\relatorio_bestseller.html', 'w')
    relatorio.write("<html>")
    relatorio.write("<head>")
    relatorio.write("<title> Relatorio Bestseller </title>")
    relatorio.write("</head>")
    relatorio.write("<body>")
    relatorio.write("<div>")
    relatorio.write("<h1>Relatorio Bestseller</h1>")

    relatorio.write("<h2>Livros</h2>")
    relatorio.write("<ul>")
    for produto in dic1:
        relatorio.write(f"<li> {produto} </li> <br/> ")
    relatorio.write("</ul>")

    relatorio.write("<h2>Moda</h2>")
    relatorio.write("<ul>")
    for produto in dic2:
        relatorio.write(f"<li> {produto} </li> <br/> ")
    relatorio.write("</ul>")

    relatorio.write("<h2>Casa</h2>")
    relatorio.write("<ul>")
    for produto in dic3:
        relatorio.write(f"<li> {produto} </li> <br/> ")
    relatorio.write("</ul>")

    relatorio.write("<h2>Esportes</h2>")
    relatorio.write("<ul>")
    for produto in dic4:
        relatorio.write(f"<li> {produto} </li> <br/> ")
    relatorio.write("</ul>")

    relatorio.write("<h2>Eletrônicos</h2>")
    relatorio.write("<ul>")
    for produto in dic5:
        relatorio.write(f"<li> {produto} </li> <br/> ")
    relatorio.write("</ul>")

    relatorio.write("</div>")
    relatorio.write("</body>")
    relatorio.write("</html>")
    relatorio.write("Algo que será escrito no arquivo")
    relatorio.close()        
        
print(arquivo)

#Cham a função que faz o menu e loop
menu()
