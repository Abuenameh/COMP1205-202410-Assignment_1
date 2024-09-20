# Assignment 1 - Fundamentals of Python Programming

**# Fundamentals of Programming**

This assignment will give you experience on the use of:

1. Integers and floats
2. Mathematical operations
3. The float(), int(), round(), print(), and input()functions
4. Importing a Python module

Click this link to accept the assignment: https://classroom.github.com/a/usvjo0H7 

**Question 1**

Programs are good at performing routine mathematical calculations. By way of illustration, you will write a program to calculate the materials needed for an ornamental garden according to the design below. In this design, the blue areas represent flowerbeds and the yellow areas are filled with stone, mulch, or other fill material. The garden is a perfect square. The four outer flowerbeds are congruent semicircles and the central flowerbed is a perfect circle.
Project Description / Specification
Your program should prompt the user for the following information:
1. The side length (in feet) of the finished garden.
2. The recommended spacing (in feet) between plants.
3. The depth (in feet) of the flowerbeds.
4. The depth (in feet) of the filled areas.

Next estimate the number of plants and the amount of fill and flowerbed soil needed.
Finally, it should report the following quantities needed for the garden:
1. Number of plants for each type of flowerbed (semicircle and circle) and total number of plants for the garden.
2. Cubic yards of soil for each type of flowerbed (semicircle and circle) and total cubic yards of soil for the garden, rounded to one decimal place.
3. Total cubic yards of fill material for the garden, rounded to one decimal place.
    
<img width="136" alt="1Q2" src="https://github.com/user-attachments/assets/1ff1f546-f67d-47d9-a86a-983331c4cb7a">

Hint: Solve the problem using paper, pencil and calculator so you understand the problem before trying to program it.

Sample Run

Calculate Garden requirements

-----------------------------

Enter length of side of garden (feet): 10

Enter spacing between plants (feet): 0.5

Enter depth of garden soil (feet): 0.8333

Enter depth of fill (feet): 0.8333

-----------------------------

Requirements

Plants for each semicircle garden: 39

Plants for the circle garden: 78

Total plants for garden: 234

Soil for each semicircle garden: 0.3 cubic yards

Soil for the circle garden: 0.6 cubic yards

Total soil for the garden: 1.8 cubic yards

Total fill for the garden: 1.3 cubic yards

**Question 2**

Create a program that prompts for a positive number greater than 2 (check this condition), then keeps taking the square root of this number until the square root is less than 2. Print the value each time the square root is taken, along with the number of times the operation has been completed. For example:
Enter an integer greater than 2: 20

1: 4.472

2: 2.115

3: 1.454

**Question 3**

The factorial of n (written n!) is the product of the integers between 1 and n. Thus 4! = 1 * 2 * 3 * 4 = 24. By definition, 0! = 1. Factorial is not defined for negative numbers.

(a) Write a program that asks the user for a non-negative integer and computes and prints the factorial of that integer. You'll need a while loop to do most of the work—this is a lot like computing a sum, but it's a product instead. And you'll need to think about what should happen if the user enters 0.

(b) Now modify your program so that it checks to see if the user entered a negative number. If so, the program should print a message saying that a nonnegative number is required and ask the user the enter another number. The program should keep doing this until the user enters a nonnegative number, after which it should compute the factorial of that number.

Hint: you will need another while loop before the loop that computes the factorial. You should not need to change any of the code that computes the factorial!

**Question 4**

Write a program that prompts the user to enter a point (x, y) and checks whether the point is within the rectangle centered at (0, 0) with width 10 and height 5. For example, (2, 2) is inside the rectangle and (6, 4) is outside the rectangle, as shown in the Figure. 
<img width="386" alt="Screenshot 2024-09-18 at 7 47 41 PM" src="https://github.com/user-attachments/assets/a11e3e98-f47b-466e-a774-b1a982242af7">

(Hint: A point is in the rectangle if its horizontal distance to (0, 0) is less than or equal to 10 / 2 and its vertical distance to (0, 0) is less than or equal to 5 / 2.) 
Here are sample runs of the program:

Sample 1:

Enter a point with two coordinates: 2, 2

Point (2.0, 2.0) is in the rectangle

Sample 2:

Enter a point with two coordinates: 6, 4

Point (6.0, 4.0) is not in the rectangle

**Question 5**

A teacher wants a program to keep track of grades for students and decides to create program as follows:

Each student will be described by three pieces of data: his/her name, his/her score on test #1, and his/her score on test#2.

The teacher must enter the class size such as 5 students 

The teacher then is prompted to enter the grades for students starting with students 1 to n depending on the class size

The program then computes the student grade, an average of the test scores entered

The program then computes the letter grade for the student corresponding to a student’s average such that:

– (80-100] will return A – please note that ‘(80-100]’ means >80 and up to and including 100 

– (60-80] will return B

– (49 - 60] will return C

– <50 will return F

The program then prints the student name and the letter grade attained.
