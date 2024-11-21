def extract_region(locale):
    # start_index = locale.find('_') + 1
    # end_index = locale.find('.')
    # return locale[start_index:end_index]

    return locale.split('_')[1].split('.')[0]


test = 'en_US.UTF-8'
print(extract_region(test))