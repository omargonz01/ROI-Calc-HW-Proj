## create a class to handle the calculations for Return on Investment (ROI)
# create methods for each of the 4 parts since calculations are needed individually before the final solution
# initialize variables 
# set defualt values to 0
# set up a dictionary to store the expenses
# create user input for each of the expenses
# break up into 4 parts: Income, Expenses, Cash Flow, and ROI
# although will need to set up calculations for each so will split up as needed
# find total monthly income - add rental income etc
# find total monthly expenses - add taxes, insurnace, utilities, HOA, vacancy, repairs, capital_expenditures, property_management, and mortgage
# find total monthly cash flow - (income - expenses)
# convert to annual *12
# Initial Investment = Purchase Price + Closing Costs + Renovation Costs add option for other 
# User input for each of the investments made to porperty 
# ROI = (annual cash flow / Initial Investment) * 100 to get into decimal 
# im sure im missing something so lets just start here and go doen the line to see what comes ip 




class RentalProperty:
    
    def __init__(self):
        # list variables we will use
        self.rental_income = 0
        self.additional_income = 0
        self.down_payment = 0
        self.rehab_budget = 0
        self.misc_budget = 0
        self.expenses = {}

    def get_monthly_income(self):
        # takes in user input for  monthly rental_income variable and additional income variable
        self.rental_income = float(input("Enter the monthly rental income: "))

        self.additional_income = float(input("Enter any additional monthly income (e.g., laundry, parking, storage etc.): "))

    def calc_monthly_income(self):
        # does the actual math to get the monthly income
        return self.rental_income + self.additional_income

    def get_monthly_expenses(self):
        # takes in expenses variable and adds them to the empty expense dictionary set up above 
        #@ for each expenses - used float so we can use decimals and convert int to floats as well so that problem got fixed
        self.expenses['tax'] = float(input("Enter monthly tax expenses: "))
        self.expenses['insurance'] = float(input("Enter monthly insurance expenses: "))
        self.expenses['utilities'] = float(input("Enter monthly utilities expenses: "))
        self.expenses['hoa'] = float(input("Enter monthly HOA expenses: "))
        self.expenses['vacancy'] = float(input("Enter monthly vacancy amount to set aside: "))
        self.expenses['repairs'] = float(input("Enter monthly repair amount to set aside: "))
        self.expenses['capital_expenditures'] = float(input("Enter monthly capital expenditures: "))
        self.expenses['property_management'] = float(input("Enter monthly property management expenses: "))
        self.expenses['mortgage'] = float(input("Enter monthly mortgage payment: "))

    def calc_monthly_expenses(self):
        # does the actual math to get the monthly expenses
        # .values() method used for summing up all the values in the dictionary self.expenses quicker
        return sum(self.expenses.values()) 

    def calc_monthly_cash_flow(self):
        # income - expenses using the input users gave 
        # returns the simple math result 
        total_income = self.calc_monthly_income()
        total_expenses = self.calc_monthly_expenses()

        return total_income - total_expenses

    def get_investment(self):
        # takes in user input for the items described in the video 
        # float()
        self.down_payment = float(input("Enter the down payment amount: "))
        self.closing_costs = float(input("Enter the closing costs: "))
        self.rehab_budget = float(input("Enter the rehab budget: "))
        self.misc_budget = float(input("Enter the miscellaneous budget: "))

    def calc_total_investment(self):
        # finds sum of user input for their investment totals
        return self.down_payment + self.closing_costs + self.rehab_budget + self.misc_budget

    def calc_annual_cash_flow(self):
        # multiply the monthly cash flow by 12 - use cash flow not income solved that error
        return self.calc_monthly_cash_flow() * 12

    def calc_cash_on_cash_roi(self):
        # save the methods to a variable so that we can use it to calculate the cash on cash ROI
        # divide annual cash flow by total investment to get the annual cash flow
        # multilply by 100 to convert to % 
        # ***note to self.do not forget to return the result
        annual_cash_flow = self.calc_annual_cash_flow()
        total_investment = self.calc_total_investment()
        coc_roi = (annual_cash_flow / total_investment) * 100

        return coc_roi


# next create instance of the class and call the methods
property1 = RentalProperty()
property1.get_monthly_income()
property1.get_monthly_expenses()
property1.get_investment()

# assigned spcefic methods to variables so I can print at the end to show the user their numbers.
total_annual_cash_flow = property1.calc_annual_cash_flow()
monthly_cash_flow = property1.calc_monthly_cash_flow()
coc_roi = property1.calc_cash_on_cash_roi()

#since we are talking about money - used the :.2f function to format to 2 decimal places

print(f"This Is Your Monthly Cash Flow: ${monthly_cash_flow:.2f}")
print(f"This Is Your Total Annual Cash Flow: ${total_annual_cash_flow:.2f}") 
print(f"This Is Your Cash on Cash ROI: {coc_roi:.2f}%")

    # actually works...
    # i used the numbers that Brandon from Bigger Pockets used to test and make sure everythng worked:

    # Enter the monthly rental income: 2000
    # Enter any additional monthly income (e.g., laundry, parking, storage etc.): 0
    # Enter monthly tax expenses: 150
    # Enter monthly insurance expenses: 100
    # Enter monthly utilities expenses: 0
    # Enter monthly HOA expenses: 0
    # Enter monthly vacancy amount to set aside: 100
    # Enter monthly repair amount to set aside: 100
    # Enter monthly capital expenditures: 100
    # Enter monthly property management expenses: 200
    # Enter monthly mortgage payment: 860
    # Enter the down payment amount: 40000
    # Enter the closing costs: 3000
    # Enter the rehab budget: 7000
    # Enter the miscellaneous budget: 0
    # This Is Your Monthly Cash Flow: $390.00
    # This Is Your Total Annual Cash Flow: $4680.00
    # This Is Your Cash on Cash ROI: 9.36%



#-----------cleaned up version ^^^

#  File "c:\Users\User\Documents\Coding Temple\Theives-126\week-3\OOP-ROI-Calc-Hw\approach3.py", line 79, in <module>
#     coc_roi = property1.calculate_cash_on_cash_roi()
#               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "c:\Users\User\Documents\Coding Temple\Theives-126\week-3\OOP-ROI-Calc-Hw\approach3.py", line 66, in calculate_cash_on_cash_roi
#     total_investment = self.calculate_total_investment()
#                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "c:\Users\User\Documents\Coding Temple\Theives-126\week-3\OOP-ROI-Calc-Hw\approach3.py", line 56, in calculate_total_investment
#     return self.calculate_initial_investment()
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# AttributeError: 'RentalProperty' object has no attribute 'calculate_initial_investment'. Did you mean: 'calculate_total_investment'?



# class RentalProperty:
#   File "c:\Users\User\Documents\Coding Temple\Theives-126\week-3\OOP-ROI-Calc-Hw\approach3.py", line 21, in RentalProperty
#     print(f'The monthly rental income is {self.rental_income}')
#                                           ^^^^
# NameError: name 'self' is not defined
