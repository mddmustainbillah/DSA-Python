############# PROBLEM ################
# A
# AB
# ABC
# ABCD

############### CODE #################
import string

alphabet = string.ascii_uppercase

for i in range(1, 5):
    for j in range(i):
        print(alphabet[j], end='')
    print()

