from extract_text import detect_text
from gemini_ai import gemini_classification
from imagekitio import ImageKit

def analyze(filepath):
    raw_text = detect_text(filepath)
    cheque_details = gemini_classification(raw_text)
    print(cheque_details)  #continue from here. cheque_details has the json of all extracted fields from the cheque
    
    # original_signature = get_original_signature()
    return "done"

def get_original_signature():
    imagekit = ImageKit(
        private_key='private_WrxZPJhyTPfaW7fg+vVhdYcA+xM=',
        public_key='public_zskDEmBVQzt/Rz7rdX3lwqNwm60=',
        url_endpoint='https://ik.imagekit.io/rf39vtebd'
    )

    # Get the image data
    image_data = requests.get(image_url).content

    # Save the image to a file
    with open('image_name.jpg', 'wb') as handler:
        handler.write(image_data)