scores = [96, 47, 113, 89, 100, 102]
# tally = 0
# for element in scores:
    

# result = ( score >= 100 for score in scores )
# my_list = list(result)
# print(my_list.count(True))

filter = ( 1 for score in scores
          if score >= 100 )
result = sum(filter)
print(result)