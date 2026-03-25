from models import Task, User, tasks_db, users_db


def create_task(title, description, assigned_to=None, priority="medium"):
    task = Task(title, description, assigned_to, priority)
    tasks_db[task.id] = task
    return task


def get_task(task_id):
    return tasks_db.get(task_id)


def get_all_tasks():
    return list(tasks_db.values())


def update_task(task_id, data):
    task = tasks_db.get(task_id)
    if task:
        task.update(data)
        return task
    return None


def delete_task(task_id):
    if task_id in tasks_db:
        del tasks_db[task_id]
        return True
    return False


def get_tasks_by_status(status):
    return [t for t in tasks_db.values() if t.status == status]


def get_tasks_by_priority(priority):
    return [t for t in tasks_db.values() if t.priority == priority]


def search_tasks(query):
    results = []
    for task in tasks_db.values():
        if query.lower() in task.title.lower() or query.lower() in task.description.lower():
            results.append(task)
    return results


def add_comment_to_task(task_id, comment_text, author):
    task = tasks_db.get(task_id)
    if task:
        comment = {
            "text": comment_text,
            "author": author,
            "created_at": __import__("datetime").datetime.now().isoformat()
        }
        task.comments.append(comment)
        return comment
    return None


def add_tag_to_task(task_id, tag):
    task = tasks_db.get(task_id)
    if task:
        if tag not in task.tags:
            task.tags.append(tag)
        return task
    return None


def create_user(name, email, role="member"):
    user = User(name, email, role)
    users_db[user.id] = user
    return user


def get_user(user_id):
    return users_db.get(user_id)


def get_all_users():
    return list(users_db.values())
