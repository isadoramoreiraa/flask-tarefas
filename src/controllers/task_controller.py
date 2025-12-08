from src.models.task import Task
from src.extensions import db
from flask import jsonify

def create_task(data, user_id):
    task = Task(
        title=data.get("title"),
        description=data.get("description"),
        status=data.get("status"),
        user_id=user_id
    )
    db.session.add(task)
    db.session.commit()

    return jsonify({"message": "Tarefa criada"}), 201


def get_tasks(user, is_admin):
    if is_admin:
        tasks = Task.query.all()
    else:
        tasks = Task.query.filter_by(user_id=user).all()

    return jsonify([{
        "id": t.id,
        "title": t.title,
        "description": t.description,
        "status": t.status,
        "user_id": t.user_id
    } for t in tasks])


def update_task(task_id, data, user, is_admin):
    if is_admin:
        task = Task.query.get(task_id)
    else:
        task = Task.query.filter_by(id=task_id, user_id=user).first()

    if not task:
        return jsonify({"error": "Não encontrado"}), 404

    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.status = data.get("status", task.status)

    db.session.commit()
    return jsonify({"message": "Atualizado"})


def delete_task(task_id, user, is_admin):
    if is_admin:
        task = Task.query.get(task_id)
    else:
        task = Task.query.filter_by(id=task_id, user_id=user).first()

    if not task:
        return jsonify({"error": "Não encontrado"}), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": "Deletado"})
