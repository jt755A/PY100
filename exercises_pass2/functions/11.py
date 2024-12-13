def extract_language(locale):
    language = locale.split('_')[0]
    return language

def extract_region(locale):
    start = locale.index('_') + 1
    stop = locale.index('.')
    region = locale[start:stop]
    return region

def greet(language):
    match language:     
        case 'en':
            return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai!'

def local_greet(locale):
    language = extract_language(locale)
    region = extract_region(locale)
    
    # match region:
    #     case 'US':
    #         return 'Hey!'
    #     case 'GB':
    #         return 'Hello!'
    #     case 'AU':
    #         return 'Howdy!'
    #     case _:
    #         return greet(language)
    
    match language, region:
        case 'en', 'US':
            return 'Hey!'
        case 'en', 'GB':
            return 'Hello!'
        case 'en', 'AU':
            return 'Howdy!'
        case _:
            return greet(language)


        


print(local_greet('en_US.UTF-8'))
print(local_greet('en_GB.UTF-8'))
print(local_greet('en_AU.UTF-8'))
print(local_greet('fr_FR.UTF-8'))