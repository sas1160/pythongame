import random
from tkinter import N
point_user = 0
point_computer = 0
while True:
   user_input = input('enter your choice(rock, paper, scissors)')
   possible_choices = ['rock', 'paper', 'scissors']
   computer_input = random.choice(possible_choices)


   print(f"you entree is {user_input} and computer input is {computer_input}")

   if user_input == computer_input:
        print(f"Its a Draw as both selected {user_input}")
   elif user_input == "rock":
        if computer_input == "scissor":
           print("User wins, rock will break the scissor")
           point_user +=1
        else:
           print("User lose, paper will cover rock")
           point_computer +=1   
   elif user_input == "paper":
        if computer_input == "rock" :
           print("User wins, paper will cover the rock")
           point_user +=1
        else:
           print("User lose, scissor will cut the paper")
           point_computer +=1 
   elif user_input == "scissor":
       if computer_input == "paper":
           print("User wins, scissor will cut the paper")
           point_user +=1
       else:
           print("User lose,rock will break the scissor")
           point_computer +=1

   play_again = input("Do you want paly again? (y/n) :")  

   if play_again.lower() != "y":
       break

print("Game over")
print(f'total points are user {point_user} comp {point_computer}')
