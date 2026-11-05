from flask import Blueprint, render_template, request, redirect, url_for, flash
logs_bp = Blueprint('logs_bp', __name__)

logs = [
    {
        "id": 1,
        "title": "Flaskのルーティングを学習",
        "body": "URLとビュー関数の関係を理解した。",
        "category": "Flask",
        "study_time": 60,
        "study_date": "2026/5/28"
    },
    {
        "id": 2,
        "title": "htmlの学習",
        "body": "htmlの基礎について学べた",
        "category": "HTML",
        "study_time": 90
    },
    {
        "id": 3,
        "title": "pythonの学習",
        "body": "pythonの基礎について学べた",
        "category": "Python",
        "study_time": 40
    },
    {
        "id": 4,
        "title": "Flaskの学習",
        "body": "Flaskの基礎について学べた",
        "category": "Flask",
        "study_time": 40
    },
    {
        "id": 5,
        "title": "Flaskの学習",
        "body": "Flaskの基礎について学べた",
        "category": "HTML",
        "study_time": 40
    },
    {
        "id": 6,
        "title": "Flaskの学習",
        "body": "Flaskの基礎について学べた",
        "category": "JavaScript",
        "study_time": 40
    },
    {
        "id": 7,
        "title": "Flaskの学習",
        "body": "Flaskの基礎について学べた",
        "category": "CSS",
        "study_time": 40
    }
]

@logs_bp.route('/logs')
def logs_list():
    return render_template('logs/list.html', logs=logs)

@logs_bp.route('/logs/<int:log_id>')
def logs_detail(log_id):
    for log in logs:
        if log["id"] == log_id:
            target_log = log
    return render_template('logs/detail.html', log_id=log_id, log=target_log)

@logs_bp.route('/logs/new')
def logs_form():
    return render_template('logs/form.html')

@logs_bp.route('/submit', methods=['POST'])
def logs_submit():
    title = request.form.get('title')
    category = request.form.get('category')
    study_time = request.form.get('study_time')
    study_date = request.form.get('study_date')
    body = request.form.get('body')
    new_id = logs[-1]["id"] + 1 if logs else 1
    new_log = {
        "id": new_id,
        "title": title,
        "body": body,
        "category": category,
        "study_time": study_time,
        "study_date": study_date
    }
    logs.append(new_log)
    flash('投稿されました！', 'success')
    return redirect(url_for('logs_bp.logs_list'))