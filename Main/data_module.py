import sys
import os
import time
import pandas as pd
#import matplotlib

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

def ani2(text, delay=0.08): #Function from the game I made earlier this year
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line

def raw_data():
    rd_df = pd.read_csv(
                            'Main/data/enlistment_data.csv',
                            header=None,
                            names = ['Entry No.','Enlistment Rating (1-10)','Housing Rating (1-5)','Employment Rating (1-5)','Education Rating (1-5)','Civil Duty Rating (1-5)']
                            )
    print(rd_df)

def enlist_avg():
    rd_df = pd.read_csv(
                            'Main/data/enlistment_data.csv',
                            header=None,
                            names = ['Entry No.','Enlistment Rating (1-10)','Housing Rating (1-5)','Employment Rating (1-5)','Education Rating (1-5)','Civil Duty Rating (1-5)']
                            )
    avg = rd_df['Enlistment Rating (1-10)'].mean()
    ani(f"The average score for peoples thoughts on Enlistment (on a scale of 1-10; simplified to 2.d.p) is: [{avg:.2f}/10]")

def housing_avg():
    rd_df = pd.read_csv(
                            'Main/data/enlistment_data.csv',
                            header=None,
                            names = ['Entry No.','Enlistment Rating (1-10)','Housing Rating (1-5)','Employment Rating (1-5)','Education Rating (1-5)','Civil Duty Rating (1-5)']
                            )
    avg = rd_df['Housing Rating (1-5)'].mean()
    ani(f"The average score for peoples thoughts on Enlisting for Housing (on a scale of 1-5; simplified to 2.d.p) is: [{avg:.2f}/5]")

def employ_avg():
    rd_df = pd.read_csv(
                            'Main/data/enlistment_data.csv',
                            header=None,
                            names = ['Entry No.','Enlistment Rating (1-10)','Housing Rating (1-5)','Employment Rating (1-5)','Education Rating (1-5)','Civil Duty Rating (1-5)']
                            )
    avg = rd_df['Employment Rating (1-5)'].mean()
    ani(f"The average score for peoples thoughts on Enlisting for Employment (on a scale of 1-5; simplified to 2.d.p) is: [{avg:.2f}/5]")

def edu_avg():
    rd_df = pd.read_csv(
                            'Main/data/enlistment_data.csv',
                            header=None,
                            names = ['Entry No.','Enlistment Rating (1-10)','Housing Rating (1-5)','Employment Rating (1-5)','Education Rating (1-5)','Civil Duty Rating (1-5)']
                            )
    avg = rd_df['Education Rating (1-5)'].mean()
    ani(f"The average score for peoples thoughts on Enlisting for Education (on a scale of 1-5; simplified to 2.d.p) is: [{avg:.2f}/5]")

def cd_avg():
    rd_df = pd.read_csv(
                            'Main/data/enlistment_data.csv',
                            header=None,
                            names = ['Entry No.','Enlistment Rating (1-10)','Housing Rating (1-5)','Employment Rating (1-5)','Education Rating (1-5)','Civil Duty Rating (1-5)']
                            )
    avg = rd_df['Civil Duty Rating (1-5)'].mean()
    ani(f"The average score for peoples thoughts on Enlisting for Civil Duty (on a scale of 1-5; simplified to 2.d.p) is: [{avg:.2f}/5]")
