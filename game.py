import random

while True:
    ans=0
    print("******* WELCOME *******")

    print("Enter your choice: \n 1. Rock\n 2.Paper \n 3.Scissor")

    choice = int(input("Enter your choice:"))
    while(choice<1 or choice >3):
        choice=int(input("Please enter Valid number!"))

    if choice ==1:
        selected = 'Rock'
    elif choice == 2:
        selected = 'Paper'
    else:
        selected = 'Scissor'

    print("Your choice is:",selected)
    print("                                               ")
    print("Now its computers turn!")

    comp_choice = random.randint(1,3)

    while comp_choice == choice:
        comp_choice = random.randint(1,3)

    if comp_choice == 1:
        select_comp='Rock'
    elif comp_choice ==2:
        select_comp ='Paper'
    else:
        select_comp = 'Scissor'
    print("Computer choice :", select_comp)
    print("                                               ")
    print(selected, "VS" ,select_comp)
    if (choice==1 and comp_choice==2):
        print("You Win!")
    elif(choice==2 and comp_choice==1):
        print("Computer Win!")

    elif(choice==2 and comp_choice==3):
        print("Computer Win!")
    elif(choice==3 and comp_choice==2):
        print("You Win!")

    elif(choice==1 and comp_choice==3):
        print("You Win!")
    elif (choice==3 and comp_choice==1):
        print("Computer Win!")
    else:
        print("Tie!")

    ans=input("Do you want play again?(yes/no)")
    if ans == "no":
        break
    else:
        continue
    
    
  



  
        
    
