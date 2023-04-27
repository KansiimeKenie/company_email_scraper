from scrap import *

# Testing extract_email_from_extracted_text
#                                           
def test_extract_email_from_extracted_text_with_valid_input():
    text = "This is an email: @keneth"
    assert extract_email_from_extracted_text(text) == "@keneth"

    #  test_extract_email_from_extracted_text_with_no_email():
    text = "This is not an email"
    assert extract_email_from_extracted_text(text) == None

#  test_extract_email_from_extracted_text_with_empty_string():
    text = ""
    assert extract_email_from_extracted_text(text) == None

# # end of Testing extract_email_from_extracted_text

def test_get_comapany_email_from_twitter_link():
    # Test case 1: Valid link with email in bio
    link = 'https://twitter.com/Amazon'
    expected_email = '@AmazonHelp'
    assert get_comapany_email_from_twitter_link(link) == expected_email

    # Test case 2: Valid link with no email in bio
    link = 'https://twitter.com/KatusiimeCarol5'
    expected_email = None
    assert get_comapany_email_from_twitter_link(link) == expected_email

    # Test case 3: Invalid link
    link = 'https://twitter.com/kansiime_keneth12'
    expected_email = 'Not Found'
    assert get_comapany_email_from_twitter_link(link) == expected_email 


# testing test_scrape_twitter_emails
def test_scrape_twitter_emails():
    # Test case 1: Valid company name
    company_names = ['amazon']
    expected_results = {'amazon': '@AmazonHelp'}
    assert scrape_twitter_emails(company_names) == expected_results

    # Test case 2: Invalid company name
    company_names = ['Invalid Company Name']
    expected_results = {'Invalid Company Name': 'Not Found'}
    assert scrape_twitter_emails(company_names) == expected_results

    # Test case 3: Multiple company names
    company_names = ['amazon', 'airbnb', 'lifyt']
    expected_results = {
        'amazon': '@AmazonHelp',
        'airbnb': '@airbnbhelp',
        'lifyt': '@AskLyft'
    }
    assert scrape_twitter_emails(company_names) == expected_results
# end test_scrape_twitter_emails