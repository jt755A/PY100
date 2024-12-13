def count_substrings(string, substring):
    return string.count(substring)
    # if substring not in string:
    #     return 0
    # else:
    #     split_string = string.split(substring)
    # return len(split_string) - 1

print(count_substrings("lemon lemon lemon ", "lemon"))
print(count_substrings("laLAlaLA", "la"))
print(count_substrings("launch", "uno"))
print(count_substrings("laLALaLA", "la"))