from openpyxl import Workbook

book = Workbook()
sheet = book.active

sheet['a1'] = 'Welcome'
sheet['b1'] = "OpenPyXL"
sheet['c1'] = 12345

sheet.cell(row=5, column=5).value = "PragimTech"

book.save("Book2.xlsx")

