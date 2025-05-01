from flask import Blueprint, render_template, url_for

company_bp = Blueprint('company', __name__, template_folder='templates/company')

@company_bp.route('/')
def company():
    return render_template('company/company.html')

# Company form navigation items
def company_form_nav_items():
    return [
        {"name": "Basic Info", "endpoint": "company.company_basic_info", "link": url_for('company.company_basic_info')},
        {"name": "Address Info", "endpoint": "company.company_address_info", "link": url_for('company.company_address_info')},
        {"name": "Social Info", "endpoint": "company.company_social_info", "link": url_for('company.company_social_info')}
    ]

# Company form routes
@company_bp.route('/basic-info')
def company_basic_info():
    return render_template('company/company_form/company_basic_info.html',
                           company_form_nav_items=company_form_nav_items())

@company_bp.route('/address-info')
def company_address_info():
    return render_template('company/company_form/company_address_info.html',
                           company_form_nav_items=company_form_nav_items())

@company_bp.route('/social-info')
def company_social_info():
    return render_template('company/company_form/company_social_info.html',
                           company_form_nav_items=company_form_nav_items())

# Other company-related routes
@company_bp.route('/details')
def company_details():
    return render_template('company/company_details.html')

@company_bp.route('/activity')
def company_activity():
    return render_template('company/company_activity.html')

@company_bp.route('/opportunities')
def company_opportunities():
    return render_template('company/company_opportunity.html')

@company_bp.route('/history')
def company_history():
    return render_template('company/company_history.html')

@company_bp.route('/notes')
def company_notes():
    return render_template('company/company_notes.html')

@company_bp.route('/documents')
def company_documents():
    return render_template('company/company_documents.html')

@company_bp.route('/email')
def company_email():
    return render_template('company/company_email.html')

@company_bp.route('/call')
def company_call():
    return render_template('company/company_call.html')

@company_bp.route('/meeting')
def company_meeting():
    return render_template('company/company_meeting.html')