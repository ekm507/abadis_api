import requests

def get_translation_raw(word, lang_from='en', lang_to='fa'):

    link = 'https://abadis.ir/api/?cmd=word&ver=20'
    data = {
        'Word':word,
        'Fr':lang_from,
        'To':lang_to,
        }

    translate_request = requests.post(link, data=data)
    return translate_request.text

def text_splitter(text:str) -> list:
    lines = text.split('^')

    output = []
    for line in lines:
        line_parts = line.split('#')
        if len(line_parts) > 1:
            output.append(line_parts)
    
    return output

def get_translation(word:str, lang_from='en', lang_to='fa')->list:
    translated_text = get_translation_raw(word, lang_from=lang_from, lang_to=lang_to)
    splitted_translation = text_splitter(translated_text)
    return splitted_translation
