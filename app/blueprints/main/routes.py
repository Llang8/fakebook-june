from .import bp as app
from flask import render_template, request, url_for, flash, redirect
from flask_login import current_user
from app import db
from app.blueprints.authentication.models import User
from app.blueprints.blog.models import Post

@app.route('/')
def home():
    # print(current_user.followed_posts)
    context = {
        'posts': current_user.followed_posts() if current_user.is_authenticated else []
    }
    return render_template('home.html', **context)

# profile
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        u = User.query.get(current_user.id)
        u.first_name = request.form.get('first_name')
        u.last_name = request.form.get('last_name')
        u.email = request.form.get('email')
        db.session.commit()
        flash('Profile updated successfully', 'info')
        return redirect(url_for('main.profile'))

    context = {
        'posts': Post.query.filter_by(user_id=current_user.id).order_by(Post.date_created.desc()).all()
    }
    return render_template('profile.html', **context)

# contact
@app.route('/contact')
def contact():
    return "This is the contact page."