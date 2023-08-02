from flask import Flask, render_template, request

import pandas as pd

app = Flask(__name__)

def check_entries_end_with_dash(file_path):
    # Read the XLSX file into a pandas DataFrame
    df = pd.read_excel(file_path)

    # Get the entries from the third column (index 2) and check if they end with a dash
    invalid_entries = df.loc[~df.iloc[:, 2].str.endswith('-'), df.columns[2]]
    return invalid_entries

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.xlsx'):
            file_path = f"uploads/{file.filename}"
            file.save(file_path)

            invalid_entries = check_entries_end_with_dash(file_path)

            return render_template('results.html', invalid_entries=invalid_entries)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
