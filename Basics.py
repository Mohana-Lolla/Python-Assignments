#1.Write a program to print your name.
print('Lolla Mohana Lakshmi')

#2.Write a program for a Single line comment and multi-line comments

# This is a single line comment. 
"""
This is Python assignment on basics.
Python has Multi-line comments.
"""

#3.Define variables for different Data Types int, Boolean, char, float, double and print on the
Console
# Defining variables of different data types
#Python does not have double and char data types
integer_var = 10                 
boolean_var = False             
string_var = 'Python'                
float_var = 10.5                 

# Printing the variables to the console
print("Integer:", integer_var)
print("Boolean:", boolean_var)
print("String :", string_var)
print("Float:", float_var)


#4.Define the local and Global variables with the same name and print both variables and
understand the scope of the variables
name='Global Variable'
def variable_s():
    name = "Local Variable"
    print("Inside the function:  ", name)
variable_s()
print("Outside the function: ", name)
