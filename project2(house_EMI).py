# Constants
r = 0.08 / 12  # Monthly interest rate (assuming 8% annual interest)
n = 48  # Number of months
EMI = 'EMI'

# Input for house budget
house = int(input('Input your house budget (minimum 500000): '))

if house <= 500000:
    print('You have to wait for some more years to get your dream home.')
else:
    pay = input('How would you like to pay for your house (EMI / INSTALMENT / Downpayment / CASH): ').upper()

    if pay == 'EMI':
        emi = house * r * (1 + r)**n / ((1 + r)**n - 1)
        print('Your monthly EMI will be:', emi)
    elif pay == 'INSTALMENT':
        instalment = house / n
        print('Your monthly instalment will be:', instalment)
    elif pay == 'DOWNPAYMENT':
        downpayment = 0.1 * house
        monthly_payment = (house - downpayment) / n
        print('Your downpayment will be:', downpayment)
        print('And your monthly instalment will be:', monthly_payment)
    elif pay == 'CASH':
        print('Congratulations, you have paid for your house in full!')
    else:
        print('Invalid payment option.')

if house >= 2500000:
    print("You can get a 2 BHK in this budget.")
elif house >= 5000000:
    print('You can get a spacious 2BHK or a 3BHK in this budget.')
elif house <= 1000000:
    print("You can get a 1 BHK in this budget.")
