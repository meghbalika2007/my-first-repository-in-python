import random
print("!What do you choose ?,Choose 0 for rock 1 for paper and 2 for scissors!")
rock=''''_______
      ---'   ____)
            (_____)
            (_____)
             (____)
      ---.__(___)'''

paper='''   _____ 
      ---'   ____)____
                ______)
                _______)
               _______)
      ---.__________)'''
scissor=''' _____     
      ---'   ____)____
                ______)
             __________)
             (____)
      ---.__(___)
'''
user=int(input("What do you choose ,type 0 for rock ,1 for paper and 2 for scissors: "))
if user==0:
  print(rock)
if user ==1:
  print(paper)
if user == 2:
  print(scissor)
computer_choice = random.randint(0,2)
print("THe computer choice is :",computer_choice)
if computer_choice==0:
  print(rock)
if computer_choice==1:
  print(paper)
if computer_choice == 2:
  print(scissor)
#To find winner or looser
if user == computer_choice:
  print("....Wow it is a draw....")
if user==0 and computer_choice == 1: 
  print("THe computer won.")
if user ==1  and computer_choice==2:
  print("The computer won")
if user==2 and computer_choice==0:
  print("The computer won")
if user==2 and computer_choice==1:
  print("user won")
if user== 0 and computer_choice==2:
  print("The user won")
if user ==1 and computer_choice==0:
  print("The user won")
