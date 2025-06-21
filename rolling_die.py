import random

#loop 
while True:
    #ask : roll the die
    start = input(print("do you want to roll the die (y = yes,n = no) : ")).upper()

# if yes
    # generater two random no
    if start == "Y":
        random_no = random.randint(1,6)
        random_no_ = random.randint(1,6)
        print(f"( {random_no} , {random_no_} )")

# if no 
    #print : game ended
    #terminate
    if start == "N":
        print("the game has ended")
        break
#else
    #print :invalid choice try again
    else:
        print("invalid choice please try again")
