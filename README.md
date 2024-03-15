# Solution
  The solution is a web application that prompts the user to upload the scanned copy of the cheque. Then the image goes through a sequence of checking process that decides whether the cheque should be bounced or cleared.
  First, the required information from the cheque image is extracted. This information includes the account number, the payee, amount, MICR code and signature. The signature is compared with the original signature stored in the bank database.
  The cheque passes through if the respective account has sufficient balance to perform the transaction.

# Extracting Information from Cheque
  For extracting the information from the cheque we use the vision API provided by google.
  link: https://cloud.google.com/vision/docs


  This uses the OCR to get us all the text needed. Then we extend this pipeline to the gemini AI which uses custom prompt templates to fetch the information needed in a particular format.

  For extracting the image sign we use the thresholding method by finding connected components in the cheque

# Verification Process involved:
  Signature Verification: We find the structural similarity score to detect if the sign is forged or not. We use custom threshold values finetuned for cheques.
  Insufficient balance checks are performed
  
  


