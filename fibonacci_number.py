# Make an algorithm that prints the first 100 numbers of 
# the fibonacci series.
# Fibonacci series is shown here, 0, 1, 1, 2, 3, 5, 8, 13


    
a=0
b=1
c=int(input("enter the terms"))
if c<=0:
   print(a)
else:
   print(a,b,end=" ")
   for x in range(c):
      next=a+b
      print(next,end=" ")
      a=b
      b=next

#####simple fibonacci   ####

a,b=0,1
while a<=100:
   print(a,end=",")
   a,b=b,a+b
print("done")
   