# Now, we will also tell the user if the number given by 
# the user is greater or smaller than the input number.
# If the user gives 4 as a number then we will check if 4 
# is less than 5 or not so it's true then we will print 
# "Number entered by you entered is small, try one more time ".
# We will again take input from the user. If the user gives 
# 7 as a number then we will check if 7 is less than 5 or 
# not so it is False then we will print "Number entered by 
# you entered is greater, try one more time ".
# If the user gives 5 as input then this number is equal to 
# the given number then we will print "Wow you guessed the 
# correct number".
# User will keep on guessing until all the chances are 
# finished.

a=1
guess=6
while a<=10:
   g=int(input("enter the number"))
   if g<guess:
      print("too too law try once more")
   elif g>guess:
      print("guess too high try once more")
   elif g==guess:
      print("guess well")
   a=a+1