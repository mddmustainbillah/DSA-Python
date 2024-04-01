################# Problem #################

# 1    1
# 12  21
# 123321

############## Code ######################
# n = 3
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         for k in range(j):
#             print(k + 1, end='')
#         for l in range(n, 1, -1):
#             print(" ", end='')
#         for m in range(n, j, -1):
#             print(" ", end='')
#         for n in range(j, 0, -1):
#             print(n, end='')
#     print("\n")

n = 3
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    for k in range(n - i):
        print("  ", end='')
    for l in range(i, 0, -1):
        print(l, end='')
    print()
