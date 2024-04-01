########## Problem ############
#       *
#      ***
#     *****
#    *******

############## Code #########
for i in range(1, 5):
    for k in range(3, i, -1):
        print(' ', end='')

    for j in range(1, i + i):
        print('*', end='')

    print()
