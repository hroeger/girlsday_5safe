# show images
# store labels
# fit models
# store model.

# i do not even need a gd instance!
# lets try a flask server
# app.py

from flask import Flask
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def gd_training_app():
    return 'Hello, World!'

tasks = []

@app.route('/api/tasks', methods=['GET'])

def get_tasks():
    return "hello world"

 

@app.route('/api/tasks', methods=['POST'])

def add_task():

    data = request.get_json()

    task = data.get('task', '')

    tasks.append(task)

    return jsonify({'message': 'Task added successfully!'})

 

@app.route('/api/tasks/<int:index>', methods=['DELETE'])

def remove_task(index):

    if 0 <= index < len(tasks):

        del tasks[index]

        return jsonify({'message': 'Task removed successfully!'})

    else:

        return jsonify({'error': 'Invalid index!'}), 400


# endpoint
# image