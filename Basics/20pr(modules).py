# modules 

def display_clock(hour):
    """
    Displays the time in a 12-hour format.
    """
    hour %= 12 
    if hour == 0:
        hour = 12  # Convert 0 to 12 
    print(f"The time is {hour} o'clock.")

# Test 
display_clock(8)  
display_clock(15)  
display_clock(0)  




import arithmetic_operations

# input 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result = arithmetic_operations.add(num1, num2)
difference_result = arithmetic_operations.subtract(num1, num2)
product_result = arithmetic_operations.multiply(num1, num2)
division_result = arithmetic_operations.divide(num1, num2)

print(sum_result)
print(difference_result)
print(product_result)
print(division_result)