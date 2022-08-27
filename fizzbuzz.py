# Write a Python program which iterates the integers from 
# 1 to 50. For multiples of three print "Fizz" instead of 
# the number and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five 
# print "FizzBuzz".
a=0
while a<=50:
   if a%3==0 and a%5==0:
      print("fizzbuzz")
   elif a%3==0:
      print("fizz")
   elif a%5==0:
      print("buzz")
   else:
      print(a)
   
   a=a+1
