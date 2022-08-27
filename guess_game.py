# Now, we will make a game using loops. We will call this 
# game a guessing game.
# In this game we take any number, let us suppose this 
# number is number 5.
# After this we take any number as an input from the user 
# between 1 to 10. The user tries to guess this number.
# Suppose the user gives 3as an input. We will then check 
# if 3 is equal to 5 or not?
# 3 is not equal to 5 so we will ask the user for another input.
# Now, we will check if that number is equal to 5 or not.
# User will get 5 chances to guess.
# If he guessed right within the 5 chances he wins and if 
# he guesses wrong then loses the game.

guess=1
user=5
while guess<=5:
   g=int(input("enter the guess number"))
   if g==user:
      print("you win")
   else:
      print("you loose")
   
   guess=guess+1
   