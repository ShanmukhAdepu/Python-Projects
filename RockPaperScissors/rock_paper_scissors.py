import random

def cpuChoice():
    
    cpu = random.choice(["r", "p", "s"])
    
    if cpu == 'r':
        return "rock"
    elif cpu == "p":
        return "paper"
    elif cpu == "s":
        return "scissors"

def userChoice(choice):

    choice = choice.lower()
    if "ro" in choice:
        return "rock"
    elif "pa" in choice:
        return "paper"
    elif "sc" in choice:
        return "scissors"

def playrps():

    print(" ")
    bestOf = input("How many rounds would you like to play? 3? 5? 7? or 9?: ")
    done = False
    win = (int(bestOf)//2) + 1
    userp = 0
    cpup = 0

    while done == False:

        print(" ")
        user = input("Do you pick rock, paper, or scissors?: ")

        userc = userChoice(user)

        cpu = cpuChoice()

        if cpu == user:

            print("Thats a tie!")
            print("The score is still CPU = " + str(cpup) + " points and YOU = " + str(userp) + " points." )

        if cpu == "rock":
            
            print("CPU's choice is rock.")
            
            if userc == "scissors":
                
                cpup += 1
                print("Sorry but you got beat! The score is now CPU = " + str(cpup) + " points and YOU = " + str(userp) + " points." )

                if cpup == win:
                    userp = userp
                    print("Seems like the CPU beat you this time with a score of " + str(cpup) + " to " + str(userp) + ". Better Luck Next Time!")
                    done = True
            
            if userc == "paper":
                
                userp += 1
                print("Nice one! The score is now CPU = " + str(cpup) + " points and YOU = " + str(userp) + " points." )

                if userp == win:
                    print("Nice job winning with a score of " + str(userp) + " to " + str(cpup) + "!")
                    done = True

        if cpu == "scissors":
            
            print("CPU's choice is scissors.")
            
            if userc == "paper":
                
                cpup += 1
                print("Sorry but you got beat! The score is now CPU = " + str(cpup) + " points and YOU = " + str(userp) + " points." )

                if cpup == win:
                    print("Seems like the CPU beat you this time with a score of " + str(cpup) + " to " + str(userp) + ". Better Luck Next Time!")
                    done = True
            
            if userc == "rock":
                
                userp += 1
                print("Nice one! The score is now CPU = " + str(cpup) + " points and YOU = " + str(userp) + " points." )

                if userp == win:
                    print("Nice job winning with a score of " + str(userp) + " to " + str(cpup) + "!")
                    done = True

        if cpu == "paper":
            
            print("CPU's choice is paper.")
            
            if userc == "rock":
                
                cpup += 1
                print("Sorry but you got beat! The score is now CPU = " + str(cpup) + " points and YOU = " + str(userp) + " points." )

                if cpup == win:
                    print("Seems like the CPU beat you this time with a score of " + str(cpup) + " to " + str(userp) + ". Better Luck Next Time!")
                    done = True
            
            if userc == "scissors":
                
                userp += 1
                print("Nice one! The score is now CPU = " + str(cpup) + " points and YOU = " + str(userp) + " points." )

                if userp == win:
                    print("Nice job winning with a score of " + str(userp) + " to " + str(cpup) + "!")
                    done = True

        
    print("Bye!")

    return

print(" ")
play = input("Are you ready to play rock, paper, scissors?: ")

if "y" in play:
    playrps()
else:
    print("Very well maybe next time.")