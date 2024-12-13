def starts_with(string, substring):
    # return string.startswith(substring)
    return string[:len(substring)] == substring

print(starts_with("launch", "la"))
print(starts_with("school", "sah"))
print(starts_with("school", "sch"))