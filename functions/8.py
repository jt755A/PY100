def greet(iso_code):
    greeting_dict = {'en': 'Hi!', 'fr': 'Salut!', 'pt': 'Olá!', 'de': 'Hallo!',
     'sv': 'Hej!', 'af': 'Haai!',}
    return greeting_dict[iso_code]

print(greet('pt'))