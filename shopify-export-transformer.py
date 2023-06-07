import csv
import os
import pandas as pd

file_format = "csv" # or "xlsx"

def parse_csv(input_file, output_file, file_format="csv"):
    rows = []
    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            new_row = []
            for cell in row:
                # remove linebreaks within a cell
                cleaned_cell = cell.replace('\n', '').replace('\r', '')
                # replace double quotes within a cell
                cleaned_cell = cleaned_cell.replace('""', '"')
                new_row.append(cleaned_cell)
            rows.append(new_row)

    df = pd.DataFrame(rows)

    if file_format.lower() == "csv":
        df.to_csv(output_file, index=False, header=False)
    elif file_format.lower() == "xlsx":
        df.to_excel(output_file, index=False, header=False, engine='openpyxl')
    else:
        print(f"Unsupported output file format: {file_format}")
        return

input_dir = 'input/'
output_dir = 'output/'

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

print(f"Converting files from {input_dir} to {output_dir}")

# Loop over all files in the input directory
for filename in os.listdir(input_dir):
    # Skip files that aren't CSVs
    if not filename.endswith('.csv'):
        continue

    # Construct full file paths
    input_file = os.path.join(input_dir, filename)
    output_file = os.path.join(output_dir, filename)

    # Change the extension to the desired output format
    output_file = os.path.splitext(output_file)[0] + '.' + 'xlsx'

    parse_csv(input_file, output_file, 'xlsx')


print("Done!")