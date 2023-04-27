# company_email_scraper
This project scrapes company Twitter pages to extract email addresses from their bio information.

Installation
To use this project, you will need to have Python 3 installed on your computer, as well as the following packages:

selenium
webdriver_manager
bs4
requests
You can install these packages using pip, like so:

bash
Copy code
pip install selenium webdriver_manager bs4 requests

Usage
To use this project, you need to provide a list of company names as input. The scrape_twitter_emails function will search for each company's Twitter page and extract the email address from their bio.

Notes
This project uses Selenium to automate the process of searching for company Twitter pages and extracting email addresses from their bios.
The get_comapany_email_from_twitter_link function assumes that the email address is located in the company's Twitter bio, and uses a regular expression to extract it. This may not always be the case, so the function may not work for all companies.
The scrape_twitter_emails function only searches for the first search result on Google. If a company has multiple Twitter pages, the function may not find the correct one.
This project is provided as-is, without any guarantees or warranties. Use at your own risk.
