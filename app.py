from flask import Flask, render_template
app = Flask(__name__, template_folder='application/templates/', static_folder='application/static')

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/logs')
def logs_all():
    return render_template('logs/list.html', logs=logs)

@app.route('/logs/<int:log_id>')
def logs_detail(log_id):
    for log in logs:
        if log["id"] == log_id:
            target_log = log
    return render_template('logs/detail.html', log_id=log_id, log=target_log)

@app.route('/logs/new')
def logs_new():
    return render_template('logs/form.html')


@app.errorhandler(404)
def page_not_found(e):
    return '''
    <h1>ログが見つかりません</h1>
    <a href="/">ホームに戻る</a>
    ''', 404

@app.errorhandler(500)
def internal_server_error(e):
    return '''
    <h1>サーバーエラーが発生しました</h1>
    <a href="/">ホームに戻る</a>
    ''', 500

if __name__ == '__main__':
    app.run(debug=True)