from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017')
db = client['chequedatabase']  # Database name
collection = db['chequecollection']  # Collection name
collection_processed_check = db['processedcheckcollection']

def insert(new_json):
    collection_processed_check.insert_one(new_json)
    
def process_check(ssim, cheque_details, acc_details):
    output_json = {}
    output_json["account_number"] = cheque_details["account_number"]
    output_json["ifsc_code"] = cheque_details["ifsc_code"]
    output_json["micr_code"] = cheque_details["micr_code"]
    output_json["issue_date"] = cheque_details["issue_date"]
    output_json["bearer_name"] = cheque_details["bearer_name"]
    output_json["amount"] = cheque_details["amount"]
    if ( ssim<0.5 ):
        output_json["approval_status"] = "Denied"
        output_json["reason"] = "Signature Mismatch"
        insert(output_json)
        print(output_json)
        return "done"
    elif ( ssim>0.5 and ssim<0.75 ):
        output_json["approval_status"] = "Waiting for human intervention"
        output_json["reason"] = "Signature Mismatch"
        insert(output_json)
        print(output_json)
        return "done"
    
    current_acc_balance = acc_details['balance']
    if(int(cheque_details['amount']) > int(current_acc_balance)):
        output_json["approval_status"] = "Denied"
        output_json["reason"] = "Insuffient Balance"
        insert(output_json)
        print(output_json)
        return "done"
    
    output_json["approval_status"] = "Approved"
    output_json["reason"] = ""
    insert(output_json)
    print(output_json)
    return "done"
