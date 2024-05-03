# import libraries
import requests
from bs4 import BeautifulSoup
import lxml

###################################################################################################

# test connection
url = 'https://www.amazon.com/VEVOR-Compost-Spreader-Adjustable-24/dp/B0BW84D326/ref=sr_1_2?dib=eyJ2IjoiMSJ9.m6lPDa5__RBJ3UPlJyQHPmCr-Twcve6_fo_Y2ssB61BfLzmv21vfhhzXn7SRmt5uSjsVDWH4qMIvhFSJMCCR0US8qD1bKlwgkkk0fQ6VtOr8Ci3OSWf2xAsSUS_KzUBM1K6uwYzHTb1mZGj7X-9E2h7Vj3VMJrYhL-cdFjdxQuGLrhAyUK-r7oDaOHJnKsBityV7f9Bn9Rd0KVnufL8We16c8cz8gfOeNNFV-TRjKNztJeAhyzO2pbw-ejEge7mgTixaxdvxxMlruHvJg5pwfpH9EyTYRqw3OQActqLGzC4.sJfzQYQaiv7SH0cyuW3j34lIlM7vrg0OHfbQuyP9WOE&dib_tag=se&keywords=Peat+moss+roller&qid=1714699015&sr=8-2'

response = requests.get(url)

print(response.text)

###################################################################################################

# Define our soup
soup = BeautifulSoup(response.text, "lxml")

###################################################################################################

# Grab title
title_element = soup.select_one('#productTitle')

title = title_element.text.strip() # strip the whitespace

print(title)

###################################################################################################

# Grab rating
rating_element = soup.select_one('#acrPopover')

rating_text = rating_element.text.strip() # strip whitespace
rating = rating_text[:3] # slice rating from string

print(rating)

###################################################################################################

# Grab price
price_element = soup.select_one('span.a-price').select_one('span.a-offscreen') # two levels deep

print(price_element.text)

###################################################################################################

# Grab image
image_element = soup.select_one('#landingImage')

image = image_element.attrs.get('src') # get attribute src

print(image)

###################################################################################################

# Grab description
description_element = soup.select_one('#feature-bullets')

print(description_element.text[20:]) # slice off section title

###################################################################################################

# Grab reviews
review_elements = soup.select("div.review")

scraped_reviews = [] # initialize list

count = 0 # initialize counter

# iterate through all reviews
for review in review_elements:

    if count == 3: # limit to 3 reviews
        break

    # name
    r_author_element = review.select_one("span.a-profile-name")
    r_author = r_author_element.text if r_author_element else None # accounts for blank names

    # rating
    r_rating_element = review.select_one("i.review-rating")
    r_rating = r_rating_element.text[:3] if r_rating_element else None

    # title
    r_title_element = review.select_one("a.review_title")
    if r_title_element: # check if r_title_element is not None
        r_title_span_element = r_title_element.select_one("span:not([class])") # select span elements without attributes
        r_title = r_title_span_element.text if r_title_span_element else None
    else:
        r_title = None

    # content
    r_content_element = review.select_one("span.review-text")
    r_content = r_content_element.text if r_content_element else None

    # date
    r_date_element = review.select_one("span.review-date")
    r_date = r_date_element.text if r_date_element else None

    # verified purchase?
    r_verified_element = review.select_one("span.a-size-mini")
    r_verified = r_verified_element.text if r_verified_element else None

    # create a dictionary of elements for the review
    r = {
        "author": r_author,
        "rating": r_rating,
        "title": r_title,
        "content": r_content,
        "date": r_date,
        "verified": r_verified
    }

    scraped_reviews.append(r) # add review to list

    count +=1 # increment counter

print(scraped_reviews)