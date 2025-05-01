from flask import Blueprint, render_template

opportunity_bp = Blueprint('opportunity', __name__, template_folder='templates/opportunity')

@opportunity_bp.route('/')
def opportunity():
    cards = [
        {"title": "Open Count", "value": "12"},
        {"title": "Open Value (Total)", "value": "Rp183.145,00"},
        {"title": "Open Value (Total)", "value": "Rp183.145,00"},
        {"title": "Forecasted Value", "value": "Rp0,00"},
        {"title": "Average Age", "value": "22"},
        {"title": "Closed - Won Value", "value": "Rp23.600,00"},
        {"title": "Closed - Won Value", "value": "Rp23.600,00"},
        {"title": "Closed - Won Value", "value": "Rp23.600,00"},
    ]
    return render_template('opportunity/opportunity.html', cards=cards)

@opportunity_bp.route('/form')
def opportunity_form():
    return render_template('opportunity/opportunity_form.html')