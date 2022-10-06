name = input("Your name please? ")
print("Welcome", name, "your adventure awaits!")

answer = input("You are at a crossroad. Either go to the left or right. So which will it be? ").lower()

if answer == "left":
    answer = input("At the river either walk around it or swim across? Type walk to walk around or swim to swim across")

    if answer == "swim":
        print("While swimming across, you lost by getting eaten by crocs")
    elif answer == "walk":
        print("While walking for miles, you lost after dying from dehydration and exhaustion")
    else:
        print("You lost because you chose an invalid option")

elif answer == "right":
    answer = input("The obstacle ahead is a wobbly bridge, do you still wish to go ahead or turn around (go forward/back)? ")

    if answer == "go forward":
        answer = input("You cross the bridge, you meet a wizard. Do you wish to talk to him (yes/no)? ")

        if answer == "yes":
            print("The wizard gives you whatever you desire. You win!")
        elif answer == "no":
            print("You offend the wizard who then makes your life miserable and you lose")
        else:
            print("You lost because you chose an invalid option")

    elif answer == "go back":
        print("You head back and lose")
    else:
        print("You lost because you chose an invalid option")

else:
    print("You are undecided, you are out")

print("Thank you for playing", name)