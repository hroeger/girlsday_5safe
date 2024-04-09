from flask import Flask, jsonify

# Create a Flask app
app = Flask(__name__)

# Define a route for the API endpoint
@app.route('/api/on', methods=['GET'])
def on():
    return jsonify({'message': 'Turned Signal ON'})


# Define a route for the API endpoint
@app.route('/api/off', methods=['GET'])
def off():
    return jsonify({'message': 'Turned Signal OFF'})


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)