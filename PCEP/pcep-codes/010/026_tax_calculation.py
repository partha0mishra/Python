income=float(input("Enter the annual income:"))
tax = 0.0
lower_limit = 85528
tax_relief = 556.02
lower_tax_rate = 0.18
higher_tax_rate = 0.32
higher_tax_base_amount = 14839.02

if income > lower_limit:
    tax = higher_tax_base_amount + higher_tax_rate*(income - lower_limit)
else: # No returning money
    tax = max(lower_tax_rate*income - tax_relief,0.0)

tax = round(tax, 0)
print("The tax is:", tax, "thalers")

# Test Cases
# input: 10,000, output: 1,244.0
# input: 100,000 output: 19,470.0
# input: 1,000   output: 0.0
# input: -100    output: 0.0