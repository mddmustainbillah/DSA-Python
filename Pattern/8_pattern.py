################ Problem ###############

# *******
#  *****
#   ***
#    *


################ Code #############
row = 4
for i in range(1, row+1):
    for j in range(1, i):
        print(" ", end='')
    for k in range(row+row-1, 0, -1):
        print('*', end='')
    row -= 1
    print('\n')




