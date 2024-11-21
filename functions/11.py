def greet(iso_code):
    eng_dict = {'US': 'Hey!', 'GB': 'Hello!', 'AU': 'Howdy!'}
    greeting_dict = {'en': eng_dict, 'fr': 'Salut!', 'pt': 'Olá!', 'de': 'Hallo!',
     'sv': 'Hej!', 'af': 'Haai!',}
    return greeting_dict[iso_code]

def extract_language(locale):
    return locale.split('_')[0]

def extract_region(locale):
    return locale.split('_')[1].split('.')[0]

# def local_greet(locale):
#     if extract_language(locale) == 'en':
#         return greet(extract_language(locale))[extract_region(locale)]
#     return greet(extract_language(locale))

def local_greet(locale):
    language = extract_language(locale)
    region = extract_region(locale)
    result = greet(language)
    return result[region] if type(result) == dict else result
    



print(local_greet('fr_FR.UTF-8'))
print(local_greet('en_US.UTF-8'))
print(local_greet('en_GB.UTF-8'))
print(local_greet('en_AU.UTF-8'))