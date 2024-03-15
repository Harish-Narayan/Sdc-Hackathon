from extract_text import detect_text
from gemini_ai import gemini_classification
from sig import signature_extraction_start
from check_sign import verifySign
from app import fetch_data
from utils import process_check

def analyze(filepath):
    raw_text = detect_text(filepath)
    cheque_details = gemini_classification(raw_text)
    print(cheque_details)  #continue from here. cheque_details has the json of all extracted fields from the cheque
    signature_extraction_start(filepath)

    chequeSignPath = "./output/output.png"
    acc_no = cheque_details['account_number']
    accDetails = fetch_data(acc_no)
    sign_url = accDetails["sign_url"]
    dbSignPath = ""
    ssimValue = verifySign(chequeSignPath, dbSignPath)
    process_check(ssimValue,cheque_details,accDetails)
    return "done"
