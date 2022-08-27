# Write a Python program that accepts a string and calculate 
# the number of digits and letter
d=0
l=0
a=input("enter the string:")
for x in (a):
   if  x.isdigit():
      d=d+1
   elif x.isalpha():
      l=l+1
   else:
      pass
print("number of letter",l)
print(" number of digit",d)