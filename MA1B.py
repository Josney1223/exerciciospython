series_M = []
serie = open('series.csv', 'r', encoding = 'utf-8')
serie_list = serie.read().replace('\n', ',').split(',')
for i in range(len(serie_list)//7):
    series_M.append([])
    for u in range(i*7, i*7+7):
        series_M[i].append(serie_list[u])
    
def verificar_ano(data):
    ano = data.split(' ')
    return ano[2]

def verificar_dez():
    for i in range(len(series_M)):
        if float(series_M[i][5]) == 10 and float(series_M[i][6]) == 10:
            print('Série:', series_M[i][0])
            print('Episódio: Temporada', series_M[i][1], ', EP', series_M[i][2])
            print('Nota IBDM:', series_M[i][5])
            print('Nota Netflix:', series_M[i][6])
            print()

def verificar_num_ep():
    num_2009 = 0
    num_2009_2019 = 0
    for i in range(len(series_M)):
        if float(verificar_ano(series_M[i][3])) <= 9:
            num_2009 += 1
        else:
            num_2009_2019 += 1
    print('Número de episódios até 2009:', num_2009)
    print('Número de episódios entre 2009 e 2019:', num_2009_2019)
    print()

def verificar_nota_serie():
    series_disp = []
    notas_serie_IMDB = []
    notas_serie_Net = []
    for i in range(len(series_M)):
        if series_M[i][0] not in series_disp:
            series_disp.append(series_M[i][0])
            notas_serie_IMDB.append([series_M[i][5], 1])
            notas_serie_Net.append([series_M[i][6], 1])
        else:
            notas_serie_IMDB[series_disp.index(series_M[i][0])][0] = float(notas_serie_IMDB[series_disp.index(series_M[i][0])][0]) + float(series_M[i][5])
            notas_serie_IMDB[series_disp.index(series_M[i][0])][1] = float(notas_serie_IMDB[series_disp.index(series_M[i][0])][1]) + 1
            notas_serie_Net[series_disp.index(series_M[i][0])][0] = float(notas_serie_Net[series_disp.index(series_M[i][0])][0]) + float(series_M[i][6])
            notas_serie_Net[series_disp.index(series_M[i][0])][1] = float(notas_serie_Net[series_disp.index(series_M[i][0])][1]) + 1
            
    for i in range(len(series_disp)):
        print(str(series_disp[i]) + ':', '{:0.2f}'.format(notas_serie_IMDB[i][0]/notas_serie_IMDB[i][1]), '(IMDB)', '{:0.2f}'.format(notas_serie_Net[i][0]/notas_serie_Net[i][1]), '(Netflix)')
        
verificar_dez()
verificar_num_ep()
verificar_nota_serie()
