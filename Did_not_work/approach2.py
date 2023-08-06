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


        # class RentalProperty:
        #     def __init__(self):
        #         self.rental_income = 0
        #         self.additional_income = 0

        #     def get_monthly_income(self):
        #         self.rental_income = float(input("Enter the monthly rental income: "))
        #         self.additional_income = float(input("Enter any additional monthly income (e.g., laundry, parking): "))

        #     def calculate_monthly_income(self):
        #         return self.rental_income + self.additional_income



        #         self.expenses = {}

        #     def get_monthly_expenses(self):
        #     pass

        #     def calculate_monthly_expenses(self):
        #         return sum(self.expenses.values())


        #     def calculate_monthly_cash_flow(self):
        #         total_income = self.calculate_monthly_income()
        #         total_expenses = self.calculate_monthly_expenses()
        #         return total_income - total_expenses


        #         pass
        #         self.down_payment = 0
        #         self.rehab_budget = 0
        #         self.misc_budget = 0

        #     def get_investment(self):
        #         pass

        #     def calculate_total_investment(self):
        #         return self.calculate_initial_investment()

        #     def calculate_annual_cash_flow(self):
        #         return self.calculate_monthly_cash_flow() * 12

        #     def calculate_cash_on_cash_roi(self):
        #         annual_cash_flow = self.calculate_annual_cash_flow()
        #         total_investment = self.calculate_total_investment()

        #         if total_investment == 0:
        #             return 0

        #         coc_roi = (annual_cash_flow / total_investment) * 100
        #         return coc_roi



        # property1 = RentalProperty()


        # monthly_cash_flow = property1.calculate_monthly_cash_flow()
        # coc_roi = property1.calculate_cash_on_cash_roi()

        # print(f"Total Monthly Cash Flow: ${monthly_cash_flow}")
        # print(f"Cash on Cash ROI: {coc_roi}")



# monthly_cash_flow = property1.calculate_monthly_cash_flow()
#                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "c:\Users\User\Documents\Coding Temple\Theives-126\week-3\OOP-ROI-Calc-Hw\Did_not_work\approach2.py", line 38, in calculate_monthly_cash_flow
#     total_expenses = self.calculate_monthly_expenses()
#                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "c:\Users\User\Documents\Coding Temple\Theives-126\week-3\OOP-ROI-Calc-Hw\Did_not_work\approach2.py", line 31, in calculate_monthly_expenses
#     return sum(self.expenses.values())
#                ^^^^^^^^^^^^^
# AttributeError: 'RentalProperty' object has no attribute 'expenses'
