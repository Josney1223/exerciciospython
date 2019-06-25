def resumir(texto):
    if len(texto) > 140:
        textoA = texto.split(' ')
        texto_resumido = ''
        tamanho = 0
        for i in textoA:
            tamanho += len(i)
            if tamanho > 140:
                tamanho -= len(i)
                texto_resumido = texto_resumido + "..."
                return texto_resumido
            else:
                tamanho += 1
                texto_resumido = texto_resumido + ' ' + str(i)
                
    else:
        texto_resumido = texto
        return texto_resumido

def DigCasas(num):
    def Print(tamanho):
        if tamanho == 0:
            return 'Centenas'
        elif tamanho == 2:
            return 'Dezenas'
        else:
            return 'Unidade'
        
    nome = ['','Mil','Milhão','Bilhão','Trilhão']
    
    numero = str(num)
    valor = numero[0] + ',' + numero[1:3]
    casa = (len(numero)-1) // 3
    if casa != 0:
        print(valor,Print(len(numero) % 3), 'de', nome[casa])
    else:
        print(valor,Print(len(numero) % 3))

def SucessoBilheteria():
    porData = {2013:[['Frozen',1276480335]],
               2012:[["Marvel's The Avengers",1518812988]],
               1997:[['Titanic',2187463944]],
               2018:[['Black Panther',1346913161],["Avenger's: Infinity War",2048359754],['Jurassic World: Fallen Kingdom',1309484461]],
               2017:[['Star Wars: The Last Jedi',1332539889],['Beauty and the Beast',1263521126]],
               2015:[["Avenger's: Age of Ultron",1405403694],['Jurassic World',1671713208],['Furious 7',1516045911],['Star Wars: The Force Awakens',2068223624]],
               2011:[['Harry Potter and the Deathly Hallows - Part 2',1341693157]],
               2009:[['Avatar',2787965087]],
               2019:[["Avenger's Endgame", 2750667499]]}

    maiorSucessoNum = 0
    for i in porData:
        x = 0
        for u in range(len(porData[i])):
            k = int(porData[i][u][1])
            x += k
            
            if k > maiorSucessoNum:
                maiorSucessoNum = porData[i][u][1]
                maiorSucesso = porData[i][u]
                ano = i
        print('Valor arrecadado em', str(i) + ': US$', end = ' ')
        DigCasas(x)
                
    print('Maior Sucesso de bilheteria é de', str(ano) + ',', 'com US$', end = ' ')
    DigCasas(maiorSucesso[1])
    print(maiorSucesso[0])
