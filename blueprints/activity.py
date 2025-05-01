from flask import Blueprint, render_template

activity_bp = Blueprint('activity', __name__, template_folder='templates/activity')

@activity_bp.route('/')
def activity():
    return render_template('activity/activity.html')