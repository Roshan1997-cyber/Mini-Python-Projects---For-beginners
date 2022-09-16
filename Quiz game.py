print("Greetings and welcome to the quiz!")

playing = input("Do you wish to proceed? ")

if playing.lower() != "yes":
    quit()

print("Alright, let the quiz begin!")
score = 0

answer = input("What is the opposite of up? ")
if answer == "down":
    print('Correct!')
    score += 1
else:
    print('Wrong')

answer = input("What is another name for Coca-Cola? ")
if answer.lower() == "coke":
    print('Correct!')
    score += 1
else:
    print('Wrong')

answer = input("Where is the Eiffel Tower? ")
if answer == "Paris, France":
    print('Correct!')
    score += 1
else:
    print('Wrong')

answer = input("When is Waitangi Day? ")
if answer == "February 6":
    print('Correct!')
    score += 1
else:
    print('Wrong')

print("You scored " + str(score) + " questions correctly!")
print("Your accuracy percentage is " + str((score / 4) * 100) + " %")