import abadis_api
from sys import argv

word = str(argv[1])
translation = abadis_api.get_translation(word)

for line in translation:
    print(f'{line[0]} : {line[1]}')