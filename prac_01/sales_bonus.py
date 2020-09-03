"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter sales: $"))
if sales >= 1000:
    print(sales * 0.15)
    print("GOOD JOB")
if sales < 1000:
    print(sales * 0.10)
    print("Try Harder Next Time")


