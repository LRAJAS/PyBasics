#if else statement
price = input('enter the price ')

if int(price) > 100:
 print("price is greater than 100")

if int(price) == 100:
  print("price is 100")
  
if int(price) < 100:
   print("price is less than 100")
   
   
   #else statement
   price = 50

if int(price) >= 100:
    print("price is greater than 100")
else:
    print("price is less than 100")
    
    
 # if , elif , else statement 
 
 
quantity = 5
amount = price*quantity

if int(amount) > 100:
    if int(amount) > 500:
      print("Amount is greater than 500")
    else:
      if int(amount) <= 500 and amount >= 400:
        print("Amount is between 400 and 500")
      elif int(amount) <= 400 and amount >= 300:
        print("Amount is between 300 and 400")
      else:
        print("Amount is between 200 and 300")
elif int(amount) == 100:
    print("Amount is 100")
else:
    print("Amount is less than 100")
   

   