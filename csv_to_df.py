import pandas as pd
import re

# Load the CSV file
file_path = 'scraped_data.csv'
data = pd.read_csv(file_path)

# Function to parse the text into different categories
def parse_text(text):
    # Initialize default values
    parsed_data = {
        'Description': '',
        'Notable Members': '',
        'Allies': '',
        'Opps': ''
    }

    # Split the text into paragraphs
    paragraphs = text.split('\n')

    # Assuming the first paragraph is always the description
    if paragraphs:
        parsed_data['Description'] = paragraphs[0]

    # Find sections for Notable Members, Allies, Opps
    for para in paragraphs:
        if 'Notable Members:' in para:
            parsed_data['Notable Members'] = para.replace('Notable Members:', '').strip()
        elif 'Allies:' in para:
            parsed_data['Allies'] = para.replace('Allies:', '').strip()
        elif 'Opps:' in para:
            parsed_data['Opps'] = para.replace('Opps:', '').strip()

    return parsed_data

# Apply parsing to the non-null entries
parsed_entries = data['Scraped Text'].dropna().apply(parse_text)
parsed_df = pd.DataFrame(parsed_entries.tolist())

# Combine the 'Name' column from the original data with the parsed data
parsed_df['Name'] = data['Text']

# Display the first few rows of the newly structured dataframe
print(parsed_df)
