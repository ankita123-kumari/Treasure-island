print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')


print("Welcome to the treasure island")
print("your mission is to find the treasuer")
choice1 = input("you are at a crossroad,where do you want to g0? type 'left' or 'right'.").lower()

if choice1 == "left":
# game continue
   choice2 = input("you have come to a lake . 'there is a island in the middle of the lake. 'type 'wait' to wait for boat. ' type 'swim' to swim across.").lower()


   if choice2 == 'wait':
     choice3 = input("""You arrived at the unharmed island. 
There is a house with 3 doors: one red, one yellow, and one blue. 
Which colour do you choose?""").lower()
        
     

     
     

     if choice3 == 'red':
       print("this room is full of fire.GAME OVER")
     elif choice3 == 'blue':
       print("you won the game !congratulation")

     elif choice3 == 'yellow':
        print("you enter a room of beats.GAME OVER")

   else:
    print("you attacked by a wolf.Game Over")   


else:
    print("you fell into a hole.Game Over")


