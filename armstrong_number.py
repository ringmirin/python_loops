##153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.#####


num=int(input("enter the number"))
sum=0
temp=num
while temp>0:
   digit=temp%10
   sum=sum+digit**3
   temp//=10
if num==sum:
   print("armstrong number")
else:
   print("not")




