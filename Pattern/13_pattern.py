############## Question ################
# 1
# 2 3
# 4 5 6

############# Code ##################

n = 3
start = 1
for i in range(1, n+1):
    for j in range(i):
        print(start, end='')
        start += 1
    print()
