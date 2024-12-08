passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']
result = '-'.join(passcode)
print(result)

# new_string = []
# for part in passcode:
#     new_string.append(part)
#     new_string.append('-')
# new_string.pop()

# result = ( member for member in new_string )
# print(result)

joined_passcode = ''
for i in range(len(passcode)):
    joined_passcode += passcode[i]
    if i == max(range(len(passcode))):
        break
    else:
        joined_passcode += '-'

print(joined_passcode)
