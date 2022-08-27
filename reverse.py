# Write a Python program that accepts a word from the user 
# and reverse it.

user=input("enter the word to reverse:")
for chr in range(len(user) -1, -1 , -1):
   print(user[chr],end="")
   