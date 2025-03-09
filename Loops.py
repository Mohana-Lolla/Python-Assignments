#1. Write a program to print "Bright IT Career" ten times using for loop 
for count in range(10):
    print("Bright IT Career")

#2. Write a program to print 1 to 20 numbers using the while loop. 
num = 1
while num <= 20:
    print(num)
    num += 1

#3. Program to use equal and not equal operators 
val1, val2 = 10, 20
print("val1 == val2", val1 == val2)
print("val1 != val2", val1 != val2)

#4. Write a program to print the odd and even numbers. 
print("Even numbers")
for even_num in range(0, 20, 2):
    print(even_num)

print("Odd numbers")
for odd_num in range(1, 20, 2):
    print(odd_num)

#5. Write a program to print the largest number among three numbers. 
x, y, z = map(int, input("Enter three numbers separated by space: ").split())

if x > y and x > z:
    print("Largest number:", x)
elif y > z:
    print("Largest number:", y)
else:
    print("Largest number:", z)

#6. Write a program to print even numbers between 10 and 20 using while loop 
num_check = 11
while num_check < 20:
    if num_check % 2 == 0:
        print(num_check, end=" ")
    num_check += 1

#7. Write a program to print 1 to 10 using the do-while loop statement. 
index = 1
while True:
    print(index, end=" ")
    index += 1
    if index > 10:
        break

#8. Write a program to check if a number is an Armstrong number or not 
number = int(input("Enter a number: "))
temp = number
armstrong_sum = 0

while temp > 0:
    digit = temp % 10  
    armstrong_sum += digit ** 3  
    temp //= 10 

if armstrong_sum == number:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

#9. Write a program to check if a number is prime or not. 
num_prime = int(input())

if num_prime < 2:
    print(f"{num_prime} is not a prime number")
else:
    is_prime = True
    for divisor in range(2, int(num_prime**0.5) + 1):
        if num_prime % divisor == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f"{num_prime} is a prime number")
    else:
        print(f"{num_prime} is not a prime number")

#10. Write a program to check if a number is a palindrome or not. 
string_input = input()
if string_input == string_input[::-1]:
    print(f"{string_input} is a palindrome")
else:
    print(f"{string_input} is not a palindrome")

#11. Program to check whether a number is EVEN or ODD using switch 
num_switch = int(input("Enter a number: "))

match num_switch % 2:
    case 0:
        print(f"{num_switch} is even")
    case 1:
        print(f"{num_switch} is odd")

#12. Print gender (Male/Female) program according to given M/F using switch
gender_input = input("Enter gender (M/F): ").strip().upper()

match gender_input:
    case 'M':
        print("Male")
    case 'F':
        print("Female")
    case _:
        print("Invalid input")
