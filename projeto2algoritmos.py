arquivo = open('C:\\Temp\\emack.csv', 'r')
#conteudo = arquivo.read()


# para abrir no PC da Faculdade: 'C:\\Temp\\emack.csv'
# para abrir no PC do Haddad: "C:/Users/Felipe/Desktop/Faculdade/Algoritmo e Programação I/Prática/Trabalho 2/emack.csv" 

# Cria listas para cada propriedade dos produtos
ids =[]
titles = []
prices = []
listPrices =[]
categories = []
isBestSeller = []
boughtLastMonth = []

#Preenche as listas acima com as informações do arquivo principal
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

#Deleta os títulos das listas
del(ids[0])
del(titles[0])
del(prices[0])
del(listPrices[0])
del(categories[0])
del(isBestSeller[0])
del(boughtLastMonth[0])


#Item a)
def categoryCount(categories):
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
    print(livros)
    print(moda)
    print(casa)
    print(esporte)
    print(elec)

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

