def main():

    incomes = []
    number_of_months = int(input("How many months? "))
# user enters number of months they want to calculate.
    for month in range(1, number_of_months + 1):
        income = float(
            input("Enter income for month {}: ".format(month)))
        incomes.append(income)
# user can input the amount for each month
    print_report(incomes)


def print_report(incomes):

    print("\nIncome Report\n-----------")
    total = 0
    for month, income in enumerate(incomes):
        total += income
        # totals the amounts for each month.
        print("Month {:2} - Income: ${:10.2f} \
        Total: ${:10.2f}".format(month + 1, income, total))

# to test this, i used 5 moths and the amount for each month was 1000, 1500, 900, 1100, 1000.
# total was 5500

main()