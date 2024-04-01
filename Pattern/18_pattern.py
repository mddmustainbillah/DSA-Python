# ############## PROBLEM ##############
# E
# D E
# C D E
# B C D E
# A B C D E


######### CODE ###############

import string
alphabet = string.ascii_uppercase

n = 5
for i in range(1, n+1):
    for j in range(i):
        print(alphabet[n-i+j], end='')
    print()




# ############## PROBLEM ##############
# E
# D D
# C C C
# B B B B
# A A A A A


######### CODE ###############

import string
alphabet = string.ascii_uppercase

n = 5
for i in range(1, n+1):
    for j in range(i):
        print(alphabet[n-i], end='')
    print()