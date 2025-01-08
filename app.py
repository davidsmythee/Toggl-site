from flask import Flask, render_template, request, jsonify
import uuid

# print("Starting Flask application...")  # Debug print

app = Flask(__name__)

@app.route('/')
def index():
    print("Serving the index page...")  # Debug print
    return render_template('index.html')
    
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)



