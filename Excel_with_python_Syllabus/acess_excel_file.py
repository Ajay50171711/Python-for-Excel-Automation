# method 1: using os
#code 1
# import os

# folder = "reports"

# files = os.listdir(folder)

# for file in files:
#     if file.endswith(".xlsx"):
#         print(file)


# method 2: using pathlib
#code 2
# from pathlib import Path

# folder = Path("reports")

# for file in folder.glob("*.xlsx"):
#     print(file)

#code 3
# def process_file(filename):
#     try:
#         print(f"Processing {filename}")
#     except Exception as e:
#         print("Error:", e)

# process_file("sales.xlsx")



#code 4
# from openpyxl import Workbook

# wb = Workbook()
# ws = wb.active

# ws['A1'] = "Name"
# ws['B1'] = "Salary"

# ws['A2'] = "John"
# ws['B2'] = 50000

# wb.save("employee.xlsx")

#code 5
import pandas as pd
import os

file_path = "reports/sales_feb.xlsx"

if os.path.exists(file_path):
    df = pd.read_excel(file_path)
    print(df.head())
    print("\n\n")
else:
    print("File not found:", file_path)

#code 6
high_sales = df[df["Amount_INR"] > 10000]

print(high_sales)

#code 7
# df.groupby("Region")["Sales"].sum()  #apne data me naahi region ha na hi multiple city hai show that we have to generate a data which contain reqire data


