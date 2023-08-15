from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from app import db
from app.models import Team
from app.main import main
from .layoutUtils import *

@main.route('/', methods=['GET', 'POST'])
def index():
    #form = PostForm()
    team = Team.query.order_by(Team.timestamp.desc()).all()
    #return render_template('index.html', form=form, team=team)
    mc = set_menu("home") #to highlight menu option
    #return render_template('home/index.html', mc=mc)
    return render_template('home/index.html', team=team, mc=mc)


@main.route('/about', methods=('GET', 'POST'))
def about():

    mc = set_menu("about")
    return render_template('home/about.html', mc=mc)


@main.route('/privacy-notice',methods=('GET', 'POST'))
def privacy():

    mc = set_menu("")
    return render_template('home/privacy-notice.html', mc=mc)


@main.route('/terms-of-service',methods=('GET', 'POST'))
def termsofservice():
    mc = set_menu("")
    return render_template('home/terms-of-service.html', mc=mc)


#These files are usually in root, but for Flask projects must
#be in the static folder
def static_from_root():
    return send_from_directory(current_app.static_folder, request.path[1:])

