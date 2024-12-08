def is_empty_or_blank(string):
    return True if string.isspace() or len(string) == 0 else False


print(is_empty_or_blank('mars'))
print(is_empty_or_blank('  '))
print(is_empty_or_blank(''))