import random
from openpyxl import Workbook

# Create a new Workbook
wb = Workbook()
# Save it
wb.save(filename="empty_book.xlsx")

# Create a new Sheet
sheet = wb.create_sheet(title="Test Sheet")

# Add Titles
sheet["A1"] = "ID"
sheet["B1"] = "Price"
sheet["C1"] = "Amount"
sheet["D1"] = "Total"

# Add Some Sample Data
for x in range(2, 100): # Header Starts at row 1 so data starts at row 2
    id_cell     = "A%s" % (x)
    price_cell  = "B%s" % (x)
    amount_cell = "C%s" % (x)
    total_cell  = "D%s" % (x)

    # Add the data
    sheet[id_cell] = x # The row number just as an example
    sheet[price_cell] = random.randint(0, 100) #  Random Number between 0 and 100
    sheet[amount_cell] = random.randint(0, 1000) # Random Number between 0 and 1000
    sheet[total_cell] =  "=SUM(%s, %s)" % (price_cell, amount_cell) # The Excel Formula When this runs, it should evaluate to eg SUM(B1, C1)

# Save the Book
wb.save(filename="empty_book.xlsx")

