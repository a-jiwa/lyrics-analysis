import requests
from bs4 import BeautifulSoup
import csv

# Define the list of dictionaries containing text and URL
data_list = [
    {'text': '12/OM', 'link': 'https://uk-drill.com/12-om/'},
    {'text': '12World/12Anti', 'link': 'https://uk-drill.com/12world-12anti/'},
    {'text': '156', 'link': 'https://uk-drill.com/156-2/'},
    {'text': '7th WoodGrange x BWC Gang Profile', 'link': 'https://uk-drill.com/7th-gang-profile/'},
    {'text': '9iners', 'link': 'https://uk-drill.com/9iners/'},
    {'text': '9th Street', 'link': 'https://uk-drill.com/9th-street/'},
    {'text': 'ACG/6th', 'link': 'https://uk-drill.com/acg-6th/'},
    {'text': 'Active Gang', 'link': 'https://uk-drill.com/active-gang/'},
    {'text': 'Archive', 'link': 'https://uk-drill.com/archive/'},
    {'text': 'AY/Aylesbury Estate', 'link': 'https://uk-drill.com/ay-aylesbury-estate/'},
    {'text': 'B-Side', 'link': 'https://uk-drill.com/b-side/'},
    {'text': 'Block 6', 'link': 'https://uk-drill.com/block-6/'},
    {'text': 'Browning17', 'link': 'https://uk-drill.com/browning17/'},
    {'text': 'CGE', 'link': 'https://uk-drill.com/cge/'},
    {'text': 'Church Road', 'link': 'https://uk-drill.com/church-road/'},
    {'text': 'Contact us / Disclaimer', 'link': 'https://uk-drill.com/contact-us/'},
    {'text': 'Cumbo', 'link': 'https://uk-drill.com/cumbo/'},
    {'text': 'Custom House', 'link': 'https://uk-drill.com/custom-house/'},
    {'text': 'Deep', 'link': 'https://uk-drill.com/deep/'},
    {'text': 'Eas Reuploads', 'link': 'https://uk-drill.com/eas-reuploads/'},
    {'text': 'East', 'link': 'https://uk-drill.com/east/'},
    {'text': 'Editorials', 'link': 'https://uk-drill.com/uk-drill-editorial-articles-blog/'},
    {'text': 'Gangs', 'link': 'https://uk-drill.com/gangs/'},
    {'text': 'CB (Crazy Blackz, Blackz) 7th', 'link': 'https://uk-drill.com/gangs/cb-7th/'},
    {'text': 'Digga D', 'link': 'https://uk-drill.com/gangs/digga-d/'},
    {'text': 'East', 'link': 'https://uk-drill.com/gangs/east/'},
    {'text': 'LD/SCRIBZ 67', 'link': 'https://uk-drill.com/gangs/trizzac/'},
    {'text': 'Mizormac Harlem Spartans', 'link': 'https://uk-drill.com/gangs/yanko/'},
    {'text': 'North', 'link': 'https://uk-drill.com/gangs/north/'},
    {'text': '3×3 Gang', 'link': 'https://uk-drill.com/gangs/north/3x3/'},
    {'text': 'PS ZONE II', 'link': 'https://uk-drill.com/gangs/hitman-x-da/'},
    {'text': 'SJ OFB', 'link': 'https://uk-drill.com/gangs/burner/'},
    {'text': 'South', 'link': 'https://uk-drill.com/gangs/south/'},
    {'text': 'West', 'link': 'https://uk-drill.com/gangs/west/'},
    {'text': 'GB – Rhyheim Barton', 'link': 'https://uk-drill.com/gb-rhyheim-barton/'},
    {'text': 'Glossary', 'link': 'https://uk-drill.com/glossary/'},
    {'text': 'Harlem Spartans', 'link': 'https://uk-drill.com/harlem-spartans/'},
    {'text': 'History of Gangs', 'link': 'https://uk-drill.com/history-of-gangs/'},
    {'text': 'Home', 'link': 'https://uk-drill.com/'},
    {'text': 'HRB', 'link': 'https://uk-drill.com/hrb/'},
    {'text': 'Kuku', 'link': 'https://uk-drill.com/kuku/'},
    {'text': 'Lil Zac', 'link': 'https://uk-drill.com/lil-zac/'},
    {'text': 'Mali Strip', 'link': 'https://uk-drill.com/mali-strip/'},
    {'text': 'Moscow 17', 'link': 'https://uk-drill.com/moscow-17/'},
    {'text': 'N15', 'link': 'https://uk-drill.com/n15/'},
    {'text': 'Negus', 'link': 'https://uk-drill.com/negus/'},
    {'text': 'Nesha', 'link': 'https://uk-drill.com/nesha/'},
    {'text': 'New Music', 'link': 'https://uk-drill.com/new-music/'},
    {'text': 'North', 'link': 'https://uk-drill.com/north/'},
    {'text': 'north', 'link': 'https://uk-drill.com/north-2/'},
    {'text': 'North Reuploads', 'link': 'https://uk-drill.com/north-reuploads/'},
    {'text': 'North West', 'link': 'https://uk-drill.com/nw/'},
    {'text': 'North West Reuploads', 'link': 'https://uk-drill.com/north-west-reuploads/'},
    {'text': 'NPK/Northumberland Park Kids', 'link': 'https://uk-drill.com/npk-northumberland-park-kids/'},
    {'text': 'OMH/Manor House', 'link': 'https://uk-drill.com/omh-manor-house/'},
    {'text': 'Original 3rd', 'link': 'https://uk-drill.com/original-3rd/'},
    {'text': 'Peckwater', 'link': 'https://uk-drill.com/peckwater/'},
    {'text': 'Perry', 'link': 'https://uk-drill.com/perry/'},
    {'text': 'Rayners Lane', 'link': 'https://uk-drill.com/rayners-lane/'},
    {'text': 'Rude Drill Songs', 'link': 'https://uk-drill.com/rude-drill-songs/'},
]

# Create a CSV file to store the scraped data
csv_filename = "scraped_data.csv"

# Initialize the CSV file with headers
csv_headers = ["Text", "Scraped Text"]
with open(csv_filename, mode="w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(csv_headers)

    # Iterate through each dictionary in the data list
    for data_dict in data_list:
        text = data_dict["text"]
        url = data_dict["link"]

        try:
            # Send an HTTP GET request to the URL
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors

            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")

            # Find the relevant HTML element(s) and extract text
            scraped_text = ""
            paragraphs = soup.find_all("p", class_="has-black-color has-text-color")
            for paragraph in paragraphs:
                scraped_text += paragraph.get_text() + "\n"

            # Write the scraped data to the CSV file
            csv_writer.writerow([text, scraped_text.strip()])

            print(f"Scraped data from {url}")

        except Exception as e:
            print(f"Error while scraping {url}: {str(e)}")

print("Scraping completed. Data saved to", csv_filename)
