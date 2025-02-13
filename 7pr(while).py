# whle loop
i = 1
while i<= 20:
    print('*' * i)
    i= 1+i
print('done')    


# buildng a guessing game using while loop

secret_code =7
guess_count = 0
guess_limit = 5
while guess_count < guess_limit:
    guess = int(input("guess the number :"))
    guess_count += 1
    if guess == secret_code:
        print("you on the game ")
        break 
else :
    print("sorry you failed , chances are over bro")    
    
