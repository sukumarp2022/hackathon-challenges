import uuid
from datetime import datetime


tasks_db = {}
users_db = {}


class Task:
    def __init__(self, title, description, assigned_to=None, priority="medium"):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.status = "todo"
        self.priority = priority
        self.assigned_to = assigned_to
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
        self.tags = []
        self.comments = []

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "priority": self.priority,
            "assigned_to": self.assigned_to,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "tags": self.tags,
            "comments": self.comments
        }

    def update(self, data):
        if "title" in data:
            self.title = data["title"]
        if "description" in data:
            self.description = data["description"]
        if "status" in data:
            self.status = data["status"]
        if "priority" in data:
            self.priority = data["priority"]
        if "assigned_to" in data:
            self.assigned_to = data["assigned_to"]
        self.updated_at = datetime.now().isoformat()


class User:
    def __init__(self, name, email, role="member"):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.role = role

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "role": self.role
        }
