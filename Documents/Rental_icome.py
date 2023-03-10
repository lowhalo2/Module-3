def enterNumber(string):
    while True:
        try:
            responce = int(input(string))
            return responce
        except:
            print('Please enter a number.')

print('\nWelcome to the Bigger Pockets investment calculator.')

# Income
print('Lets start off with rental properties estimated income.')
income = enterNumber('What is the estimated monthly rental income? ')

# Expenses
print("\nEasy enoug lets move onto the expected expenses of the property.")
tax = enterNumber('What is the estimated monthly tax cost? ')
insurance = enterNumber('What is the estimated monthly insurance cost? ')
utilities = enterNumber('What is the estimated monthly combined utilities cost? ')
hoa = enterNumber('What is the estimated monthly hoa fees if none enter 0. ')
lawn_care = enterNumber('What is the estimated monthly lawn care cost? ')
vacancy = enterNumber('Do you plan to put away a monthly sum in case of vacancies if so how much and if no enter 0. ')
repairs = enterNumber('What is the estimated monthly repair cost? ')
capex = enterNumber('What is the estimated monthly capital expenditures cost? ')
managment = enterNumber('What is the estimated monthly protpery managment cost? ')
mortgage = enterNumber('What is the estimated monthly mortgage cost? ')
expenses = tax + insurance + utilities + hoa + lawn_care + vacancy + repairs + capex + managment + mortgage
print(f"All done your total monthly expenses equate to {expenses}.")

# Cash Flow
cash_flow = income - expenses
print(f'Your monthly cash flow comes to {cash_flow} and annuel to {cash_flow * 12}.')

# Cash on cash return on investment
while True:
    paid = input("Did you take out a mortgage? (yes/no)")
    if paid.lower() == 'yes':
        down_payment = enterNumber('How much did you put down on for the down payment? ')
        break
    elif paid.lower() == 'no':
        break
    else:
        print("Enter yes or no")
closing_cost = enterNumber('How much are closing cost? ')
rehab_budget = enterNumber('What is the expected cost in repairs the property requires? ')
misc_cost = enterNumber('Other unmentioned cost if none enter 0. ')
total_investment = down_payment + closing_cost + rehab_budget + misc_cost
print(f"Your total investment comes out to {total_investment}.")
print(f"Your cash on cash return on investment is {((cash_flow * 12) / total_investment) * 100}%")