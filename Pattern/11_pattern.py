################ Problem ################
# 1
# 0 1
# 1 0 1
# 0 1 0 1


############### Code #################
n = 4
for i in range(1, n+1):
    for j in range(1, i+1):
        sum_axis = i + j
        if sum_axis % 2 == 0:
            print('1 ', end='')
        else:
            print('0 ', end='')
    print('\n')
