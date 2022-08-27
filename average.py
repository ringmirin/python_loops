# Take input of weights of 11 people and then print their 
# average and then check whether the average weight is a 
# multiple of 5 or not? This means that when you will 
# divide the average weight by 5, the remainder should be 0.


a=1
t=0
average=0
while a<=11:
   weight=int(input("enter the weight"))
   t=t+weight
   average=t/11
   print(average)
   a=a+1
                     
if average%5==0:
   print(average)
a=a+1 