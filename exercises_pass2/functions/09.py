def extract_language(locale):
    language = locale.split('_')[0]
    return language

print(extract_language('en_US.UTF-8'))
print(extract_language('en_GB.UTF-8'))
print(extract_language('ko_KR.UTF-16'))