from flask import Flask, request, jsonify
from flask_cors import CORS
from database import (
    create_task, get_task, get_all_tasks, update_task, delete_task,
    get_tasks_by_status, search_tasks, add_comment_to_task, add_tag_to_task,
    create_user, get_user, get_all_users
)

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return jsonify({"message": "Task Tracker API", "version": "1.0.0"})


@app.route("/tasks", methods=["GET"])
def list_tasks():
    status = request.args.get("status")
    if status:
        tasks = get_tasks_by_status(status)
    else:
        tasks = get_all_tasks()
    return jsonify([t.to_dict() for t in tasks])


@app.route("/tasks", methods=["POST"])
def create_new_task():
    data = request.get_json()
    title = data.get("title")
    description = data.get("description", "")
    assigned_to = data.get("assigned_to")
    priority = data.get("priority", "medium")

    if not title:
        return jsonify({"error": "Title is required"}), 400

    task = create_task(title, description, assigned_to, priority)
    return jsonify(task.to_dict()), 201


@app.route("/tasks/<task_id>", methods=["GET"])
def get_single_task(task_id):
    task = get_task(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task.to_dict())


@app.route("/tasks/<task_id>", methods=["PUT"])
def update_existing_task(task_id):
    data = request.get_json()
    task = update_task(task_id, data)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task.to_dict())


@app.route("/tasks/<task_id>", methods=["DELETE"])
def delete_existing_task(task_id):
    success = delete_task(task_id)
    if not success:
        return jsonify({"error": "Task not found"}), 404
    return jsonify({"message": "Task deleted"}), 200


@app.route("/tasks/search", methods=["GET"])
def search():
    query = request.args.get("q", "")
    tasks = search_tasks(query)
    return jsonify([t.to_dict() for t in tasks])


@app.route("/tasks/<task_id>/comments", methods=["POST"])
def add_comment(task_id):
    data = request.get_json()
    text = data.get("text")
    author = data.get("author")
    comment = add_comment_to_task(task_id, text, author)
    if not comment:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(comment), 201


@app.route("/tasks/<task_id>/tags", methods=["POST"])
def add_tag(task_id):
    data = request.get_json()
    tag = data.get("tag")
    task = add_tag_to_task(task_id, tag)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task.to_dict())


@app.route("/users", methods=["GET"])
def list_users():
    users = get_all_users()
    return jsonify([u.to_dict() for u in users])


@app.route("/users", methods=["POST"])
def create_new_user():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    role = data.get("role", "member")

    if not name or not email:
        return jsonify({"error": "Name and email are required"}), 400

    user = create_user(name, email, role)
    return jsonify(user.to_dict()), 201


@app.route("/users/<user_id>", methods=["GET"])
def get_single_user(user_id):
    user = get_user(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict())


# BUG: This endpoint has issues - status transition validation missing
@app.route("/tasks/<task_id>/transition", methods=["POST"])
def transition_task(task_id):
    data = request.get_json()
    new_status = data.get("status")
    task = get_task(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    task.status = new_status
    return jsonify(task.to_dict())


# TODO: Add endpoint for bulk task operations
# TODO: Add endpoint for task statistics/dashboard
# TODO: Add endpoint for task assignment history
# TODO: Add input validation and error handling improvements


if __name__ == "__main__":
    app.run(debug=True, port=5000)
