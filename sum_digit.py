# Write a program to accept a string and display the sum of the digits, if any present in string.
# for example:


string= "My position is 1st and my friend come on 4th"
sum=0
for c in string:
   if c.isdigit()==True:
      sum+=int(c)
print(sum)
