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

#### Most importantly, code n' chill! 🙆 💻 ☕️
