import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"test-project1-363705-3d4548a263d7.json"

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision

    client = vision.ImageAnnotatorClient()

    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    extracted_raw_text = response.full_text_annotation.text
    
    return  extracted_raw_text