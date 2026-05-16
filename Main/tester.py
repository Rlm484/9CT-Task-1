import sys
import os
import time
def cs():                 #Function from the game I made earlier this year
    print()
    time.sleep(1.5)
    # Check the operating system and run the appropriate clear command
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS and Linux
        os.system('clear')

def ani(text, delay=0.075): #Function from the game I made earlier this year
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line

def ui():
    while True:
        print("-=- Enlistment Data Interface -=-")
        ani("1. View Raw Data")
        ani("2. Exit")
        ani("3. Testy thingy")
        ani("\nPlease Select an option (1-3): ")
        choice = input("")
        ani("Loading...")
        if choice == "1":
            cs()
            ani("Hi")
            cs()
        elif choice == "2":
            cs()
            break
        elif choice == "3":
            cs()
            ani("How would you like to view this Data?")
            ani("a) View as a Pie Chart")
            ani("b) View as a Bar Chart")
            po1 = input()
            ani("Loading...")

            if po1 == "a":
                cs()
                print("Pie chart here for if enlist")
            elif po1 == "b":
                cs()
                print("Bar chart here for if enlist")
            else:
                cs()
                print("invalid msg")
                cs()
        else:
            cs()
            ani("INVALID, TRY AGAIN")
            cs()
            

ui()