# Exceptions 
try:
    age = int(input('age: '))
    income= 10000
    risk = income / age 
    print(age)
    print(risk)
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Age cannot be zero. Please enter a valid age.")
    