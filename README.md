# First_project
Data engineering gitlab template

install badge
[![CI](https://github.com/nogibjj/First_project/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/First_project/actions/workflows/install.yml)

lint badge
[![CI](https://github.com/nogibjj/First_project/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/First_project/actions/workflows/lint.yml)

test badge
[![CI](https://github.com/nogibjj/First_project/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/First_project/actions/workflows/test.yml)

format badge
[![CI](https://github.com/nogibjj/First_project/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/First_project/actions/workflows/format.yml)


Requirements

- Python script using Pandass for descriptive statistics
- Read a dataset (CSV or Excel)
- Generate summary statistics (mean, median, standard deviation)
- Create at least one data visualization

Dataset
- Basketball Referemce 2023-2024 NBA Player Stats: Per Game
    - https://www.basketball-reference.com/leagues/NBA_2024_per_game.html#per_game_stats

Required Files

- requirements.txt
    - required dependencies to run this file
    - provides required versions of devops and web components
- Makefile
    - instructions to install, format, lint, and test python files
- devcontainer
    - devcontainer.json
        - contains docker container for python 3 dependencies
- main.py
    - contains code to use pandas to read dataset, generate summary statistics, visualization, and a report
- test_main.py
    - contains code to test main.py file
- hello.yml
    - provides the functionality to do CI runs
- .gitignore
    - ignores unecessary files and programs to prevent installation conflicts

Steps
- set up github repository files such as requirements.txt, Makefile, devcontainer, hello.yml, etc.
- create main.py file containing python script to load in CSV file, create summary statistics, plot visualization, and generate a summary report
- test main.py file by making a test_main.py file
- perform a CI/CD run verifying that the code has passed all the linters and tests