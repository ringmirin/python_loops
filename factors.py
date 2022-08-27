# The factor of any number is a whole number which exactly divides the 
# number into a whole number without leaving any remainder.

# For example, 3 is a factor of 9 because 3 divides 9 evenly leaving no 
# remainder.


#####   factors using for loop   ####
number=int(input("enter the number"))
for i in range(1,number+1):
   if number%i==0:
      print(i)


####factors using while loop ####

number=int(input("enter the number"))
print("factors of number:")
i=1
while i<=number:
   if number%i==0:
      print(i)
   i+=1