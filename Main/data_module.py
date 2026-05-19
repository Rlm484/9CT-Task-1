import sys
import os
import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

def ani2(text, delay=0.085): #Function from the game I made earlier this year
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line

def raw_data(): #dataframe w/ raw data
    rd_df = pd.read_csv(
                            'Main/data/enlistment_data.csv',
                            header=None,
                            names = ['Recipient No.','Enlistment Rating (1-10)','Housing Rating (1-5)','Employment Rating (1-5)','Education Rating (1-5)','Civil Duty Rating (1-5)','Highest Rated Section']
                            )
    print(rd_df)

def enlist_avg(): #avg of the enlistment rating column in raw data
    rd_df = pd.read_csv(
                            'Main/data/enlistment_data.csv',
                            header=None,
                            names = ['Recipient No.','Enlistment Rating (1-10)','Housing Rating (1-5)','Employment Rating (1-5)','Education Rating (1-5)','Civil Duty Rating (1-5)','Highest Rated Section']
                            )
    avg = rd_df['Enlistment Rating (1-10)'].mean()
    ani(f"The average score for peoples thoughts on Enlistment (on a scale of 1-10; simplified to 2.d.p) is: [{avg:.2f}/10]")

def housing_avg(): #avg of the housing rating column in raw data
    rd_df = pd.read_csv(
                            'Main/data/enlistment_data.csv',
                            header=None,
                            names = ['Recipient No.','Enlistment Rating (1-10)','Housing Rating (1-5)','Employment Rating (1-5)','Education Rating (1-5)','Civil Duty Rating (1-5)','Highest Rated Section']
                            )
    avg = rd_df['Housing Rating (1-5)'].mean()
    ani(f"The average score for peoples thoughts on Enlisting for Housing (on a scale of 1-5; simplified to 2.d.p) is: [{avg:.2f}/5]")

def employ_avg(): #avg of the employment rating column in raw data
    rd_df = pd.read_csv(
                            'Main/data/enlistment_data.csv',
                            header=None,
                            names = ['Recipient No.','Enlistment Rating (1-10)','Housing Rating (1-5)','Employment Rating (1-5)','Education Rating (1-5)','Civil Duty Rating (1-5)','Highest Rated Section']
                            )
    avg = rd_df['Employment Rating (1-5)'].mean()
    ani(f"The average score for peoples thoughts on Enlisting for Employment (on a scale of 1-5; simplified to 2.d.p) is: [{avg:.2f}/5]")

def edu_avg(): #avg of the education rating column in raw data
    rd_df = pd.read_csv(
                            'Main/data/enlistment_data.csv',
                            header=None,
                            names = ['Recipient No.','Enlistment Rating (1-10)','Housing Rating (1-5)','Employment Rating (1-5)','Education Rating (1-5)','Civil Duty Rating (1-5)','Highest Rated Section']
                            )
    avg = rd_df['Education Rating (1-5)'].mean()
    ani(f"The average score for peoples thoughts on Enlisting for Education (on a scale of 1-5; simplified to 2.d.p) is: [{avg:.2f}/5]")

def cd_avg(): #avg of the civil duty rating column in raw data
    rd_df = pd.read_csv(
                            'Main/data/enlistment_data.csv',
                            header=None,
                            names = ['Recipient No.','Enlistment Rating (1-10)','Housing Rating (1-5)','Employment Rating (1-5)','Education Rating (1-5)','Civil Duty Rating (1-5)','Highest Rated Section']
                            )
    avg = rd_df['Civil Duty Rating (1-5)'].mean()
    ani(f"The average score for peoples thoughts on Enlisting for Civil Duty (on a scale of 1-5; simplified to 2.d.p) is: [{avg:.2f}/5]")

def bcif(): #bar chart if enlist
    fig, ax = plt.subplots()

    rd_df = pd.read_csv(
                        'Main/data/enlistment_data.csv',
                        header=None,
                        names=['Recipient No.',
                               'Enlistment Rating (1-10)',
                               'Housing Rating (1-5)',
                               'Employment Rating (1-5)',
                               'Education Rating (1-5)',
                               'Civil Duty Rating (1-5)',
                               'Highest Rated Section']
                        )
    
    ratings = rd_df.iloc[:, 1].tolist()

    score_repeat = []
    for i in range(1, 11):
        score_repeat.append(ratings.count(i))

    colours = plt.cm.RdYlGn(np.linspace(0,1,10))

    plt.xticks(range(1,11))
    plt.ylim(0,37)
    ax.yaxis.set_minor_locator(plt.MultipleLocator(1))
    plt.bar(range(1,11),score_repeat,color=colours)
    plt.title("Enlistment Ratings Across GHS")
    plt.xlabel("Score Submitted (1-10)")
    plt.ylabel("Number of Recipients")

    plt.show()

def bcwhy(): #bar chart why enlist
    fig, ax = plt.subplots()

    rd_df = pd.read_csv(
                        'Main/data/enlistment_data.csv',
                        header=None,
                        names=['Recipient No.',
                               'Enlistment Rating (1-10)',
                               'Housing Rating (1-5)',
                               'Employment Rating (1-5)',
                               'Education Rating (1-5)',
                               'Civil Duty Rating (1-5)',
                               'Highest Rated Section']
                        )
    
    ratings = rd_df['Highest Rated Section'].value_counts()

    colours = plt.cm.PuBu(np.linspace(0,1,len(ratings)))

    plt.ylim(0,37)
    ax.yaxis.set_minor_locator(plt.MultipleLocator(1))
    ax.bar(ratings.index,ratings.values,color=colours)
    plt.title("Peoples Highest Rated Reason to Enlist")
    plt.xlabel("Reasons to Enlist")
    plt.ylabel("Number of Recipients")

    plt.show()

def pci(): #pie chart if enlist
    rd_df = pd.read_csv(
                        'Main/data/enlistment_data.csv',
                        header=None,
                        names=['Recipient No.',
                               'Enlistment Rating (1-10)',
                               'Housing Rating (1-5)',
                               'Employment Rating (1-5)',
                               'Education Rating (1-5)',
                               'Civil Duty Rating (1-5)',
                               'Highest Rated Section']
                        )
    
    times = rd_df["Enlistment Rating (1-10)"].value_counts().sort_index()

    pltmap=plt.get_cmap("Pastel2")
    colors = pltmap(np.linspace(0,1,len(times)))

    plt.figure(figsize=(6,6))
    plt.pie(
        times,
        labels=times.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors
    )

    plt.title("Enlistment Ratings across GHS [Percentages rounded to 1d.p]")
    plt.axis("equal")
    plt.show()

def pcw(): #pie chart why enlist
    rd_df = pd.read_csv(
                        'Main/data/enlistment_data.csv',
                        header=None,
                        names=['Recipient No.',
                               'Enlistment Rating (1-10)',
                               'Housing Rating (1-5)',
                               'Employment Rating (1-5)',
                               'Education Rating (1-5)',
                               'Civil Duty Rating (1-5)',
                               'Highest Rated Section']
                        )
    
    times = rd_df["Highest Rated Section"].value_counts()

    pltmap=plt.get_cmap("Pastel1")
    colors = pltmap(np.linspace(0,1,len(times)))

    plt.figure(figsize=(6,6))
    plt.pie(
        times,
        labels=times.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors
    )

    plt.title("Peoples Highest Rated Reason to Enlist [Percentages rounded to 1d.p]")
    plt.axis("equal")
    plt.show()

pci()