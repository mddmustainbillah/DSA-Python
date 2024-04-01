############# Problem #########
# 1 2 3 4
# 1 2 3
# 1 2
# 1

########### Code ###########

for i in range(4):
    for j in range(4, i, -1):
        print(4-j+1, end='')
    print('\n')