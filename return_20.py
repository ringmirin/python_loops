# # Write a Python program to sum of two given integers. 
# # However, if the sum is between 15 to 20 it will return 20

x=int(input("enter the number"))
y=int(input("enter the second"))
sum=x+y
if sum in range(15,20):
   print(20)
else:
   print(sum)



