from PIL import Image
from surya.recognition import RecognitionPredictor
from surya.detection import DetectionPredictor
import regex as re

'''
    This code is a wrapper around the Surya OCR python library.
    https://github.com/VikParuchuri/surya
'''

filter_confidence_threshold=0.5
filter_patterns = [
    r"\bnew york times (best\s*)?seller\b",
    r"\b(international|national)?\s*bestseller\b",
    r"\bbestselling author\b",
    r"\bnow (a|an)? (major )?(motion picture|netflix (original )?series|tv series|film)\b",
    r"\bbook club pick\b",
    r"\b(reese's|oprah's) book club\b",
    r"\bsoon to be (a )?(movie|film|series|adaptation)\b",
    r"\bover \d+(,\d+)? (copies sold|sold worldwide)\b",
    r"\baward[- ]winning\b",
    r"\bcritically acclaimed\b",
    r"\bpulitzer prize (winner|winning)\b",
    r"\b(winner|shortlisted|finalist) of (the )?[a-zA-Z ]+ (award|prize)\b",
    r"\bincludes bonus content\b",
    r"\bwith (a )?new (introduction|foreword|afterword)\b",
    r"\b(special|exclusive|limited|collector'?s|deluxe) edition\b",
    r"\bmust[- ]read\b",
    r"\b(page[- ]turner|gripping|thrilling|unputdownable|heartwarming)\b",
    r"\bfrom the #?1 bestselling author\b",
    r"\bperfect for fans of [^.,;:!?]*",
    r"\bas seen on (tv|netflix|amazon)\b",
    r"\bamazon (top pick|bestseller)\b",
    r"\b(editor'?s choice|staff pick)\b",
    r"\bgoodreads choice awards?\b",
    r"\bpulitzer prize\b",
    r"\bbooker prize\b",
    r"\bnational book award\b",
    r"\bnewbery medal\b",
    r"\bcaldecott medal\b",
    r"\bhugo award\b",
    r"\bnebula award\b",
    r"\bcosta book award\b",
    r"\bwomen'?s prize for fiction\b",
    r"\bman booker prize\b",
    r"\bcoretta scott king award\b",
    r"\bedgar award\b",
    r"\bbram stoker award\b",
    r"\b(introduction|foreword|afterword|preface) by [A-Z][a-zA-Z .'-]+\b",
    r"\btranslated by [A-Z][a-zA-Z .'-]+\b"
]


def init_ocr():
    '''
        Downloads the model/weights if they are not cached. Retruns a reference to the recognition and detection predictor.
    '''
    return RecognitionPredictor(), DetectionPredictor()  

def read_book_cover(ocr_ref, image):
    '''
        Reads the book cover from the image and returns the text.
    '''
    recognition_predictor, detection_predictor = ocr_ref
    image = Image.open(image)
    predictions = recognition_predictor([image], [['en']], detection_predictor)[0].text_lines
    full_cover_text = ' '.join([i.text for i in predictions if filter_text(i)])
    print(f'Post-processed book cover text: {full_cover_text}')
   
    return full_cover_text

def filter_text(line):

    if line.confidence <= filter_confidence_threshold:
        print(f'Filtering out {line.text} due to a confidence of {line.confidence}')
        return False

    for pattern in filter_patterns:
        if re.search(pattern, line.text, re.IGNORECASE):
            print(f'Filtering out {line.text} due to a match with {pattern} regex')
            return False

    return True
