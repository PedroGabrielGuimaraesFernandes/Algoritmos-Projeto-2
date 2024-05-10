arquivo = open('C:\\Temp\\emack.csv', 'r')
#conteudo = arquivo.read()
ids =[]
titles = []
prices = []
listPrices =[]
categories = []
isBestSeller = []
boughtLastMonth = []

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

del(ids[0])
del(titles[0])
del(prices[0])
del(listPrices[0])
del(categories[0])
del(isBestSeller[0])
del(boughtLastMonth[0])
print(categories)
#Livros, Esportes, Casa, Moda, Eletrónicos
categoryCount(categories)

