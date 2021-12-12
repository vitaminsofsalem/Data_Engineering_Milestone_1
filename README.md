# Data Engineering & Visualization Milestone 1
## Exploring the history of the olympics

- The project aims to explore the long history of the olympic games
- courtesy to heesoo37 for making great efforts in providing us with the following useful and rich data : [(original source)](https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results?select=athlete_events.csv)

## basic project structure
### In order to make the project source more modular and easier to work with, the following protocols should be applied.
- keep the data files and the source code in separate folders, it is recommended to organize hierarchically when possible.
- separate the code base into notebooks and .py files, the notebook should have a clean and concise presentation of the project.
- try to use variable and function labels that accurately reflect the purpose.
- each notebook should tell a story, so it is important that they maintain a clean and concise presentation.
- .py files are useful for defining functions useful for data pipelining,transformation and other tasks.

#### good example 😊
```bash
--project
    |-OlympicExploration.ipynb
    |-ParticipationsByCountry.ipynb
    |-ParticipantsHealth.ipynb
    |-data
    |   |-athlete_events.csv
    |   |-participants.csv
    |   ...etc
    |
    |-data_proc
    |   |-DataFiltering.py
    |   |-DataRemapping.py
    |   ...etc
    |
 ```

 - heirarchical organization of files.
 - useful and intuitive labels
 - code modularity, simplifying the presentation on the notebook.

#### bad example 😛
```bash
--project
    |-Untiled 1.ipynb 
    |-athlete_events.csv
    |-participants.csv
    |-djfkdjfj.csv
    ...etc
```


 - lack of organization and meaningless file labels (e.g. Untitled 1.ipynb, x1.py)
 - all proj implementations in one file, making the notebook look verbose and distracting

## EDA Process Explained
#### Overview of the used dataset

The dataset that was used for this project was the 'athlete_events.csv' which counts a 120 years of data of all the olympic games held Athens 1896 till Rio 2016. This dataset was gathered using R programming language and posted on Kaggle. It contains 15 columns namely:
- Id
- Name
- Sex
- Age
- Height
- Weight
- Team
- NOC ( country code )
- Games
- Year
- Season
- City
- Sport
- Event
- Medal

The names are self descriptive so no need to add descriptions.
When we ran dataset.info() and dataset.describe() commands, we discoverd that the dataset contains NULL values in the Age, Height, Weight, Medal columns that were dealt with accordingly as will be explained below. The dataset also contains 271116 entries out of which 135571 are unique entries / players.

#### Project Goals and Motivation for it

This project is a school project that was assigned to us, to document the EDA process that we take towards this dataset. We were tasked to come up with a few research questions and explore them using the dataset at hand and indeed that is what we do.
the Research questions proposed are:
- Relationship between obesity rates in participants and NOC ( country )
- What is the the ration of men to women as well as the top 10 most popular sports for men and women ?
- What is the most popular city to hold the olympics?
- which cities hosted the largest number of athletes?
We explore all those research questions in the notebook

#### General Description of steps taken in the project

- As mentioned above, we first started by describing and seeing what the data is like:
- After which we realized that there are null values in the dataset and proceed to impute the dataset
- After imputing / cleaning the dataset, we proceed to explore our research questions
- We visualized data when needed to help pass through the information to the reader / viewer in an easier to digest way.
- All the data and in detail implementations of steps taken to reach research questions, exploring dataset, imputation techniques used are all mentioned in the notebook markdown


#### This is the end of this readme file. I hope you enjoyed and...  Most importantly, code n' chill! 🙆 💻 ☕️
