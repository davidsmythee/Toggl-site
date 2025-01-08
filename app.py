from flask import Flask, render_template, request, jsonify
import uuid

# print("Starting Flask application...")  # Debug print

app = Flask(__name__)

@app.route('/')
def index():
    print("Serving the index page...")  # Debug print
    return render_template('index.html')

if __name__ == '__main__':
    print("Running Flask app...")  # Debug print
    app.run(debug=True)


