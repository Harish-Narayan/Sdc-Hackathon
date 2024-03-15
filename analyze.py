from extract_text import detect_text
from gemini_ai import gemini_classification
from sig import signature_extraction_start
from pymongo import MongoClient
from bson.json_util import dumps
from flask import jsonify
from imagekitio import ImageKit
import requests
from utils import process_check
from check_sign import verifySign

client = MongoClient('mongodb://localhost:27017')
db = client['chequedatabase']  # Database name
collection = db['chequecollection']  # Collection name
collection_processed_check = db['processedcheckcollection']

def analyze_cheque(filepath):
    raw_text = detect_text(filepath)
    cheque_details = gemini_classification(raw_text)
    # print(cheque_details)  #continue from here. cheque_details has the json of all extracted fields from the cheque
    signature_extraction_start(filepath)

    chequeSignPath = "./output/output.png"
    acc_no = cheque_details['account_number']
    accDetails = fetch_data(acc_no)
    # accDetails=accDe
    # print(accDetails)
    sign_url = accDetails["sign_url"]
    get_original_signature(sign_url)
    dbSignPath = "./dbSigns/dbSignature.jpg"
    ssimValue = verifySign(chequeSignPath, dbSignPath)
    process_check(ssimValue,cheque_details,accDetails)
    return "done"
def fetch_data(number):
    data = collection.find_one({"account_number": number})

    if data: 
        return data
    else:
        return jsonify({"message": "No data found"})
    
def get_original_signature(image_url):
    imagekit = ImageKit(
        private_key='private_WrxZPJhyTPfaW7fg+vVhdYcA+xM=',
        public_key='public_zskDEmBVQzt/Rz7rdX3lwqNwm60=',
        url_endpoint='https://ik.imagekit.io/rf39vtebd'
    )

    # Get the image data
    image_data = requests.get(image_url).content

    # Save the image to a file
    with open('./dbSigns/dbSignature.jpg', 'wb') as handler:
        handler.write(image_data)