# ############# PROBLEM ###############
#
# ****
# *  *
# *  *
# ****

################# CODE #################

r = 2
for i in range(r, 0, -1):
    for j in range(i):
        print('*', end='')
    for k in range((r-i)*2):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print()

for m in range(1, r+1):
    for n in range(m):
        print('*', end='')
    for o in range((r-m)*2):
        print(' ', end='')
    for n in range(m):
        print('*', end='')

    print()