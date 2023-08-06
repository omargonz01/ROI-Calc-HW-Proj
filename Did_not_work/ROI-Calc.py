# create a class to handle the calculations for Return on Investment (ROI).
# The ROI will be calculated using the formula:

# ROI = (Net Profit / Initial Investment) * 100

# Net Profit = Total Rental Income - Total Expenses
# Initial Investment = Purchase Price + Closing Costs + Renovation Costs
# 
# set defualt values to 0
# set up a dictionary to store the expenses
# find total income
# find total expenses
# find cash flow
# do math for each for each month, then x 12 to get annual

#find total investment - use annual cash flow // total invesment to get cash on cash roi

    # class RentalProperty:
    #     def __init__(self):
    #         self.purchase_price = 0
    #         self.closing_costs = 0
    #         self.renovation_costs = 0
    #         self.rental_income = 0
    #         self.additional_income = 0
    #         self.down_payment = 0
    #         self.rehab_budget = 0
    #         self.misc_budget = 0
    #         self.expenses = {}

    #     def get_user_input(self):
    #         self.purchase_price = float(input("purchase price: "))

    #         self.closing_costs = float(input(" closing costs: "))

    #         self.renovation_costs = float(input(" renovation costs: "))

    #         self.rental_income = float(input(" rental income: "))

    #         self.additional_income = float(input("additional income  "))

    #         self.expenses['tax'] = float(input(" tax expenses: "))
    #         self.expenses['insurance'] = float(input(" insurance expenses: "))
    #         self.expenses['utilities'] = float(input(" utilities expenses: "))
    #         self.expenses['hoa'] = float(input(" HOA expenses: "))
    #         self.expenses['vacancy'] = float(input("vacancy expenses: "))
    #         self.expenses['repairs'] = float(input(" repairs expenses: "))
    #         self.expenses['capital_expenditures'] = float(input("monthly capital expenditures: "))
    #         self.expenses['property_management'] = float(input(" property management : "))
    #         self.expenses['mortgage'] = float(input(" mortgage : "))

    #         self.down_payment = float(input("Enter the down payment amount: "))
    #         self.rehab_budget = float(input("Enter the rehab budget: "))
    #         self.misc_budget = float(input("Enter the miscellaneous budget: "))

    #     def calculate_net_profit(self):
    #         total_income = self.rental_income + self.additional_income
    #         total_expenses = sum(self.expenses.values())
    #         return total_income - total_expenses

    #     def calculate_initial_investment(self):
    #         return self.purchase_price + self.closing_costs + self.renovation_costs + self.down_payment + self.rehab_budget + self.misc_budget

    #     def calculate_roi(self):
    #         net_profit = self.calculate_net_profit()
    #         initial_investment = self.calculate_initial_investment()

    #         if initial_investment == 0:
    #             return 0

    #         roi = (net_profit / initial_investment) * 100
    #         return roi

    #     def calculate_monthly_cash_flow(self):
    #     pass

    #     def calculate_annual_cash_flow(self):
    #         return self.calculate_monthly_cash_flow() * 12

    #     def calculate_cash_on_cash_roi(self):
    #         pass

    #         if  == 0:
    #             return 0

    #         coc_roi = (annual_cash_flow / total_investment) * 100
    #         return coc_roi

    # testproperty = RentalProperty()

    # testproperty.get_user_input()

    # print(testproperty.calculate_roi())


