
def vowel_count(word):
    # count = 0
    # for char in word:
    #     if char.lower() in "aeiou":
    #         count += 1
    # return count
    return sum(1 for char in word if char.lower() in "aeiou")

words = input().split()
print(" ".join([f"{word}({vowel_count(word)})" for word in words]))

# method 2
# print(*(f"{word}({vowel_count(word)})" for word in words))

# method 3
# for word in words[:-1]:
#     print(f"{word}({vowel_count(word)}) ")
# print(f"{word}({vowel_count(word)}) ")

# #Another Method


# # Write your code here to read the input and print the output

# strin=input()
# l=[]
# l=strin.split()
# c=0
# s=[]

# for i in l:
#     for j in i:
#         if j.lower() in ('a','e','i','o','u'):
#             c=c+1
#     s.append(c)
#     c=0
    
# for i in range(len(l)):
#     print(f"{l[i]}({s[i]})",end= ' ')


# Vowel count of words
# Write a program that takes a string and counts the number of vowels in every word. The program should then print each word followed by the count of vowels in parentheses.

# Assume words are seperated by space and spaces should be retained in the output.

# NOTE: This is an I/O type question, you need to write the whole code for taking input and printing the output.

# Input Format

# A string in the first line.
# Output Format

# A string with vowel count of each word in parantheses after each word.
# Example

# Input

# Computer science is amazing
# Output

# Computer(3) science(3) is(1) amazing(3)
