import re

file = open('sla.txt', 'r')
file_new = file.read()
episodeRegex = re.compile(r'(.*),(.*),(.*),(.*),(.*),(.*),(.*)')
mo = episodeRegex.findall(file_new)

    

