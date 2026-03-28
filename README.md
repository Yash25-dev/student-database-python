# Student Database System (Python)

This program is used to store and manage student records and calculate their grades based on marks.

## Features
- Input multiple student records
- Unique USN validation (no duplicates allowed)
- Stores marks using tuple
- Uses dictionary to store student details
- Calculates average marks
- Assigns grades based on performance

## How the Program Works

1. User enters the number of students
2. For each student:
   - USN is entered and checked for duplicates
   - Name and marks are entered
   - Data is stored in a dictionary
3. Marks are stored as a tuple
4. All student data is stored in a list
5. After input, the program:
   - Calculates average marks
   - Assigns grade using conditions:
     - Above 90 → A
     - 80–89 → B
     - 70–79 → C
     - Below 70 → Satisfactory
6. Results are displayed for all students

## Concepts Used
- List
- Set
- Tuple
- Dictionary
- Loops
- Conditional statements

## How to Run
1. Install Python
2. Run:
   python student-database-python.py
