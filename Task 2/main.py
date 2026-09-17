import os
import shutil
import re
import csv
from pathlib import Path

def organize_and_parse(input_folder, output_folder):
    source = Path(input_folder)
    destination = Path(output_folder)
    
    if not source.exists():
        print(f"Source directory '{input_folder}' does not exist.")
        return

    # Create the different/new output folder if it doesn't exist
    destination.mkdir(parents=True, exist_ok=True)

    # 1. Copy and organize files into extension subdirectories in the DIFFERENT folder
    for file in source.iterdir():
        if file.is_file() and file.name != "master_log.csv":
            ext = file.suffix.lstrip('.') or 'other'
            sub_dir = destination / ext
            sub_dir.mkdir(exist_ok=True)
            
            # Copy files so your original folder stays safe and untouched
            shutil.copy2(str(file), str(sub_dir / file.name))

    # 2. Parse text files from the new folder for emails and transaction IDs using regex
    results = []
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    tx_pattern = r'TX[0-9]+'
    
    for txt_file in destination.rglob('*.txt'):
        try:
            content = txt_file.read_text(encoding='utf-8', errors='ignore')
            
            # Find unique emails and transaction IDs
            emails = set(re.findall(email_pattern, content))
            transactions = set(re.findall(tx_pattern, content))
            
            for email in emails:
                results.append([txt_file.name, 'Email', email])
            for tx in transactions:
                results.append([txt_file.name, 'Transaction ID', tx])
        except Exception as e:
            print(f"Error reading {txt_file.name}: {e}")

    # 3. Save outputs to a master CSV file inside the DIFFERENT folder
    csv_file = destination / 'master_log.csv'
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Filename', 'Data Type', 'Extracted Value'])
        writer.writerows(results)
        
    print(f"Automation complete! Found {len(results)} items and saved them to {csv_file}")

if __name__ == "__main__":
    # Automatically get the script's directory
    script_dir = Path(__file__).parent
    
    # Input folder with raw files
    input_dir = script_dir / "unorganized_data"
    
    # A completely DIFFERENT output folder for sorted files and CSV
    output_dir = script_dir / "organized_output"
    
    organize_and_parse(input_dir, output_dir)
