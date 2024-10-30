from random import random, randint
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
flag=True
while flag:
    player = int(input(f"What do you want to choose? 0 for rock, 1 for paper or 2 for scissors and 3 for exit\n"))
    computer = randint(0,2)
    if player == 0 and computer == 0:
        print(f"you chose\n{rock}")
        print(f"Computer chose\n{rock}")
        print("its a draw")
    elif player == 1 and computer == 0:
        print(f"you chose\n{paper}")
        print(f"Computer chose\n{rock}")
        print("You win")
    elif player == 2 and computer == 0:
        print(f"you chose\n{scissors}")
        print(f"Computer chose\n{rock}")
        print("You lose")
    elif player == 0 and computer == 1:
        print(f"you chose\n{rock}")
        print(f"Computer chose\n{paper}")
        print("You lose")
    elif player == 1 and computer == 1:
        print(f"you chose\n{paper}")
        print(f"Computer chose\n{paper}")
        print("Its a draw")
    elif player == 2 and computer == 1:
        print(f"you chose\n{scissors}")
        print(f"Computer chose\n{paper}")
        print("You win")
    elif player == 0 and computer == 2:
        print(f"you chose\n{rock}")
        print(f"Computer chose\n{scissors}")
        print("You win")
    elif player == 1 and computer == 2:
        print(f"you chose\n{paper}")
        print(f"Computer chose\n{scissors}")
        print("You lose")
    elif player == 2 and computer == 2:
        print(f"you chose\n{scissors}")
        print(f"Computer chose\n{scissors}")
        print("its a draw")
    elif player == 3 :
         print("Existed")
         flag=False
    else:
        print("error")