# ################# PROBLEM ################
# ******
# **  **
# *    *
# *    *
# **  **
# ******


########### CODE ###################
n = 3
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end='')
    for k in range((-i+n)*2):
        print(' ', end='')
    for j in range(i):
        print("*", end='')
    print()

for l in range(n):
    for m in range(l+1):
        print('*', end='')
    for m in range((n-l-1)*2):
        print(' ', end='')
    for m in range(l+1):
        print('*', end='')

    print()


