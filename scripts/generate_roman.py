import pandas as pd
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

def convert_to_roman(text):

    return transliterate(text, sanscript.DEVANAGARI, sanscript.ITRANS)

def process_dataset():
    file_path = 'data/khortha_parallel.csv'
    df = pd.read_csv(file_path)
    
    # Only fill Roman if it's currently empty
    df['roman'] = df.apply(
        lambda row: convert_to_roman(row['devanagari']) if pd.isna(row['roman']) else row['roman'], 
        axis=1
    )
    
    df.to_csv(file_path, index=False)
    print("Transliteration complete!")

if __name__ == "__main__":
    process_dataset()