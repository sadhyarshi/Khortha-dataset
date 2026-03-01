import pandas as pd
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

def convert_to_roman(text):
    if not text or pd.isna(text):
        return ""
    # Converts Devanagari to ITRANS format
    return transliterate(str(text), sanscript.DEVANAGARI, sanscript.ITRANS)

def process_dataset():
    file_path = 'data/khortha_parallel.csv'
    
    # Load the data
    df = pd.read_csv(file_path)

    # Clean header names just in case of trailing spaces
    df.columns = df.columns.str.strip()

    # The Logic: Target the exact column names you requested
    # We use .get() to avoid KeyError if a column is missing
    df['Roman (Target)'] = df.apply(
        lambda row: convert_to_roman(row['Devanagari']) 
        if pd.isna(row.get('Roman (Target)')) or str(row.get('Roman (Target)')).strip() == "" 
        else row['Roman (Target)'], 
        axis=1
    )
    
    # Save back to CSV
    df.to_csv(file_path, index=False)
    print("✅ Success! Roman (Target) column updated in data/khortha_parallel.csv")

if __name__ == "__main__":
    process_dataset()