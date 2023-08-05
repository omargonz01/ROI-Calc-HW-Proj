

class RentalProperty:
    def __init__(self):
        self.rental_income = 0
        self.additional_income = 0

    def get_monthly_income(self):
        self.rental_income = float(input("Enter the monthly rental income: "))
        self.additional_income = float(input("Enter any additional monthly income (e.g., laundry, parking): "))

    def calculate_monthly_income(self):
        return self.rental_income + self.additional_income



        self.expenses = {}

    def get_monthly_expenses(self):
        self.expenses['tax'] = float(input("Enter monthly tax expenses: "))
        self.expenses['insurance'] = float(input("Enter monthly insurance expenses: "))
        self.expenses['utilities'] = float(input("Enter monthly utilities expenses: "))
        self.expenses['hoa'] = float(input("Enter monthly HOA expenses: "))
        self.expenses['vacancy'] = float(input("Enter monthly vacancy expenses: "))
        self.expenses['repairs'] = float(input("Enter monthly repairs expenses: "))
        self.expenses['capital_expenditures'] = float(input("Enter monthly capital expenditures expenses: "))
        self.expenses['property_management'] = float(input("Enter monthly property management expenses: "))
        self.expenses['mortgage'] = float(input("Enter monthly mortgage expenses: "))

    def calculate_monthly_expenses(self):
        return sum(self.expenses.values())




    def calculate_monthly_cash_flow(self):
        total_income = self.calculate_monthly_income()
        total_expenses = self.calculate_monthly_expenses()
        return total_income - total_expenses


        pass
        self.down_payment = 0
        self.rehab_budget = 0
        self.misc_budget = 0

    def get_investment(self):
        self.down_payment = float(input("Enter the down payment amount: "))
        self.closing_costs = float(input("Enter the closing costs: "))
        self.rehab_budget = float(input("Enter the rehab budget: "))
        self.misc_budget = float(input("Enter the miscellaneous budget: "))

    def calculate_total_investment(self):
        return self.calculate_initial_investment()

    def calculate_annual_cash_flow(self):
        return self.calculate_monthly_cash_flow() * 12

    def calculate_cash_on_cash_roi(self):
        annual_cash_flow = self.calculate_annual_cash_flow()
        total_investment = self.calculate_total_investment()

        if total_investment == 0:
            return 0

        coc_roi = (annual_cash_flow / total_investment) * 100
        return coc_roi



property1 = RentalProperty()
property1.get_monthly_income()
property1.get_monthly_expenses()
property1.get_investment()

monthly_cash_flow = property1.calculate_monthly_cash_flow()
coc_roi = property1.calculate_cash_on_cash_roi()

print(f"Total Monthly Cash Flow: ${monthly_cash_flow}")
print(f"Cash on Cash ROI: {coc_roi}")
