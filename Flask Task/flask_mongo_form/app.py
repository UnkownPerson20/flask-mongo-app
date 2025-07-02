from flask import Flask, request, render_template, redirect, url_for
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash

app = Flask(__name__)

# Load MongoDB URI from .env
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

# Connect to MongoDB Atlas
client = MongoClient(MONGO_URI)
db = client["Task2_database"]
collection = db["users"]

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        passwd = request.form['password']
        try:
            hashed_password = generate_password_hash(passwd)
            collection.insert_one({"name": name, "email": email, "password": hashed_password})
            return redirect(url_for('success'))
        except Exception as e:
            return render_template('form.html', error=str(e))
    return render_template('form.html')

@app.route('/submit')
def success():
    return render_template('submit.html')

if __name__ == '__main__':
    app.run(debug=True)
