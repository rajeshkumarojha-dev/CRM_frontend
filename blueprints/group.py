from flask import Blueprint, render_template

group_bp = Blueprint('group', __name__, template_folder='templates/group')

@group_bp.route('/')
def group():
    return render_template('group/group.html')

@group_bp.route('/add')
def add_group():
    return render_template('group/add_group.html')

@group_bp.route('/details')
def group_details():
    return render_template('group/group_details.html')

@group_bp.route('/contacts')
def group_contacts():
    return render_template('group/group_contacts.html')

@group_bp.route('/activity')
def group_activity():
    return render_template('group/group_activity.html')

@group_bp.route('/opportunities')
def group_opportunities():
    return render_template('group/group_opportunities.html')

@group_bp.route('/history')
def group_history():
    return render_template('group/group_history.html')

@group_bp.route('/notes')
def group_notes():
    return render_template('group/group_notes.html')

@group_bp.route('/documents')
def group_documents():
    return render_template('group/group_documents.html')

@group_bp.route('/access')
def group_access():
    return render_template('group/group_access.html')