from flask import Flask, request, jsonify
import db_config

app = Flask(__name__)

# READ
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(db_config.get_tasks())

# CREATE
@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json.get('task')
    db_config.add_task(task)
    return jsonify({"message": "Task added"}), 201

# UPDATE
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    new_task = request.json.get('task')
    db_config.update_task(task_id, new_task)
    return jsonify({"message": "Task updated"})

# DELETE
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    db_config.delete_task(task_id)
    return jsonify({"message": "Task deleted"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
#    app.debug = True
#   app.run()

