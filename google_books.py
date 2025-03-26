import requests
import json

'''
    This code is a wrapper around the Google Books API.
    https://developers.google.com/books/docs/v1/using
'''

API_URL = "https://www.googleapis.com/books/v1/volumes?q="  # Base API URL for search queries
def get_book_data(search_term):
    '''
        Returns the book data from the Google Books API.
    '''

    # Call API query
    response = requests.get(API_URL + search_term)
    data = response.json()

    # Check if book exists
    if "items" not in data or not data["items"]:
        return {"message": "No books found"}, 404

    # Extract only first book result
    item = data["items"][0]
    volume_info = item.get("volumeInfo", {})

    book = {
        "title": volume_info.get("title", "No Title"),
        "subtitle": volume_info.get("subtitle", "No Subtitle"),
        "authors": volume_info.get("authors", ["Unknown Author"]),
        "average_rating": volume_info.get("averageRating", "No Rating"),
        "ratings_count": volume_info.get("ratingsCount", 0),
        "page_count": volume_info.get("pageCount", "N/A"),
        "categories": volume_info.get("categories", ["No Categories"]),
        "description": volume_info.get("description", "No Description Available"),
    }, 200

    return book