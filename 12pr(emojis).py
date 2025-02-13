#emoji use in python
def greet_user():
    print("Welcome to the Emoji Converter!")
    
    
print("Start")
greet_user()


message = input(">")
words = message.split(" ")
emojis = {
    ":)": "😊",
    ":(": "☹️",
    "<3": "❤️",
    }
output=''
for word in words :
    output = emojis.get(word,word) + ''
    print(output)

print("finish")