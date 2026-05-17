# **Assessment Task 1 2026**
# **Phase 1 - Identifying and Defining**
## Mindmap
![Mindmap](Images/Mindmap.png)

[Miro Mindmap Link!](https://miro.com/app/board/uXjVHdK6NuQ=/?share_link_id=179304639963)

## Defining My Purpose
### Hypothesis: *Students in Gosford High are LESS LIKELY to enlist for the ADF after High School*

## Requirement Outline
### Functional Requirements
>Data Loading: It should be able to load CSV files into data frames while also handling errors or invalid input in a way that doesn't crash the program. The program should also be able to open charts and graphs without any issues or missing images/pieces of data within the files.

> Data Cleaning: Though there shouldn't be any missing values of data (due to it coming from a survey and being manually typed in), however if there are missing values the program should be able to skip over that row of the data set to prevent errors. The program should also be able to filter out information the user doesn't wish to see and be able to group specific columns the user does wish to see.

> Data Analysis: The program should have the ability to display the mean for two responses in order to summarise the data shown.

> Data Visualisation: The data will be displayed with panda dataframes along with matplotlib pie charts and bar graphs.

> Data Reporting: The system should output charts that contribute to answering the original question in a way that allows users to visualise the data. The system should also be able to calculate averages from the dataset and display the raw data itself. There should also be a UI for the user to interact with in order to make a successful program. In order to do all of the above, I will need Pandas for data display, Matplotlib for charts, and a CSV file for the data containment.

### Non-Functional Requirements
> Usability: The UI should offer multiple choices for the user to choose from, while also being labelled in a way that clearly lets the user know what they are actually selecting (E.g. instead of a choice being [See Graph], it should instead be [Data Visualisation of Survey Outcomes]). On top of this, the README should...

> Reliability: The system should be able to register invalid responses and instead output an [INVALID: PLEASE TRY AGAIN] message for the user. This should prevent most errors, however, should other errors appear, a try/except OR if/elif/ekse code will run to register any outputs or inputs that could cause issues, presenting a different error code, [ERROR: SYSTEM MALFUNCTION, PLEASE TRY AGAIN]. In regards to data integrity, the system should be able to present the collected data as is, whether the form differs, the core data should remain accurate and consistent throughout the system. This data is also collected through public survey, so averages should be properly calculated through python functions, again remaining consistent with the original data. In regards to the viewable raw data, it should be complete and discernible for users to view and compare to the summarised displays. On top of all this, the responses from the actual google form will not be displayed with names, but the correlating order in submition to ensure privacy for those responding as well, ensuring data integrity for users. Within the actual interface itself, user names will not be stored, and all variables related to it will be cleared and reset once the program ends.

### Use-Case
>  
    Actor: User

    Goal: To have the capability to view data in a way that will give the user a clear answer or response to the defined hypothesis just by interacting with the system/UI and accessing the data within.

    Preconditions:

    - The data from the survey is already preloaded onto a CSV file within the repository, and turned into graphs, dataframes, and calculated averages

    - The user is able to access the system through forking a github repository, allowing them to access the data within through cloning it through Github Desktop (therefore the user must have access to Github along with Github Desktop)

    Main Flow:
    User runs the main.py code and enters in their UID

    User views/sees the user interface along with all the choices/options

    User chooses one of the 5 different options with different outcomes:
    1. View the Data Frame of Raw Data?
        a) Import pandas dataframe and present it to the user
    2. See the Visualisation of whether people wish to enlist?
        a) View as a Pie chart?
        b) View as a Bar chart?
    3. See the Visualisation of why people wish to enlist?
        a) View as a Pie chart?
        b) View as a Bar chart?
    4. View averages of survey outcomes?
        a) View the averages of the Pro-Enlist faction?
        b) View the averages of people's thoughts on enlisting for Housing opportunities (no./5)?
        c) View the averages of people's thoughts on enlisting for Employment opportunities (no./5)?
        d) View the averages of people's thoughts on enlisting for Education opportunities (no./5)?
        e) View the averages of people's thoughts on enlisting for Civil Duty (no./5)?
    5. Exit

    System runs code based on what the user chose to do, including sub-selection. Whether that be importing/presenting data frames, opening/presenting graphs or charts, calculating averages for all outcomes/choices, and closing/ending the loop or program.

    Postconditions:

    - User has viewed and/or interacted with the data.

    Any valid updates are saved by the system.

    Data remains available for further queries or analysis.

# **Phase 2 - Researching and Planning**
## Researching my Chosen Issue
### Due to the lack of information online related to the hypothesis, only 3 websites are listed below:
### https://www.abs.gov.au/articles/australian-defence-force-service
### https://theforge.defence.gov.au/article/deep-dive-our-tiny-recruitment-pool
### https://generationsurvey.org.au/data_story/young-australians-aspire-to-join-the-defence-force/?utm_source=copilot.com

## Discussing my Findings - SEEC/L
### In regards to the overall information retrieved from the websites listed, a common point I've found is the fact that only a very small minority of the population actually serve in the army. You see, when refering to enlistment, there are actually 2 major parts. The first is choosing to enlist (signing up for the army), and the second is being actually chosen to be a part of the ADF. When seeing if a young person is eligible to serve, the ADF does have to still see if they meet the criteria (e.g. health, criminal records, etc). These factors make the pool of recruits even smaller for the ADF, subsequently, only 16% of young Australians both meet the criteria to qualify for  the ADF, and actually show the interest to join the military, causing only a minority to serve. 

### Leading on from the last paragraph, the majority of people who enlist seem to be university graduates. When looking at the goverment sight abs, we can see that the age that gets the most enlisters is 25-34, the average age where people have graduated from university. The total count in fact, was 21,168 people in 2021, compared to the runnerups (15-24) being 14,710, a full 144% increase in people. This data can allow us to corrolate the fact that people who want to go to the army probably want to get their education out of the way before starting, showing further evidence of university graduates probably being the biggest portion of the ADF. However, following the last paragraph, 21,168 people isnt actually a large number. Australia had 25.4 million people in 2021, meaning that the largest portion in the people enlisting (age wise), doesn't even add up to 1% of the population. This also further shows the fact that the amount of people that enlist are a very small minority overall.

## Aquiring my Data
> ### [GOOGLE FORM!: What are YOUR thoughts on Military?](https://forms.gle/VNycTJ2GhKjxYJcd9)
### The above is a google form for the students of Gosford High School, filled in by peers across the school community.

## Teenage thoughts on Enlistment -  Data Dictonary
|Field|Datatype|Format for Display|Description|Example|Validation|
|-|-|-|-|-|-|
|Submition_Number|str|X...X|Number representing the responders in the same order the responses come in.|#23|Must have a # in front to discern from the row numbers. Following should be 1-2 numbers.|
|Enlistment Thoughts 1-10|int|N...N|Scale of 1-10 on how responders view enlistment. 10 being 'AMAZING', 1 being 'HORRIBLE'.|10|Must be a number consisting of 1-2 digits lying on the range 1-10.|
|Enlistment for Housing 1-5|int|N|Scale of 1-5 on responders thought on enlistig for housing if they were to enlist.|3|Must be a number consisting of 1 digit lying on the range 1-5.|
|Enlistment for Employment 1-5|int|N|Scale of 1-5 on responders thought on enlistig for emplyment if they were to enlist.|5|Must be a number consisting of 1 digit lying on the range 1-5.|
|Enlistment for Education 1-5|int|N|Scale of 1-5 on responders thought on enlistig for education if they were to enlist.|2|Must be a number consisting of 1 digit lying on the range 1-5.|
|Enlistment for Civil Duty 1-5|int|N|Scale of 1-5 on responders thought on enlistig for civil duty if they were to enlist.|4|Must be a number consisting of 1 digit lying on the range 1-5.|

# **Phase 3 - Producing and Implementing**