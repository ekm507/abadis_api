#!/bin/python3

# use abadis api library
import abadis_api
from sys import argv
lang_from = 'en'
lang_to = 'fa'
word = str(argv[1])
if word == '-fa':
    lang_from = 'fa'
    word = argv[2]
elif word == '-en':
    lang_to = 'en'
    word = argv[2]
elif word == '-r':
    lang_from, lang_to = lang_to, lang_from
    word = argv[2]

# get translation of the word
translation = abadis_api.get_translation(word, lang_from=lang_from, lang_to=lang_to)

# print translation
for line in translation:
    print(f'{line[0]} : {line[1]}')
