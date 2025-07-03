# Reusable Function 
def emoji_convertor(message):
    words = message.split(" ")
    emojis = {
        ":)": "😊",
        ":(": "☹️",
        "<3": "❤️",
        }
    output=''
    for word in words :
        output += emojis.get(word,word) + ''    
        

message = input(">")
emoji_convertor(message)
print(emoji_convertor(message))
