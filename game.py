

from PIL import Image
# Load and display an image
image = Image.open("RPS.jpg")
image.show()



# # ASCII art for rock, paper, scissors
import random
game_art = [
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
]

# Game logic
user_choice = int(input("What do you want to choose? 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

# Validate user input
if user_choice < 0 or user_choice > 2:
    print("You typed an invalid number. Please try again.")
    exit()

# Display user's choice
print(f"You chose:\n{game_art[user_choice]}")

# Computer's random choice
computer_choice = random.randint(0, 2)
print(f"Computer chose:\n{game_art[computer_choice]}")

# Determine the winner
if user_choice == computer_choice:
    print("It's a draw!")
elif (user_choice == 0 and computer_choice == 2) or \
     (user_choice == 1 and computer_choice == 0) or \
     (user_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose!")


