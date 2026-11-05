from flask import Blueprint, render_template, request, redirect, url_for, flash
main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/about')
def about():
    return render_template('about.html')

@main_bp.errorhandler(404)
def page_not_found(e):
    return '''
    <h1>ログが見つかりません</h1>
    <a href="/">ホームに戻る</a>
    ''', 404

@main_bp.errorhandler(500)
def internal_server_error(e):
    return '''
    <h1>サーバーエラーが発生しました</h1>
    <a href="/">ホームに戻る</a>
    ''', 500