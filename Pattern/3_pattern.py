############# Problem #############
# 1
# 1 2
# 1 2 3
# 1 2 3 4

########## Code ##############

for i in range(4):
    for j in range(i+1):
        print(j+1, '', end='')
    print("\n")