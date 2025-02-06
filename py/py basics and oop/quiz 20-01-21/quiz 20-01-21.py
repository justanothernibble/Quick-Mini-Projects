"""
Add custom questions and answers.
Take the quiz and track their score.
Display results at the end of the quiz
"""

import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

import pandas as pd

while True:
    qs = pd.read_csv('questions.csv') # enters CSV into DF
    choice = int(input("What would you like to do?\n1. Take the quiz\n2. View current Q&A\n3. Add a question\n4. Remove a question\n5. Exit\n> "))
    if choice == 1: # Take the quiz
        score = 0 # initialises score to 0
        for i in range(len(qs)):
            ans = input((f"Question {i+1}: {qs.iat[i,0]}\n> ")) # asks the question
            if ans == qs.iat[i,1]: # if answer is equal to second row
                print("Correct! +1 Point") # tells user that their answer is correct
                score+=1 # adds 1 to score
            else:
                print("Wrong!")
        print(f"Your score is: {score}. Well done!") # tells user their score
    elif choice == 2: # View Qns
        for i in range(len(qs)): # iterates through the DF, printing each Row
            print(f"\nQ:{qs.iat[i,0]}\nA:{qs.iat[i,1]}") # this just makes it look nice
            print("")
    elif choice == 3: # Add Qn
        try: # incase of error since users can be stupid
            qn = input("What is your question?\n> ") # asks to input qn
            an = input("What is your answer?\n> ") # asks userr to input answer
            qna = {'Question': qn, 'Answer': an} # dictionary of Qn and Answer
            qs.loc[len(qs)] = qna # add the question and answer to end of DF
            qs.to_csv('questions.csv', index=False) # Save the updated DataFrame back to the CSV file
        except Exception as e: # error handling
            print(f"Error: {e}") # tells user the error
    elif choice == 4: # Remove qn
        qn = input("What question do you want to remove?\n> ") # asks the question to be removed
        found = False # flag to know if its been found
        for i in range(len(qs)): # iterates through each row
            if qs.iat[i,0] == qn: # if the question in the row matches, then:
                qs = qs.drop(i).reset_index(drop=True) # delete row and reset indexes
                qs.to_csv('questions.csv', index=False) # updates doc
                found = True # let computer know its been found
                print("Question removed successfuly.") # tell the user its been removed successfully
                break # end the loop
        if found == False: # if not found, then:
            print("Question not found.") # tell the user that it hasnt been found
    elif choice == 5: # exiting the app
        print("Exiting the quiz app.") # tells the user its exiting
        break # ends while True loop
    else:
        print("Invalid choice. Please try again.") # incase the user gives a choice unasked for
