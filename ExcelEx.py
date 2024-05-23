from openpyxl import Workbook  
import time  
  
wb = Workbook()  
sheet = wb.active  
  
sheet['A1'] = 21  
sheet['A2'] = "sandeep"  
sheet['A3'] = 31.75  
sheet['A4'] = 56  
sheet['B1'] = True
  
now = time.strftime("%x")  
sheet['A5'] = now  
  
wb.save("Excelfile.xlsx")  