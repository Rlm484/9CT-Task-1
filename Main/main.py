import sys
import os
import time
#from data_module import()

def cs():                 #Function from the game I made earlier this year
    print()
    time.sleep(1.5)
    # Check the operating system and run the appropriate clear command
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS and Linux
        os.system('clear')

def ani(text, delay=0.04): #Function from the game I made earlier this year
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line

def ani2(text, delay=0.06): #Function from the game I made earlier this year
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line

def ui():
    while True:
        print("-=- Enlistment Data Interface -=-")
        ani("1. View Raw Data")
        ani("2. View Data Visualisation: Do people want to Enlist?")
        ani("3. View Data Visualisation: Why people would Enlist?")
        ani("4. View Averages")
        ani("5. Exit Program")

        ani("Please select an option (1-5): ")
        pc = int(input(""))

        if pc == 1:    
            ani2("Loading...")
            cs()
            print("Raw Data here")

        elif pc == 2:
            ani2("Loading...")
            cs()
            ani("How would you like to view this Data? (a,b)")
            ani("a) View as a Pie Chart")
            ani("b) View as a Bar Chart")
            p2 = input()
            ani2("Loading...")

            if p2 == "a":
                cs()
                print("Pie chart here for if enlist")
            elif p2 == "b":
                cs()
                print("Bar chart here for if enlist")
            else:
                cs()
                ani("INVALID: REASON -> 'Invalid Input'")
                ani("PLEASE TRY AGAIN")
                cs()
            
        elif pc == 3:
            ani2("Loading...")
            cs()
            ani("How would you like to view this Data? (a,b)")
            ani("a) View as a Pie Chart")
            ani("b) View as a Bar Chart")
            p3 = input()
            ani2("Loading...")

            if p3 == "a":
                cs()
                print("Pie chart here for why enlist")
            elif p3 == "b":
                cs()
                print("Bar chart here for why enlist")
            else:
                cs()
                ani("INVALID: REASON -> 'Invalid Input'")
                ani("PLEASE TRY AGAIN")
                cs()

        elif pc == 4:
            ani2("Loading...")
            cs()
            ani("Which Averages would you like to see? (a,b,c,d,e)")
            ani("""a) View Averages for thoughts on Enlistment? (Choices were on a scale of 1-10)
b) View Averages for thoughts on Enlisting for Housing? (Choices were made on a scale of 1-5)
c) View Averages for thoughts on Enlisting for Employment? (Choices were made on a scale of 1-5)
d) View Averages for thoughts on Enlisting for Eduucation? (Choices were made on a scale of 1-5)
e) View Averages for thoughts on Enlisting for Civil Duty? (Choices were made on a scale of 1-5)""")
            p4 = input()
            ani2("Loading...")

            if p4 == "a":
                cs()
                print("average calculation for enlistment")
            elif p4 == "b":
                cs()
                print("average calculation for housing")
            elif p4 == "c":
                cs()
                print("average calculation for employment")
            elif p4 == "d":
                cs()
                print("average calculation for education")
            elif p4 == "e":
                cs()
                print("average calculation for civil duty")
            else:
                cs()
                ani("INVALID: REASON -> 'Invalid Input'")
                ani("PLEASE TRY AGAIN")
                cs()
        elif pc == 5:
            ani("Exiting Program...")
            ani("Thank you for using the 'Enlistment Data Interface'")
            cs()
            break
        else:
            ani("INVALID: REASON -> 'Invalid Input'")
            ani("PLEASE TRY AGAIN")
            cs()

if __name__ == "__main__":
    ui()