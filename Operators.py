#1.Write a function for arithmetic operators(+,-,*,/)
def arithmetic_func(a,b):
    print("Add:",a+b)
    print(f'subtract:',a-b)
    print('Multiple:',a*b)
    print('Divide: ',a/b)
arithmetic_func(6,2)

#2.Write a method for increment and decrement operators(++, --)
def inc_dec(num):
    num=10
    #incrementing
    num+=1
    print("Incremented Value :",num)
    #decrementing
    num-=1
    print("Decremented Value :",num)
inc_dec(num)

#3Write a program to find the two numbers equal or not
a = int(input())
b = int(input())
if a == b:
    print("Equal")
else:
    print("Not Equal")

#4.Program for relational operators (<,<==, >, >==)
a = 10
b = 20
# Using relational operators
print("a < b:", a < b)    
print("a <= b:", a <= b)  
print("a > b:", a > b)    
print("a >= b:", a >= b)  

##5.Print the smaller and larger number
m = int(input())
n = int(input())
if a < b:
    smaller, larger = m, n
else:
    smaller, larger = n, m
print("Smaller number:", smaller)
print("Larger number:", larger)
