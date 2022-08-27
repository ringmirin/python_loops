#####factorial number  ####

###the factorial of 6 is 1*2*3*4*5*6 = 720  ###
 
 ##using while loop ####
num=int(input("enter the number"))
if num<0:
   print("invalid")
elif num==0 or num==1:
   print(1)
else:
   fac=1
   while num>1:
      fac=fac*num
      num=num-1
print(fac)





####using for loop####      
num=int(input("enter the number"))
fac=1
if num<0:
      print("invalid")
elif num==0 or num==1:
      print(1)
else:
   for i in range(1,num+1):
      fac=fac*i
   print(fac)