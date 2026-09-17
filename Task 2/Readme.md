# 📂 File Organizer and Data Parser

 A 🐍 Python automation script that organizes files from an input directory into extension-based folders, extracts 📧 email addresses and 🧾 transaction IDs from text files, and generates a master 📊 CSV log.

 ## ✨ Features

 - 📋 Copies files from `unorganized_data` without modifying the originals.
- 📁 Automatically organizes files by file extension.
- 📦 Places files without an extension into an `other` folder.
- 🔎 Scans `.txt` files for:
  - 📧 Email addresses
  - 🧾 Transaction IDs in the format `TX12345`
- ♻️ Removes duplicate extracted values within each file.
- 📊 Creates a `master_log.csv` containing all extracted data.
- 🛡️ Handles text files using UTF-8 encoding while ignoring invalid characters.

 ## 📁 Project Structure

 After running the script, the project will look similar to:

```
Task 3/
├── 🐍 organize.py
├── 📂 unorganized_data/
│   ├── 📄 sample_log_1.txt
│   ├── 📕 user_report.txt
│   └── 🖼️ logo.png
│
└── 📂 organized_output/
    ├── 📂 txt/
    │   └── 📄 sample_log_1.txt
    │   └── 📕 user_report.txt
    ├── 📂 png/
    │   └── 🖼️ logo.png
    └── 📊 master_log.csv
```

 ## 🛠️ Requirements

 - 🐍 Python 3.7 or newer
- 📦 No external Python packages are required.

 The script uses only Python standard-library modules:

```
import os
import shutil
import re
import csv
from pathlib import Path
```

 ## 🚀 Setup

 1. 📁 Create a folder for the project.
2. 🐍 Save the Python script inside the project folder.
3. 📂 Create an `unorganized_data` folder.
4. 📄 Place the files you want to process inside `unorganized_data`.

 Example:

```
Task 3/
├── 🐍 main.py
└── 📂 unorganized_data/
    ├── 📄 sample_log_1.txt
    ├── 📄 user_report.txt
    └── 📕 logo.png
```

 ## ▶️ Running the Script

 Open a terminal in the project directory and run:

```
python organize.py
```

 The script automatically determines its own directory, so the input and output paths are:

```
📂 unorganized_data/
📂 organized_output/
```

 🛡️ The original files remain untouched because the script **copies** files rather than moving them.

 ## ⚙️ How It Works

 ### 1️⃣ File Organization

 Each file is copied into a folder based on its extension.

 For example:

```
📷 logo.png   → 📂 organized_output/png/logo.png
📕 user_report.txt  → 📂 organized_output/txt/user_report.txt
```

 Files without an extension are placed in:

```
📂 organized_output/other/
```

 The existing `master_log.csv` in the input directory is intentionally skipped.

 ### 2️⃣ 🔎 Data Extraction

 The script searches all `.txt` files inside `organized_output`.

 It uses regular expressions to find 📧 email addresses:

```
example@example.com
john.doe@example.org
```

 It also searches for 🧾 transaction IDs beginning with `TX` followed by one or more numbers:

```
TX12345
TX987654
```

 ♻️ Duplicate emails and transaction IDs found within the same file are removed.

 ### 3️⃣ 📊 Master CSV

 The extracted information is saved to:

```
📊 organized_output/master_log.csv
```

 The CSV contains three columns:

 | 📄 Filename | 🔖 Data Type | 🔎 Extracted Value |
| --- | --- | --- |
| customers.txt | 📧 Email | user@example.com |
| transactions.txt | 🧾 Transaction ID | TX12345 |

## ⚠️ Important Notes

 - 📋 The script **copies** files, so the source directory is not modified.
- 🔄 Running the script again can overwrite files with the same names in the output folders.
- 📄 Only `.txt` files are scanned for emails and transaction IDs.
- 🧾 Transaction IDs must match the pattern `TX` followed by digits.
- 📊 The generated `master_log.csv` is stored in the output directory.

 ## 🛡️ Error Handling

 If a text file cannot be read, the script prints an error message and continues processing the remaining files.

 Example:

```
⚠️ Error reading example.txt: ...
```

 ## 🎯 Purpose

 This project is useful for:

 - 📂 Automatic file organization
- 🔎 Extracting structured information from text files
- 📧 Finding email addresses
- 🧾 Finding transaction IDs
- 📊 Generating a centralized CSV report
- 🤖 Basic file-processing automation
