#  Write a Python program that prints all the numbers from 
# 0 to 6 except 3 and 6.
number=1,2,3,4,5,6,7,8,9
even=0
odd=0
for x in number:
   if x%2==0:
      even+=1
   else:
      odd+=1
print("number of even:",even)
print("number of odd:",odd)
