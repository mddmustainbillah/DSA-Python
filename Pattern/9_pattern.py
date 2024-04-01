########## Problem ############
#       *
#      ***
#     *****
#    *******
#    *******
#     *****
#      ***
#       *

############ Code ################

row = 4
for i in range(1, row+1):
    for j in range(row-1, 0, -1):
        print(" ", end='')
    for k in range(i+i-1, 0, -1):
        print('*', end='')
    row -= 1
    print('\n')
row = 4
for m in range(1, row+1):
    for n in range(1, m):
        print(' ', end='')
    for o in range(row+row-1, 0, -1):
        print('*', end='')

    row -= 1
    print('\n')


