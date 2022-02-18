import random
def game(computer,a):
    if computer == a:
        return None
    elif computer == "rock":
        if a == "paper":
            return False
        elif a == "scissor":
            return True
    elif computer == "paper":
        if a == "scissor":
            return False
        elif a == "rock":
            return True 
    elif computer == "scissor":
        if a == "rock":
            return False
        elif a == "paper":
            return True
        
print("computers: rock,paper & scissor")
r = random.choice(["rock","paper","scissor"])
if r == "rock":
    computer = "rock"
if r == "paper":  
    computer = "paper"
if r == "scissor":
    computer = "scissor"
w = 0
l = 0
z = 0
for i in range(5):
    a = input("Choose:")
    while(a!= "rock"and a!= "paper"and a!= "scissor"):
        print("Value is not given")
        a = input("Choose:")
    b = game(computer,a)

    print(f"Computer choose: {computer}")
    print(f"You Choose: {a}")

    
    if b == None:
        z = (int(z))+1

        print("This game is tied")
    elif b:
        print("You Win")
        w = w+1
        
    else:
        print("you Lose")
        l = l+1
    print("you:\n",w)
    print("computer:\n",l)
    print("Tied:\n",z)
if (w>l):
    print("You win")
elif(l>w):
    print("Computer wins")
else:
    print("The Game is Tied")

print ("Thankyou for playing")
