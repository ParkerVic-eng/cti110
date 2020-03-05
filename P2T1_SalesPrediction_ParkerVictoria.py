# This project will display the profit made from total sales.
# 2/20/2020
# CTI-110 P2T1 - Sales Prediction
# Victoria Parker
#
#Sales Prediction #2

sales=float(input("Please enter the amount of total sales"))
profitMargin=0.23
totalProfit=sales*profitMargin
print("Your total profit from sales is",format(totalProfit,',.2f'),".",sep='')

