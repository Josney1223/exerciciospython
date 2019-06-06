import re

file = open('sla.txt', 'r')
file_new = file.read()
episodeRegex = re.compile(r'(.*),(.*),(.*),(.*),(.*),(.*),(.*)')
mo = episodeRegex.findall(file_new)

num_2009 = 0
num_2009_2019 = 0
series_disp = []
notas_series = []

for i in range(len(mo)):
    ## Episódios 10/10
    if float(mo[i][5]) == 10 and float(mo[i][6]) == 10:
        print('Série:', mo[i][0])
        print('Episódio: Temporada', mo[i][1], ', EP', mo[i][2])
        print('Nota IBDM:', mo[i][5])
        print('Nota Netflix:', mo[i][6])
        print()

    ## Quantidade de episódios
    if float(mo[i][3][2]) <= 9:
        num_2009 += 1
    else:
        num_2009_2019 += 1

    ## Nota média
    if mo[i][0] not in series_disp:
        series_disp.append(mo[i][0])
        notas_series.append([[mo[i][5],1],[mo[i][6],1]])
    else:
        notas_series[series_disp.index(mo[i][0])][0][0] = float(notas_series[series_disp.index(mo[i][0])][0][0]) + float(mo[i][5])
        notas_series[series_disp.index(mo[i][0])][0][1] = float(notas_series[series_disp.index(mo[i][0])][0][1]) + 1
        notas_series[series_disp.index(mo[i][0])][1][0] = float(notas_series[series_disp.index(mo[i][0])][1][0]) + float(mo[i][6])
        notas_series[series_disp.index(mo[i][0])][1][1] = float(notas_series[series_disp.index(mo[i][0])][1][1]) + 1

for i in range(len(series_disp)):
    print('{:<20}'.format(str(series_disp[i]) + ':'), '{:^4.2f}'.format(notas_series[i][0][0]/notas_series[i][0][1]), '(IMDB)', '{:^4.2f}'.format(notas_serie[i][1][0]/notas_series[i][1][1]), '(Netflix)')
    

    

