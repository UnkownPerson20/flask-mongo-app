# Import necessary modules
from flask import Flask, jsonify  # Flask is used to create the web application, jsonify converts Python objects to JSON format
import json  # Used to work with JSON data

# Create an instance of the Flask application
app = Flask(__name__)

# Define a route for the '/api' endpoint
@app.route('/api')
def api():
    try:
        # Try to open and load the contents of 'data.json'
        with open('data.json', 'r') as file:
            data = json.load(file)  # Load JSON data from the file
        return jsonify(data)  # Return the JSON data as a response
    except Exception as e:
        # If there's any error (e.g., file not found, invalid JSON), return an error message with status code 500
        return jsonify({"error": str(e)}), 500

# Entry point of the application
if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode, useful for development
