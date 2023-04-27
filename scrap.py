from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import re

def extract_email_from_extracted_text(text):
    try:
        email_regex = r"@[\w]+"
        email_matches = re.findall(email_regex, text)
        if email_matches:
            return email_matches[0]
        else:
            return None
    except:
        print("An error occurred while trying to extract the email.")
        return None

#get company emails from twitter link
def get_comapany_email_from_twitter_link(link):
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(link)
        bio = driver.find_element(By.CSS_SELECTOR,'div[data-testid="UserDescription"]').text

        if bio is not None:
            email = extract_email_from_extracted_text(bio)
            print(f"Extracted email : {email}")
            return email
        else:
            print("Could not extract email")
            return "Not Found"
    except Exception as e:
        print(f"An error occurred while trying to extract the email: {e}")
        return "Not Found"   

def scrape_twitter_emails(company_names):
    results = {}
    for company_name in company_names:
        try:
            print(f"Searching for {company_name} on Google...")
            search_query = company_name + ' Company Twitter link'
            search_url = f"https://www.google.com/search?q={search_query}"
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
            response = requests.get(search_url, headers=headers)
            # parsing the HTML response using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            # extracting the first search result URL from the page
            result = soup.find('div', class_='g')
            link = result.find('a')['href']
            print(f"Extracted Twitter URL: {link}")
            #call function to get emails from links
            email = get_comapany_email_from_twitter_link(link)
            results[company_name] = email
        except AttributeError as e:
            response = f"No Twitter link found for {company_name}: {str(e)}"
            print(response)
            results[company_name] = "Not Found"
        except Exception as e:
            response = f"Error occurred while processing {company_name}: {str(e)}"
            print(response)
            results[company_name] = "Error"
    return results
