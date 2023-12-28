#import random module with 'r' 
import random as r

print("Step into the world of Rock Paper Scissors Game!")

#Information 
print("Enter 1 for choosing Rock \n Enter 2 for choosing Paper \n Enter 3 for choosing Scissors\n")

while True:
    #Take input 
    user_ch=int(input("Enter your choice"))
    #User choice 
    if(user_ch==1):
        print("You have chose Rock!\n") #elif(user_ch==2):
        print("You have chose Paper!\n")
    else:
        print("You have chose Scissors!\n")
        print("Now it's turn for computer's Choice\n")

 #Computer choice, randomly choose any number among 1,2,3
    cp_ch=r.randint(1,3) #Using randint method of random module
    if(cp_ch==1):
        print("Computer's choice: Rock!\n") 
    elif(cp_ch==2):
        print("Computer's choice: Paper!\n")
    else:
        print("Computer's choice: Scissors!\n")
 #Conditions to win
    print("Now it's Time to Play")

    if((user_ch==1 and cp_ch==2) or (user_ch==1 and cp_ch==3) or(user_ch==3 and cp_ch==2)):
        print("User wins!!")
    elif((user_ch==2 and cp_ch==1) or (user_ch==2 and cp_ch==3)or
        (user_ch==3 and cp_ch==1)):
            print("Computer wins!!")
    elif(user_ch==cp_ch):
        print("It's a tie!")
 #Asking2 to play more
    print("Do you want to play again(Y/N)?")
    a=input()
 #if input is N loop continues
    if(a=='N'):
        break
    print("Thanks for playing!")