from flask import render_template, url_for
from werkzeug.utils import redirect
from app.blueprints.blog.models import Post
from .import bp as app
from flask import flash, request
from flask_login import current_user

@app.route('/post/<int:id>')
def get_post(id):
    context = {
        'p': Post.query.get(id)
    }
    return render_template('blog-single.html', **context)

@app.route('/post/create', methods=['POST'])
def create_post():
    Post(body=request.form.get('body'), user_id=current_user.id).save()
    flash('Post created successfully', 'primary')
    return redirect(url_for('main.home'))
