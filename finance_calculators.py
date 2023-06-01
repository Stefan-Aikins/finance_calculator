import math
#This program will ask the user to choose a calculator which will either calculate investment or bond
#for now I will store the value of the input, awaiting display
#I have added the lower case method to change all input to lower case
#This calculator with switch mode depending on the users's choice. An investment or bond calculator mode
calc_option =input(f'''
        Investment - to calculate the amount of interest you will earn on your investment.
        Bond - to calculate the amount you would have to pay on a home loan.

        Either enter [Investment or Bond] from the Menu above to proceed: 
    ''').lower()
#The calculator is in investment calculation mode
if calc_option == 'investment':
    
    #the value entered will be used to calculate simple and compound interest
    deposit = input('how much money are you depositing?: ')

    #Progran can only proceed if a number is entered and the number of characters is not less than 3 and not greater than 12
    #the isnumeric() function was sourced from w3schools. https://www.w3schools.com/python/ref_string_isnumeric.asp#:~:text=The%20isnumeric()%20method%20returns,%2D9)%2C%20otherwise%20False. 
    #The minimum amount that can be deposited 5 figures and maximum is 12 figues
    if (deposit.isnumeric()) and len(deposit) >= 6 and len(deposit) < 13:
        deposit = int(deposit) #The ca`lculations cannot be done with strings hence why casting
    else:
        while True: 
             #the calculator requires that the user enters the correct figures before the program can proceed
             deposit = input('''minimum of 6 characters is required, Also please type numbers only, type amount here:  
              ''')
             #The calculator will stop asking after ther correct input is entered
             if (deposit.isnumeric() == True) and len(deposit) >= 3 and len(deposit) < 13:
                 int(deposit)
                 break
    #the calculator requires the interest rate to be used for calculating interest on the investment
    interest_rate = input('What interest rate would you prefer?: ')

    # I am validating the interest rate to only accept single digit numbers before the program can proceed
    if (interest_rate .isnumeric()) and (len(interest_rate) == 1):
        #input values are strings so I am casting the value
        interest_rate = int(interest_rate) /100
    else:
        while True:
             #
             interest_rate = input('PLease type numbers only, between 0 - 10: ')
             #the user is allowed enter only a digit as interest rate
             if interest_rate.isnumeric() == True and len(interest_rate) == 1:
                  interest_rate = int(interest_rate) / 100
                  break
             
    #proceed with number of years if only a maximum of 2 digits have been entered by the user
    years = input('How many years do you plan to invest?: ')

    if years.isnumeric() and len(years) == 1 or len(years) == 2:
        years = int(years)
    else:
        while True:
            years = input('Please enter a maximum of 2 characters, only numbers: ')
            if years.isnumeric() and len(years) == 1 or len(years) == 2:
                years = int(years)
                break

    #This program should only proceed to calculate simple or compound interest if the user has typed simple or compound
    # as input.
    type_of_interest = input('Do you want [simple or compound] interest?: ').lower()
    if type_of_interest == 'simple':
        #calculate compound interest using the formular below
        Amount = int(deposit * (1 + interest_rate * years ))
        print(f'You are expected to earn £{Amount} by the end of {years} years which is charged at {int(interest_rate * 100)}% interest rate.')

    elif type_of_interest == 'compound':
            Amount = int(deposit * math.pow((1+interest_rate),years))
            print(f'You are expected to earn £{Amount} by the end of {years} years which is charged at {int(interest_rate * 100)}% interest rate.')
    else:
        while True:
            type_of_interest = input('Required! Please type either [simple or compound]: ?: ').lower()
            if type_of_interest == 'simple':
                Amount = print((deposit * (1 + interest_rate * years )))
                print(f'You are expected to earn £{Amount} by the end of {years} years which is charged at {int(interest_rate * 100)}% interest rate.')
                break
            else:
                if type_of_interest == 'compound':
                    #calculate the coumpound interest on amount deposited sing this formular
                    Amount = int(deposit * math.pow((1+interest_rate),years))
                    print(f'You are expected to earn £{Amount} by the end of {years} years which is charged at {int(interest_rate * 100)}% interest rate.')
                    break

# The program will calaculate the amount to pay on a home loan when bond is entered rather than investment
elif calc_option == 'bond':
    presentValue = input('Please enter a present value of the house: ')
    if (presentValue.isnumeric()) and len(presentValue) >= 6 and len(presentValue) < 13:
        presentValue = int(presentValue) #The ca`lculations cannot be done with strings hence why casting
    else:
        while True: 
             presentValue = input('''minimum of 6 characters is required, Also please type numbers only, type amount here:  
              ''')
             if (presentValue.isnumeric() == True) and len(presentValue) >= 3 and len(presentValue) < 13:
                 presentValue = int(presentValue)
                 break
             
    interest_rate = input('What interest rate would you prefer?: ')

    # I am validating the interest rate to only accept single digit numbers before the program can proceed
    if (interest_rate .isnumeric()) and (len(interest_rate) == 1):
        interest_rate = int(interest_rate)
        interest_rate = (interest_rate/ 100) / 12
        
    else:
        while True:
             interest_rate = input('PLease type numbers only, between 0 - 10: ')
             if interest_rate.isnumeric() == True and len(interest_rate) == 1:
                 interest_rate = int(interest_rate)
                 interest_rate = (interest_rate/ 100) / 12   
                 break
    
    #proceed with number of years if only a maximum of 2 digits have been entered by the user
    months = input('How many months do you plan to invest?: ')

    # The calculator should accept a string which is 
    if months.isnumeric() and len(months) == 2 or len(months) == 3:
        months = int(months)
    else:
        while True:
            months = input('You are only allow to enter 2 or 3 characters. eg. 90 or 120 ')
            if months.isnumeric() and len(months) == 1 or len(months) == 2:
                months = int(months)
                break
                #Calculate bond using this formular from python
    Amount = int((interest_rate * presentValue) / (1 - (1 + interest_rate)**(-months)))
    print(f'You are expected to pay £{Amount} for {months} months at a rate of {float((interest_rate))}% per month.')

else:
    #The program should stall when the user does not enter investment or bond
    print('''
    Sorry!, your input is not recognised: Ensure you have entered [investment or bond] \n 
    PLEASE CLOSE THE APPLICATION then RUN AGAIN, THANK YOU!
    ''')