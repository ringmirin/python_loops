##### harshad number  ###### (156)1+5+6=12 (12 is divisible by 156)
  
   

num=int(input("enter the number"))
sum=0
temp=num
while temp:
   sum=sum+temp%10
   temp//=10
if num%sum==0:
   print(num,"is harshad number")
else:
   print(num,"is not harshad number")

