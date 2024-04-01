########## Problem ###############
# *
# **
# ***
# ****
# ***
# **
# *

############# Code ###############
n=3
for i in range(1,n+1):
    for j in range(i):
        print('*', end='')
    print("\n")
for k in range(n, 1, -1):
    for l in range(k, 1, -1):
        print('*', end='')
    print("\n")

