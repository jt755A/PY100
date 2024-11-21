# Using the code below as a starting point, write a while loop
# that prints the elements of lst at each index and terminates
# after printing the last element of the list.

# lst = [1, 3, 7, 15]
# index = 0

# # while index < len(lst):
# #     print(lst[index])
#     # index += 1

# while True:
#     if index >= len(lst):
#         break
#     print(lst[index])
#     index += 1


lst = []
index = 0

while index < len(lst): # doesn't output on empty list 
                        #because len(lst) = 0 == starting index
    print(lst[index])
    index += 1

print(len(lst))