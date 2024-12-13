from string import capwords
mystrg = 'launch school tech & talk'

# result = mystrg.title()
# result = capwords(mystrg)
# print(result)

all_words = mystrg.split()
sentence = []
for word in all_words:
    sentence.append(word.capitalize())

result = ' '.join(sentence)
print(result)
