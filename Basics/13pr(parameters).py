#parameters
'''def Greet_user(name ,last_name,registration ,email):
    print("Hello! I'm your assistant. I'll be happy to help you with any questions")
    print(f' Hello {name, last_name}!')
    print(f'Your registration no. is {registration}')
    print("Welcome")
    
    
print(">>>>>>>>>>>>>>>>>>")
Greet_user("Rajas"," Lambe "," 1122334455 "," abcdef@gmail.com")
print("<<<<<<<<<<<<<<<<<<")    
'''

# Keyword argument

def __user__(f_name,l_name,email):
    print(f"Hello, a user with name {f_name}{l_name} and email {email} has been registered ")
    return f'Hello {f_name} {l_name} your email is {email}'
# Test the function
print(__user__("John","Doe","john@example.com"))



