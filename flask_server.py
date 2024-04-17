from flask import Flask, jsonify, request

import sys
import os

from girls_day import GirlsDayModel


# brauche zugriff auf das Model.
# objekt übergeben.



# Create a Flask app
app = Flask(__name__)


# Define a function to add CORS headers to responses
def add_cors_headers(response):
    # Allow requests from all origins
    response.headers['Access-Control-Allow-Origin'] = '*'
    # Allow all standard HTTP methods
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    # Allow the Content-Type header, which is necessary for POST and PUT requests
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

# Apply the CORS headers to all routes using a Flask decorator
@app.after_request
def after_request(response):
    return add_cors_headers(response)

model = None

def set_model(model):
    model = model


# Define a route for the API endpoint
@app.route('/api/on', methods=['GET'])
def on():
    return jsonify({'message': 'Turned Signal ON'})


# Define a route for the API endpoint
@app.route('/api/off', methods=['GET'])
def off():
    return jsonify({'message': 'Turned Signal OFF'})

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/', methods=['POST'])
def update_model():

    print(f'received:{request.get_json()}')

    X = [[1,0,0],[1,1,0], [0,1,0], [1,1,0], [0,0,0],[1,0,0],[1,1,0], [0,1,0], [1,1,0], [0,0,0]]
    data= request.get_json()
    y_tf = [x['rating'] for x in data]
    print (y_tf)
    y = [0 if x == False else 1 for x in y_tf]

    print(X)
    print(y)

    GirlsDayModel.train_model(X,y)
    return ("hello world")

#re-train the model
@app.route('/model', methods=['GET', 'POST'])
def example():

    # parse output
    # use it as input to scikit together with knowledge about images.
    # train model and store it.
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)



# Run the Flask app
if __name__ == '__main__':
    app.run()

