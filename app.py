from flask import Flask, render_template, request, send_file,jsonify
import os
from pymongo import MongoClient
from analyze import analyze
from bson.json_util import dumps


app = Flask(__name__)
client = MongoClient('mongodb://mongo:27017/')
db = client['chequedatabase']  # Database name
collection = db['chequecollection']  # Collection name
collection_processed_check = db['processedcheckcollection']

# Directory to store uploaded images
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        analysis_result = analyze("uploads/"+filename)
        return filename
    

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), as_attachment=True)

@app.route('/insert', methods=['POST'])
def insertProcessedCheck():
    # Expecting data in the form of {"name": "John Doe", "age": 30}
    data = request.json
    collection_processed_check.insert_one(data)
    return jsonify({"message": "Data inserted successfully"}), 201

@app.route('/getAllProcessedCheck', methods=['GET'])
def getAllProcessedCheck():
    documents = collection.find({})
    
    # Convert MongoDB query result to a list of dictionaries
    data = list(documents)
    
    # Convert all ObjectId's to string to make it JSON serializable
    for document in data:
        document["_id"] = str(document["_id"])

    return jsonify(data,200)

@app.route('/fetch/<number>', methods=['GET'])
def fetch_data(number):
    # Query the collection for documents where the "name" field matches the parameter
    data = collection.find_one({"account_number": number})
    if data: 
            return dumps(data), 200
    else:
        return jsonify({"message": "No data found"}), 404
    
@app.route('/process_checked')
def process_checked():
    # Perform any processing if needed
    # Redirect to the desired page
    return render_template('p_cheque.html')
if __name__ == '__main__':
    app.run(debug=True)
