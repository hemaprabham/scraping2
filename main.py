import csv
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to extract Twitter profile information
def scrape_twitter_profile(profile_url):
    # Set up Selenium WebDriver (make sure to download the appropriate driver for your browser)
    driver = webdriver.Chrome()
    
    # Open the Twitter profile URL
    driver.get(profile_url)
    
    # Wait for the profile page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='UserDescription']")))
    
    # Extract information using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Extracting Bio, Following Count, Followers Count, Location, Website
    bio = soup.find('div', {'data-testid': 'UserDescription'}).text.strip()
    following_count = soup.find('span', {'data-testid': 'following_count'}).text.strip()
    followers_count = soup.find('span', {'data-testid': 'followers_count'}).text.strip()
    location = soup.find('span', {'data-testid': 'UserProfileHeader_Items'}).text.strip()
    website_tag = soup.find('a', {'data-testid': 'UserProfileHeader_Items'})
    website = website_tag.get('title') if website_tag else ''

    # Close the WebDriver
    driver.quit()

    return bio, following_count, followers_count, location, website

# List of Twitter profile URLs
twitter_urls = [
    'https://twitter.com/GTNUK1',
    'https://twitter.com/whatsapp',
    'https://twitter.com/aacb_CBPTrade',
    'https://twitter.com/aacbdotcom',
    'https://twitter.com/@AAWindowPRODUCT',
    'https://www.twitter.com/aandb_kia',
    'https://twitter.com/ABHomeInc',
    'https://twitter.com/Abrepro',
    'https://www.twitter.com',
    'https://twitter.com/ACChristofiLtd',
    'https://twitter.com/aeclothing1',
    'https://www.twitter.com/',
    'https://twitter.com/AETechnologies1',
    'https://www.twitter.com/wix',
    'https://twitter.com/AGInsuranceLLC'
]

# Create CSV file with the extracted information
with open('twitter_profiles_data.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header
    csv_writer.writerow(['Twitter URL', 'Bio', 'Following Count', 'Followers Count', 'Location', 'Website'])

    # Loop through Twitter URLs and scrape information
    for url in twitter_urls:
        bio, following_count, followers_count, location, website = scrape_twitter_profile(url)
        csv_writer.writerow([url, bio, following_count, followers_count, location, website])

print('Twitter profiles data has been scraped and saved to twitter_profiles_data.csv')
