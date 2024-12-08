def get_quote(person):
    if person == 'Yoda':
        return 'Do. Or do not. There is no try.'
    if person == 'Confucius':
        return 'I hear and I forget. I see and I remember. I do and I understand.'
    if person == 'Einstein':
        return 'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'
print('Confucius says:')
print('"' + get_quote('Confucius') + '"')

#TypeError: can only concatenate str (not "NoneType") to str.
# The problem is that there is no return value in the get_quote function.
# As a result, None will be passed to other blocks when the function is used.
# Adding return to each if statement fixes issue.