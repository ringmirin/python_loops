#  ##Write a program to count the number of lowercase and uppercase character in a
# string accepted from the user

name=input("enter the string")
lower=0
upper=0
i=0
while i<len(name):
   if name[i]>="a" and name[i]<="z":
      lower+=1
   elif name[i]>="A" and name[i]<="Z":
      upper+=1
   i+=1
print("lower:",lower)
print("upper:",upper)

