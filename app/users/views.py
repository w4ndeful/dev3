from flask import Blueprint, render_template, request, redirect, url_for

users_bp = Blueprint('users', __name__, template_folder='templates/users')

@users_bp.route('/hi/<name>')
def greetings(name):
    age = request.args.get('age', 'unknown')
    return render_template('hi.html', name=name.upper(), age=age)

@users_bp.route('/admin')
def admin():
    return redirect(url_for('users.greetings', name='Administrator', age=45))
