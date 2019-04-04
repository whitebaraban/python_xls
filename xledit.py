import xlrd
import xlwt
import openpyxl

# opening file 
# file = xlrd.open_workbook('file.xls', formatting_info=True)

file = openpyxl.load_workbook(filename = 'file.xlsx')

# picking a sheet
#sheet = file.sheet_by_index(0)

sheet = file['Лист1']

# get value of first cell
#val = sheet.row_values(0)[0]

val = sheet['A1'].value

print(val)
