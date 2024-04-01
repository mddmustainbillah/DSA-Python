# ######### PROBLEM ##########
# A
# BB
# CCC
# DDDD
# EEEEE

############### CODE ###############

import string

alphabet = string.ascii_uppercase

for i in range(1, 6):
    for j in range(i):
        print(alphabet[i-1], end='')
    print()