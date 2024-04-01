################### PROBLEM ###################

# # Count digits in a number
# # Problem Statement: Given an integer N, write a program to count the number of digits in N.
#
# Example 1:
# Input: N = 12345
# Output: 5
# Explanation: N has 5 digits
#
# Example 2:
# Input: N = 8394
# Output: 4
# Explanation: N has 4 digits


################### CODE ###################

def digit_count(n):
    count = 0
    val = n
    while(val != 0):
        val //= 10
        count += 1
    return count

print('Number of digits is', digit_count(12345))

