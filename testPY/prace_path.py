import openpyxl as xl
wb = xl.load_workbook('luoquan.xlsx')
sheet = wb['sheet1']
cell = sheet.cell(1, 1)
print(cell.value)