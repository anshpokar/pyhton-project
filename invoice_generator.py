from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4

from reportlab.lib.styles import getSampleStyleSheet
import datetime
from datetime import date
quantity = int(input("Enter the total courses: "))
products = []
prices = []
subscriptions = []

for i in range(quantity):
    product = input("Enter the name of the Course: ")
    price = int(input("Enter the price of Course: "))
    subscription = input("Enter the tenure of Course: ")
    products.append(product)
    prices.append(price)
    subscriptions.append(subscription)
    print("-------------------------------------------------------------")

total_cost = sum(prices)
print("Total = ",total_cost)
discount = int(input("Enter Discount: "))
x=(discount/100)*total_cost
# print(x)
total_cost_after_discount = total_cost-x
print("Total cost after discount = ",total_cost_after_discount)

DATA = [
    ["No.", "Date", "Name", "Subscription", "Price (Rs.)"],
    *[
        [i+1, date.today(), products[i], subscriptions[i], prices[i]]
        for i in range(quantity)
    ],
    ["Sub Total", "", "", "", total_cost],
    ["Discount", "", "", "", discount],
    ["Total", "", "", "", total_cost_after_discount]
]

pdf = SimpleDocTemplate("receipt.pdf", pagesize=A4)

styles = getSampleStyleSheet()

title_style = styles["Heading1"]
title_style.alignment = 1

title = Paragraph("Quastech", title_style)

style = TableStyle(
    [
        ("BOX", (0, 0), (-1, -1), 1, colors.black),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("BACKGROUND", (0, 0), (4, 0), colors.gray),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
    ]
)

table = Table(DATA, style=style)

pdf.build([title, table])

print("Your invoice is ready")