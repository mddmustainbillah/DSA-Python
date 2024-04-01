############## PROBLEM #################

# Problem Statement: Given a number N reverse the number and print it.
#
# Example 1:
# Input: N = 123
# Output: 321
# Explanation: The reverse of 123 is 321
#
# Example 2:
# Input: N = 234
# Output: 432
# Explanation: The reverse of 234 is 432


############# CODE #################

# # Solution - 1
# print(''.join(reversed('123')))

# # Solution -2
# n = 123
# n = str(n)
# print(n[::-1])

# Solution - 3
n = 123
def reverse_number(n):
    n_list = list(str(n))
    left = 0
    right = len(n_list) -1

    while(left != right):
        borrow = n_list[left]
        n_list[left] = n_list[right]
        n_list[right] = borrow

        left += 1
        right -= 1
    return "".join(n_list)


print(reverse_number(n))


# def reverse_number(num):
#     reversed_num = 0
#     while num > 0:
#         # Get the last digit of the number
#         digit = num % 10
#
#         # Append the digit to the reversed number
#         reversed_num = (reversed_num * 10) + digit
#
#         # Remove the last digit from the number
#         num //= 10
#
#     return reversed_num
#
#
# # Test the function
# num = 12345
# reversed_num = reverse_number(num)
# print("Original number:", num)
# print("Reversed number:", reversed_num)





