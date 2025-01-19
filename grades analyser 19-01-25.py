"""
- **Mini-project**: Grades Analyzer
    
    - Your mini-project for Day 13 could involve using these advanced functions to process a list of students' grades. You might:
        - Use `map()` to adjust the grades (e.g., increase all grades by 5%).
        - Use `filter()` to select students who passed (e.g., grades above 50).
        - Use `reduce()` to calculate the average grade for the class.
"""

from random import randint
import string
from functools import reduce
from math import trunc

class Student():
    def __init__(self, name):
        self.name = name
        self.grade = randint(1,100)
    
students = [Student(name) for name in string.ascii_uppercase[:10]]

while True:
    choice = int(input("What would you like to do?\n1. Adjust grades\n2. See who passed\n3. Calculate average grade\n4. Exit\n5. View current grades\n> "))
    if choice == 1:
        percentage = int(input("Enter the percentage that you want to adjust by\n> "))
        adj = list(map(lambda x: x*((100+percentage)/100), (student.grade for student in students)))
        adjTrunc = list((trunc(grade) for grade in adj))
        for i in range(len(adj)-1):
            print(adjTrunc[i], end=', ')
        print(adjTrunc[len(adjTrunc)-1])
        print("", end='\n')
    elif choice == 2:
        filt = list(filter(lambda x: x>=50, (student.grade for student in students)))
        for i in range(len(filt)-1):
            print(filt[i], end=', ')
        print(filt[len(filt)-1])
        print("", end='\n')
    elif choice == 3:
        avg = trunc(reduce(lambda x, y: x + y, (student.grade for student in students)) / len(students))
        print(f"The average grade is: {avg}\n")
    elif choice == 4:
        break
    elif choice == 5:
        for i in range(len(students)):
            print(f"{students[i].name}: {students[i].grade}")