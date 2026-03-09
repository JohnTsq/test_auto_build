import pandas as pd

excel_file = pd.ExcelFile('translations.xlsx')

for sheet_name in excel_file.sheet_names:
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    output_csv = f"translations_{sheet_name}.csv"
    df.to_csv(output_csv, index=False, encoding='utf-8-sig')
    print(f"Saved: {output_csv}")