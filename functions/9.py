# from locale import getlocale

def extract_language(locale):
    return locale.split('_')[0]

print(extract_language('ko_KR.UTF-16'))

# test = 'ko_KR.UTF-16'
# print(extract_language(locale))