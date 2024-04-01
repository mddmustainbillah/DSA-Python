##########  PROBLEM  ###############
# N = 4

# 4 4 4 4 4 4 4
# 4 3 3 3 3 3 4
# 4 3 2 2 2 3 4
# 4 3 2 1 2 3 4
# 4 3 2 2 2 3 4
# 4 3 3 3 3 3 4
# 4 4 4 4 4 4 4

############ CODE ################
n = 4
for i in range(n*2-1):
    for j in range(n*2-1):
        top = i
        bottom = j
        left = (n*2-2) - i
        right = (n*2-2) - j

        print(n - (min(top, bottom, left, right)), end='')
    print()


# n = 4
# # Outer loop for number of rows
# for i in range(2*n - 1):
#     # Inner loop for number of columns
#     for j in range(2*n - 1):
#         # Initializing the top, down, left, and right indices of a cell
#         top = i
#         bottom = j
#         right = (2*n - 2) - j
#         left = (2*n - 2) - i
#         # Min of 4 directions and then subtract from n
#         # because previously we would get a pattern whose border
#         # has 0's, but we want with border N's and then decreasing inside.
#         print(n - min(min(top, bottom), min(left, right)), end=" ")
#     # Move to the next row and give a line break
#     print()

# def main():
#     # Here, we have taken the value of N as 5.
#     # We can also take input from the user.
#     N = 5
#     pattern22(N)
#
# if __name__ == "__main__":
#     main()

