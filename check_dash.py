import pandas as pd

def check_entries_end_with_dash(file_path):
    # Read the XLSX file into a pandas DataFrame
    df = pd.read_excel(file_path)

    # Get the entries from the third column (index 2) and check if they end with a dash
    invalid_entries = df.loc[~df.iloc[:, 2].str.endswith('-'), df.columns[2]]
    return invalid_entries

if __name__ == "__main__":
    # Replace 'your_file.xlsx' with the actual file path
    file_path = "C:\\Users\\ediamond\\OneDrive - Capgemini\\Desktop\\test_ecs_check.xlsx"
    invalid_entries = check_entries_end_with_dash(file_path)

    if not invalid_entries.empty:
        print("Invalid entries in the third column (column index 2) that do not end with a dash:")
        print(invalid_entries)
    else:
        print("All entries in the third column end with a dash.")
