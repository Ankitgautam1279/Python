from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')  # Serve an HTML file

# API endpoint for app functionality
@app.route('/process', methods=['POST'])
def process():
    data = request.json  # Receive data from the front end
    result = int(data['number']) * 2  # Example logic: Double the number
    return jsonify({'result': result})  # Return JSON response

if __name__ == '__main__':
    app.run(debug=True)
