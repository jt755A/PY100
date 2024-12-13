def extract_region(locale):
    # start = locale.index('_') + 1
    # stop = locale.index('.')
    # region = locale[start:stop]
    return locale.split('_')[1].split('.')[0]
    # return region

print(extract_region('en_US.UTF-8'))
print(extract_region('en_GB.UTF-8'))
print(extract_region('ko_KR.UTF-16'))