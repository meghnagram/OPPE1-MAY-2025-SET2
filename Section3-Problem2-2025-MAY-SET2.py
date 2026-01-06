

n = int(input())
for i in range(n):
    side_space = ' ' * (n - i - 1) # space between vertical bar | and / or \
    mid_space = ' '* 2 * i # middle space between / and \
    print(f"|{side_space}/{mid_space}\\{side_space}|")

# #Another Method


# # Write your code here to read the input and print the output
# n=int(input())

# for i in range(n):
#     print('|'   +   (n-i-1)*' '  + '/' + (i*2)*' '  +  '\\'  +  (n-i-1)*' '  + '|')




# #  | 4 space / \ 4 space |
# #  | 3 space/ 2 space \ 3space |
# #  | 2 pace / 4space \ 2space|

# Pattern Printing - W Pattern
# Given an integer n (where n > 0), print an "W" shaped pattern with n rows.

# The pattern should consist of a vertical bar (|) on the left and right sides of each row. Additionally, it should have forward slashes (/) and backslashes () moving diagonally towards each other from the top to the bottom.

# NOTE: This is an I/O type question, you need to write the whole code for taking input and printing the output.

# Input Format

# A single integer n, representing the number of rows in the pattern.
# Output Format

# An "W" shaped pattern with n rows, as described.
# Examples

# Input:

# 1
# Output:

# |/\|

# Input:

# 2
# Output:

# | /\ |
# |/  \|
# Input:

# 3
# Output:

# |  /\  |
# | /  \ |
|/    \|
