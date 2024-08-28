Footballer_Skills.py: Explores Basic Python Principles

Submitted by: Evan Balson
### Time spent: 20 days

<img src='https://github.com/Evan-Balson/Footballer_Skills_CLI/blob/main/footballer_skill_CLI.png' />

# Footballer_Skills_CLI
This Python Command Line Interface (CLI) program aims to encapsulate functionalities essential for  comprehensive football player evaluation. This will include an organized code structure, employing  variables, functions, control structures, lists and standard libraries enhancing modularity and readability.


## Description:
Footballer_Skills.py: Explores Essential Python Principles, showcasing the flexibility of this IDE in computing. It will explore fundamental arithmetic, subroutines, and control flow with sample a sample program which we will develop into an advanced program with robust error & exception handlining:


## Basic flow chart for simple progam
<img src='https://github.com/Evan-Balson/Footballer_Skills_CLI/blob/main/basic%20flow%20chart.jpg'/>

### Implement input function to collect player data for:
* [x] Speed
* [x] Shooting
* [x] Passing
* [x] Defending
* [x] Dribbling
* [x] Physicality
### Use an appropriate data structure to store:
* [x] Player skill ratings
* [x] Calculated overall rates
* [x] Corresponding salaries
### Calculate the overall rate using the formula:
* [x] Summation of skill ratings * 100 / 30
* [x] Implement salary estimation logic:
* [x] Overall rate >= 80: Salary = 1000
* [x] Overall rate == 60: Salary = 700
* [x] 45 <= Overall rate < 60: Salary options = 700, 500
* [x] Overall rate == 45: Salary = 500
* [x] 30 <= Overall rate < 45: Salary options = 500, 400
* [x] Overall rate <= 30: Salary = 400
* [x] Print the computed salary value(s) as integers.
### Ensure the program follows a clear structure with appropriate functions:
* [x] Function to collect input
* [x] Function to calculate overall rate
* [x] Function to determine salary
* [x] Function to output results
* [x] (Optional) Add validation and error handling for input values to ensure they are within the range 0-5.


## Flow chart for advanced Program:
* [x] Design pseudocode or draw a flowchart for the program.

<img src='https://github.com/Evan-Balson/Footballer_Skills_CLI/blob/main/advanced%20flow%20chart.png' />



## Solution for Advanced Program:

### Checklist for Functions:
* [x]  Split and pack up coursework 1 code into functions.
* [x]  Implement main() function.
* [x]  Implement calculate_rating() function.
* [x]  Implement calculate_salary() function.
* [x]  Use main() to call other functions:
* [x]  Receive 6 player skill ratings.
* [x]  Calculate the player's overall rating.
* [x]  Calculate the player's salary range.
### Checklist for Input Expansion
* [x]  Adjust the program to ask for:
* [x]  Player ID (2-digit number).
* [x]  Player name.
* [x]  Player date-of-birth (D.o.B) in ISO format (YEAR-MONTH-DATE).
* [x]  Ask for the 6 skills (speed, shooting, passing, defending, dribbling, physicality).
### Checklist for Looping the Code
#### Implement a loop to:
* [x]  Ask for information for three players, or
* [x]  Until the input for user ID is "end".
### Checklist for Calculating Overall Ratings
* [x]  Calculate the players' overall ratings.
* [x]  Store the overall ratings for later use.
### Checklist for Calculating Salary Ranges
* [x]  Calculate the players' salary ranges.
* [x]  Store the salary ranges for later use.
### Checklist for Calculating Players' Ages
* [x]  Calculate each player's age based on year of birth.
* [x]  Store the age for later use.
### Checklist for Tabulating Data
* [x]  Use the tabulate library to display a table summarizing input data in ascending order of user ID.
* [x]  Table columns: UID, Name, D.o.B, Age, Score, Salary Range.
### Checklist for File Writing
* [x]  Save the summary table into a local file named "players.txt".
### Checklist for Input Validation
* [x]  Implement robust input validation:
* [x]  Validate player ID.
* [x]  Validate D.o.B.
* [x]  Validate ratings.
* [x]  Display warning "The rating you entered was invalid" for any input errors.
### Checklist for Data Structures
* [x]  Use appropriate data structures for storing player information.
### Checklist for Code Structures
* [x]  Use appropriate code structures for implementing the functionality.
### Checklist for Distinction Advanced Function
* [x]  Implement advanced() function:
* [x]  Serve as a complimentary main() method.
* [x]  Use the provided file as input instead of user input.
* [x]  Accept filename as an argument.
* [x]  Read user information record from provided file "PlayerData.txt".
* [x]  Use this data as input for the program.
* [x]  Call all other functions and produce a text file output.


## Table of Content:

1. Technologies used
2. Instructions
3. Requirements
4. Contributions
5. License Information

------------------------------------------------------------------------
# 1. TECHNOLOGIES USED:
------------------------------------------------------------------------
1. Python: Used as the primary programming language for developing the application.
2. os: Used for accessing operating system dependent functionality such as file handling.
3. tabulate: Used for creating well-formatted tables to display player information.
4. datetime: Used for manipulating dates and times, crucial for calculating players' ages.
5. re: Used for regular expression operations to validate input data like dates.


------------------------------------------------------------------------
# 2. Instructions:
------------------------------------------------------------------------
1. Clone the repository to your local machine.
2. Navigate to the project directory in the terminal.
3. Install the required Python libraries.
4. Run the Python script.
5. Follow the on-screen prompts to enter player information.
6. The summary table will also be saved to a file named players.txt.



------------------------------------------------------------------------
# 3. Requirements
------------------------------------------------------------------------
## Prerequisites:
1. Python: Ensure you have Python installed on your system. You can download it from python.org.

2. tabulate Library: Install the tabulate library to display formatted tables: pip install tabulate

3. datetime Module: Python's datetime module is used for manipulating dates and times. It should be available by default in your Python installation.

4. re Module: The re module is used for regular expression operations for input validation. It should be available by default in your Python installation.
------------------------------------------------------------------------
# 4. CONTRIBUTIONS
------------------------------------------------------------------------

We welcome contributions from everyone, regardless of their experience level or background.

## How to Contribute:

Testing Contributions: Test the project and report any bugs or issues you encounter. You can also contribute by writing automated tests to improve test coverage.

Feedback and Suggestions: Provide feedback on the project, suggest new features.

------------------------------------------------------------------------
# 5. LICENSE INFORMATION
------------------------------------------------------------------------

## MIT License

Copyright (c) 2024 Evan Balson, Version 1.0

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.






.