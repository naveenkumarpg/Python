from flask import Flask, request, jsonify
from flask_cors import CORS
from code_analyzer_open_ai import generate_comments_open_ai

app = Flask(__name__)
CORS(app, origins='*')

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        try:
            data = request.get_data()  # Get raw data from the request
            return data, 200  # Return the raw data with an OK status
        except Exception as e:
            # Log the error or handle it appropriately
            return jsonify({"error": str(e)}), 500  # Return an error message with a 500 status
    else:
        return "Send a POST request to see the data.", 200

@app.route('/code-analyzer', methods=['GET', 'POST'])
def abc():

    if request.method == 'POST':
        try:
            data = request.get_data()   # Get raw data from the request
            return generate_comments_open_ai(data), 200  # Return the raw data with an OK status
        except Exception as e:
            # Log the error or handle it appropriately
            return f'Some error occurred while generating {e}'
    else:
        return "Send a POST request to see the data.", 200
    

if __name__ == '__main__':
    app.run(port=5000, debug=True)
