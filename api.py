import ocr
import google_books

'''
    Code which defines the logic of the api.
'''

def get_book_data_from_image(ocr_ref, image):
    '''
        Main function called by flask to take in an image of a book, and return info about the book.
    '''
    full_cover_text = ocr.read_book_cover(ocr_ref, image)
    return google_books.get_book_data(full_cover_text)
