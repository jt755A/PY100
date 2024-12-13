def get_quote(person):
    if person == 'Yoda':
        return 'Do. Or do not. There is no try.'
    if person == 'Confucius':
        return 'I hear and I forget. I see and I remember. I do and I understand.'
    if person == 'Einstein':
        return 'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'

print('Confucius says:')
print('"' + get_quote('Confucius') + '"')

print('Yoda says:')
print('"' + get_quote('Yoda') + '"')

print('Einstein says:')
print('"' + get_quote('Einstein') + '"')




# the problem is that the function get_quote does not return anything.
# so the default return value of None is used
# adding return to each if block fixes issue