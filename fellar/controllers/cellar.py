from fellar.models import FacebookGroupPost, FacebookGroup
from flask import Blueprint, render_template
from glask import redirect_for

app = Blueprint('cellar', __name__)


@app.route('/')
def index():
    return redirect_for('.group_list')


@app.route('/group/')
def group_list():
    groups = FacebookGroup.query.all()
    return render_template('cellar/group/list.html', groups=groups)


@app.route('/group/<int:id>/post')
def post_list(id):
    group = FacebookGroup.query.get_or_404(id)
    posts = FacebookGroupPost.query.with_parent(group).all()
    return render_template('cellar/post/list.html', group=group, posts=posts)
