"""
The program asks user to enter sales amount for each day of the week,
store it in a list and calculate the sum
"""

def main():
    list_sales = sales()
    total_sales(list_sales)

def sales():
    sales_week = []
    while len(sales_week) < 7:
        sales_day = input("Enter amount: ")
        sales_week.append(float(sales_day))
    return sales_week

def total_sales(lst):
    total = 0
    for i in lst:
        total += i
    print(f"Total sales: {total}")
    return total

    main()
    