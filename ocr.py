from PIL import Image
from surya.recognition import RecognitionPredictor
from surya.detection import DetectionPredictor

'''
    This code is a wrapper around the Surya OCR python library.
    https://github.com/VikParuchuri/surya
'''

def init_ocr():
    '''
        Downloads the model/weights if they are not cached. Retruns a reference to the recognition and detection predictor.
    '''
    return RecognitionPredictor(), DetectionPredictor()  

def read_book_cover(ocr_ref, image):
    '''
        Reads the book cover from the image and returns the text. Since the text is not always accurate, we also return the top three most confident reads.
        We can attempt to search for these separately to prevent searching for gibberish.
    '''
    recognition_predictor, detection_predictor = ocr_ref
    image = Image.open(image)
    predictions = recognition_predictor([image], ['en'], detection_predictor)
    full_cover_text = ' '.join([i.text for i in predictions[0].text_lines])
    top_three_most_confident_hits = [i.text for i in sorted(predictions[0].text_lines, key=lambda x: x.confidence, reverse=True)[:3]]

    return full_cover_text, top_three_most_confident_hits