################ PROBLEM ################
#    A
#   ABA
#  ABCBA
# ABCDCBA

################ CODE ###############

import string
alphabet = string.ascii_uppercase

n = 3
for i in range(n):
    for j in range(n-1, i, -1):
        print(' ', end='')

    row_value = i * 2 + 1
    div = int(row_value / 2)

    for k in range(div + 1):
        print(alphabet[k], end='')
    for m in range(div-1, -1, -1):
        print(alphabet[m], end='')

    print()



