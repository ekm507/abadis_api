import requests

def get_translation(word, lang_from='en', lang_to='fa'):

    link = 'https://abadis.ir/api/?cmd=word&ver=20'
    data = {
        'Word':word,
        'Fr':lang_from,
        'To':lang_to,
        }

    translate_request = requests.post(link, data=data)
    return translate_request.text

