#Problem Statement: Write a Python program that will do:
#Handles invalid input (non-numbers, wrong format).
#Performs basic calculations (addition, subtraction, division, etc.). Offers optional hard calculations
#(exponentiation, modulus,etc.). Presents results clearly for both basic and hard calculations (if
#chosen).

# Taking input
num1 = float(input('Enter first number: ')) 
num2 = float(input('Enter second number: '))
# Addition8
sum = num1 + num2 # Subtraction
min = num1 - num2 # Multiplication
mul = num1 * num2 #Division
div = num1 / num2 #Modulus
mod = num1 % num2 #Exponentiation
exp = num1 ** num2 # Floor Division
floordiv = num1 // num2
print('The sum of the numbers is: ',sum) 
print('The difference of the numbers is: ',min)
print('The multiplication of the numbers is: ',mul) 
print('The division of the numbers is: ',div)
print('The modulus of the numbers is: ',mod)
print('The exponentiation result of the numbers is: ',exp) 
print('The floor division of the numbers is: ',floordiv)
