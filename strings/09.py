def starts_with(string, prefix):
    # return string.startswith(prefix)
    return prefix == string[:len(prefix)]

print(starts_with("launch", "la"))
print(starts_with("school", "sah"))
print(starts_with("school", "sch"))