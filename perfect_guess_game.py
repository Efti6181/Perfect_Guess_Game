import random
n= random.randint(1,100)
a=0
guess=0
while(a !=n):
    guess +=1
    a=int(input("Guess the number: "))
    if(a>n):
        print(f"Wrong Guess!\nEnter a Lower number")
    else:
        print(f"Wrong Guess!\nEnter a Higher number")
print(f"You Have Guess The Number Correctly in Total {guess} Attempts")
        
