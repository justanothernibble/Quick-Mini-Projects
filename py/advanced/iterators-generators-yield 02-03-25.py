"""
Create a generator that produces a sequence of numbers based on user input:

    Start number
    End number
    Step size (optional)

The user can iterate through the sequence, and the program should 
handle edge cases like invalid inputs or step sizes of zero.
Steps to Build the Project:

    User Input: Collect the start, end, and step size.
    Generator Function: Use yield to produce the numbers one by one.
    Error Handling: Handle invalid ranges or zero step sizes.
    Output: Print each number as the user iterates through the sequence."""#


def num_gen(start, end, step):
    if step == 0:
        raise ValueError("Step size is 0")
    if (start<end and step<0) or (start>end and step>0):
        raise ValueError("Going in the wrong direction")
    while (start <= end and step>0) or (start >= end and step <0):
        yield start
        start +=step

try:
    start = int(input("Enter start value -> "))
    end = int(input("Enter end value -> "))
    step = int(input("Enter step value -> "))

    for num in num_gen(start, end, step):
        print(num)
        generated = True
    
    if not generated:
        print("No numbers generated")
except Exception as e:
    print(f"Error: {e}")