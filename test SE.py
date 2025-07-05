def calculate_tax(income, spouse=False, num_children=0, childbirth_expenses=0, num_parents=0, num_disabled=0):
# Deductible expenses
    personal_expense = 60000
spouse_expense = 60000 if spouse else 0
child_expense = num_children * 30000
childbirth_expense = min(childbirth_expenses, 60000) # Max 60,000 Baht
parent_expense = num_parents * 30000 # For parents over 60 years old
disabled_expense = num_disabled * 60000 # For disabled dependents

# Total deductions
total_deductions = (
personal_expense + spouse_expense + child_expense +
childbirth_expense + parent_expense + disabled_expense
)

# Deduct from income
taxable_income = max(0, income - total_deductions) # Taxable income cannot be negative

# Tax brackets
tax_brackets = [
(150000, 0), # 0% for income 0-150,000
(300000, 0.05), # 5% for income 150,001-300,000
(500000, 0.10), # 10% for income 300,001-500,000
(750000, 0.15), # 15% for income 500,001-750,000
(1000000, 0.20), # 20% for income 750,001-1,000,000
(2000000, 0.25), # 25% for income 1,000,001-2,000,000
(5000000, 0.30), # 30% for income 2,000,001-5,000,000
(float('inf'), 0.35) # 35% for income above 5,000,001
]

# Calculate tax
tax = 0
previous_limit = 0

for limit, rate in tax_brackets:
if taxable_income > limit:
tax += (limit - previous_limit) * rate
previous_limit = limit
else:
tax += (taxable_income - previous_limit) * rate
break

return tax

# Example usage
income = 880000 # Annual income in Baht
spouse = True
num_children = 2
childbirth_expenses = 0
num_parents = 2
num_disabled = 0

tax = calculate_tax(
income, spouse, num_children, childbirth_expenses, num_parents, num_disabled
)
print(f"The tax for an income of {income} Baht after deductions is {tax:.2f} Baht.")