### Day 76 — Reading CSV and Excel Files

# Overview

Learned how to read, explore, and export CSV and Excel files using Pandas.

# Topics Covered

- Reading CSV files using "pd.read_csv()"
- Reading Excel files using "pd.read_excel()"
- Understanding relative and absolute file paths
- Using "pathlib" for file management
- Reading specific rows with "nrows"
- Selecting columns using "usecols"
- Setting an index using "index_col"
- Understanding "header=0" and "header=None"
- Skipping rows using "skiprows"
- Reading files with different separators using "sep"
- Reading specific Excel sheets using "sheet_name"
- Exporting DataFrames using "to_csv()" and "to_excel()"
- Understanding "index=False"
- Reading exported files back into Pandas

# Practical Work

- Loaded student records from a CSV file.
- Explored DataFrame shape, data types, and rows.
- Read selected rows and columns.
- Worked with semicolon-separated CSV files.
- Exported CSV data into Excel format.
- Loaded exported Excel and CSV files back into DataFrames.

# Important Functions

Function| Purpose
"pd.read_csv()"| Read CSV files
"pd.read_excel()"| Read Excel files
"df.to_csv()"| Export DataFrame to CSV
"df.to_excel()"| Export DataFrame to Excel
"df.head()"| Display first rows
"df.info()"| Display DataFrame information

# Key Learning

Understood how Pandas works with external data files and how to import and export datasets for data analysis.

Status: Completed ✅