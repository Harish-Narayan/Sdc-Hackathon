import os
from langchain_google_genai import ChatGoogleGenerativeAI
import json

def gemini_classification(raw_text):
        if "GOOGLE_API_KEY" not in os.environ:
                os.environ["GOOGLE_API_KEY"] = "AIzaSyDRxdGIcKqXuYkjiZpA74oGTU7jUG4ipOM"

        llm = ChatGoogleGenerativeAI(model="gemini-pro")

        result = llm.invoke("A list of strings parsed from an image of a bank cheque is provided below. I want to classify the strings into the following categories:\
                        1. account_number\
                        2. ifsc_code\
                        3. bearer_name\
                        4. amount\
                        5. amount_in_words\
                        6. issue_date\
                        7. expiry_date (Calculate from the string that contains how long the cheque is valid. Ignore this field if not available)\
                        8. micr_code ()\
                                \
                        bearer_name is the person's name present in the cheque to whom the amount is to be paid\
                                \
                        micr_code is a 9-digit code.\
                        Eg: ⑈309159⑈ 500211012⑆ 426160⑈ 31\
                        Here, 500211012 is the micr_code.\
                                \
                        Issue date is always in the format ddmmyyyy in the raw text but in JSON output, provide the date in the format dd/mm/yyyy\
                        Calculate expiry date from a string that says about the validity of the cheque. If a string similar to 'VALID FOR THREE MONTHS FROM THE DATE OF ISSUE' is present, calculate expiry_date from issue_date using that string.\
                        Amount in words will always be the amount written in words. Check the spelling and correct if any other error is detected in amount_in_words.        \
                        Remove any special characters in the amount field. amount field should contain only the number.\
                        The output should be in JSON. Ignore any field (mark as nil) if it is not present in the strings. The output should be just the JSON file with no additional strings included." + raw_text)
        
        stripped_result = result.content.replace('json', '').strip()
        stripped_result = stripped_result.replace('`', '').strip()
        stripped_result = stripped_result.replace('JSON', '').strip()
        result_json = json.loads(stripped_result)
        return result_json
