from scrap import *

#read company_names from file
def read_file_names(file):
    try:
        with open(file) as f:
            company_names = [line.strip() for line in f]
        return company_names
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

#storing the emails in a file
def create_email_file(file, emails):
    try:
        with open(file, 'w') as f:
            for company_name, email in emails.items():
                f.write(f"{company_name}: {email}\n")
    except Exception as e:
        print(f"An error occurred while creating the email file: {e}")


company_names = read_file_names('company_names.txt')
emails = scrape_twitter_emails(company_names)
create_email_file('campany_emails.txt', emails)