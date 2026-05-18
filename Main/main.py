import sys
import os
import time
from data_module import(
    raw_data,
    cs,
    ani,
    ani2,
    enlist_avg,
    housing_avg,
    employ_avg,
    edu_avg,
    cd_avg

)

def ui():
    ani("Welcome User to the 'Enlistment Data Interface'! What shall we call you during your time here?")
    name = input("")
    ani(f"Hello {name}, we hope you enjoy your stay")
    ani2(f"USER: {name}")
    ani2("ENTERING DATA INTERFACE...")
    cs()
    while True:
        print("-=- Enlistment Data Interface -=-")
        ani(f"USER: {name}")
        ani("1. View Raw Data")
        ani("2. View Data Visualisation: Do people want to Enlist")
        ani("3. View Data Visualisation: Main reason people would Enlist")
        ani("4. View Averages")
        ani("5. Exit Program")
        print("")
        ani("Please select an option (1-5): ")
        pc = input("")

        if pc == "1":    
            ani2("Loading...")
            cs()
            raw_data()
            choice="n"
            while choice.lower()=="n":
                ani("Would you like to exit the sub-program? (y/n)")
                choice = input("")
                if choice.lower() == "y":
                    ani2("Exiting sub-program...")
                    cs()
                else:
                    print("")

        elif pc == "2":
            ani2("Loading...")
            cs()
            ani("How would you like to view this Data? (a,b)")
            ani("a) View as a Pie Chart")
            ani("b) View as a Bar Chart")
            ani("c) View both Charts")
            ani("d) Exit sub-program")
            p2 = input()

            if p2 == "a":
                ani2("Loading...")
                cs()
                print("Pie chart here for if enlist")
            elif p2 == "b":
                ani2("Loading...")
                cs()
                print("Bar chart here for if enlist")
            elif p2 == "c":
                ani2("Loading...")
                cs()
                print("All charts here")
            
            elif p2 == "d":
                ani2("Exiting sub-program...")
                cs()

            else:
                cs()
                ani("INVALID: REASON -> 'Invalid Input'")
                ani("PLEASE TRY AGAIN")
                cs()
            
        elif pc == "3":
            ani2("Loading...")
            cs()
            ani("How would you like to view this Data? (a,b)")
            ani("a) View as a Pie Chart")
            ani("b) View as a Bar Chart")
            ani("c) View both Charts")
            ani("d) Exit sub-program")
            p3 = input()

            if p3 == "a":
                ani2("Loading...")
                cs()
                print("Pie chart here for why enlist")

            elif p3 == "b":
                ani2("Loading...")
                cs()
                print("Bar chart here for why enlist")

            elif p3 == "c":
                ani2("Loading...")
                cs()
                print("All charts here")

            elif p3 == "d":
                ani2("Exiting sub-program...")
                cs()

            else:
                cs()
                ani("INVALID: REASON -> 'Invalid Input'")
                ani("PLEASE TRY AGAIN")
                cs()

        elif pc == "4":
            ani2("Loading...")
            cs()
            ani("Which Averages would you like to see? (a,b,c,d,e,f,g)")
            ani("""a) View Averages for thoughts on Enlistment? (Choices were on a scale of 1-10)
b) View Averages for thoughts on Enlisting for Housing? (Choices were made on a scale of 1-5)
c) View Averages for thoughts on Enlisting for Employment? (Choices were made on a scale of 1-5)
d) View Averages for thoughts on Enlisting for Eduucation? (Choices were made on a scale of 1-5)
e) View Averages for thoughts on Enlisting for Civil Duty? (Choices were made on a scale of 1-5)
f) View all Averages
g) Exit sub-program""")

            p4 = input()

            if p4 == "a":
                ani2("Loading...")
                cs()
                ani2("Calculating...")
                enlist_avg()
                print("")
                choice = "n"
                while choice.lower()=="n":
                    ani("Would you like to exit the sub-program? (y/n)")
                    choice = input("")
                    if choice.lower() == "y":
                        ani2("Exiting sub-program...")
                        cs()
                    else:
                        print("")

            elif p4 == "b":
                ani2("Loading...")
                cs()
                ani2("Calculating...")
                housing_avg()
                print("")
                choice = "n"
                while choice.lower()=="n":
                    ani("Would you like to exit the sub-program? (y/n)")
                    choice = input("")
                    if choice.lower() == "y":
                        ani2("Exiting sub-program...")
                        cs()
                    else:
                        print("")

            elif p4 == "c":
                ani2("Loading...")
                cs()
                ani2("Calculating...")
                employ_avg()
                print("")
                choice = "n"
                while choice.lower()=="n":
                    ani("Would you like to exit the sub-program? (y/n)")
                    choice = input("")
                    if choice.lower() == "y":
                        ani2("Exiting sub-program...")
                        cs()
                    else:
                        print("")

            elif p4 == "d":
                ani2("Loading...")
                cs()
                ani2("Calculating...")
                edu_avg()
                print("")
                choice = "n"
                while choice.lower()=="n":
                    ani("Would you like to exit the sub-program? (y/n)")
                    choice = input("")
                    if choice.lower() == "y":
                        ani2("Exiting sub-program...")
                        cs()
                    else:
                        print("")

            elif p4 == "e":
                ani2("Loading...")
                cs()
                ani2("Calculating...")
                cd_avg()
                print("")
                choice = "n"
                while choice.lower()=="n":
                    ani("Would you like to exit the sub-program? (y/n)")
                    choice = input("")
                    if choice.lower() == "y":
                        ani2("Exiting sub-program...")
                        cs()
                    else:
                        print("")

            elif p4 == "f":
                ani2("Loading...")
                cs()
                ani2("Calculating...")
                enlist_avg()
                housing_avg()
                employ_avg()
                edu_avg()
                cd_avg()
                print("")
                choice = "n"
                while choice.lower()=="n":
                    ani("Would you like to exit the sub-program? (y/n)")
                    choice = input("")
                    if choice.lower() == "y":
                        ani2("Exiting sub-program...")
                        cs()
                    else:
                        print("")

            elif p4 == "g":
                ani2("Exiting sub-program...")
                cs()

            else:
                cs()
                ani("INVALID: REASON -> 'Invalid Input'")
                ani("PLEASE TRY AGAIN")
                cs()

        elif pc == "5":
            ani2("Exiting Program...")
            ani(f"Thank you {name} for using the 'Enlistment Data Interface', we hope you have a wonderful day!")
            cs()
            break

        else:
            ani("INVALID: REASON -> 'Invalid Input'")
            ani("PLEASE TRY AGAIN")
            cs()

if __name__ == "__main__":
    ui()