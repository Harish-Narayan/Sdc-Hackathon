from extract_text import detect_text
from gemini_ai import gemini_classification

def analyze(filepath):
    raw_text = detect_text(filepath)
    cheque_details = gemini_classification(raw_text)
    print(cheque_details)  #continue from here. cheque_details has the json of all extracted fields from the cheque
    return "done"
