def is_empty_or_blank(string):
    if len(string) == 0 or string.isspace():
        return True
    else:
        return False

print(is_empty_or_blank('mars'))
print(is_empty_or_blank('  '))
print(is_empty_or_blank(''))