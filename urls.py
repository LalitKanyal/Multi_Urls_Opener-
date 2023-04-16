import openpyxl
import webbrowser

# Open the Excel file and select the active worksheet
workbook = openpyxl.load_workbook('./sheet.xlsx')
worksheet = workbook.active

# Iterate over the rows in the worksheet and open each URL in a web browser
for row in worksheet.iter_rows(values_only=True):
    url = row[0]
    webbrowser.open_new_tab(url)
