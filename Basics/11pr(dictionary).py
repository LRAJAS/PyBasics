# Dictionary ''{ }''
customer = {
    "name": "rajas l",
    "age" : "20",
    "gender" : "male ",
    "birthdate":"1 jan 2000"}
print(customer.get("name"))
print(customer.get("birthdate"))

#task 
phone_no = input('contact no.' )
digits_mapping ={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight" }
output=""
for ch in phone_no :
    output += digits_mapping.get(ch,"!") + " "
print(output)
