import ocr
import google_books

'''
    Code which defines the logic of the api.
'''

def get_book_data_from_image(ocr_ref, image):
    '''
        Main function called by flask to take in an image of a book, and return info about the book.
    '''
    full_cover_text, top_three_most_confident_hits = ocr.read_book_cover(ocr_ref, image)
    
    data = google_books.get_book_data(full_cover_text)
    if data == None:
        for hit in top_three_most_confident_hits:
            data = google_books.get_book_data(hit)
            if data != None:
                return data

    return None