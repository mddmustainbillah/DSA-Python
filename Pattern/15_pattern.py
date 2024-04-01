######### Problem #############
# ABCDE
# ABCD
# ABC
# AB
# A

######### CODE ##############

import string

alphabet = string.ascii_uppercase

for i in range(5, 0, -1):
    for j in range(i):
        print(alphabet[j], end='')
    print()



