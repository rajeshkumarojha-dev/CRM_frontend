from flask import Blueprint, render_template, url_for

contact_bp = Blueprint('contact', __name__, template_folder='templates/contact')

# Contact main page
@contact_bp.route('/')
def contact():
    contacts = [
        # Your contacts list remains the same
        {
            'name': 'Paresh Mohanty',
            'company': 'EA Tech Corporation',
            'email': 'paresh@eatechpvtltd.com',
            'phone': '+91 1234567890',
            'role': 'UI/UX Designer',
            'department': 'Information Technology',
            'website': 'www.google.com',
            'country': 'India',
            'status': 'Active'
        },
        # ... other contacts
    ]
    action_buttons = [
        {"type": "button", "label": "Filter", "icon": "fi fi-rr-filter", "class": "btn-outline-secondary", "url": "#"},
        {"type": "button", "label": "Duplicate", "icon": "fi fi-rr-copy", "class": "btn-outline-secondary", "url": "#"},
        {"type": "button", "label": "Map", "icon": "fi fi-rr-marker", "class": "btn-outline-secondary", "url": "#"},
        {"type": "button", "label": "Attach", "icon": "fi fi-rr-clip", "class": "btn-outline-secondary", "url": "#"},

        {
            "type": "dropdown", "label": "Export", "icon": "fi fi-rr-download", "class": "btn-outline-secondary",
            "dropdown_items": [
                {"label": "Export as PDF", "url": "#"},
                {"label": "Export as CSV", "url": "#"},
                {"label": "Export as Excel", "url": "#"}
            ]
        },

        {
            "type": "link", "label": "Add Contact", "icon": "fa-solid fa-plus",
            "class": "button-bg filter-button text-white", "url": url_for('contact.contact_basic_info')
        }
    ]
    return render_template('contact/contact.html', contacts=contacts,action_buttons=action_buttons)

# Contact form navigation items
def contact_form_nav_items():
    return [
        {"name": "Basic Info", "endpoint": "contact.contact_basic_info", "link": url_for('contact.contact_basic_info')},
        {"name": "Address Info", "endpoint": "contact.contact_address_info", "link": url_for('contact.contact_address_info')},
        {"name": "Social Info", "endpoint": "contact.contact_social_info", "link": url_for('contact.contact_social_info')}
    ]

# Contact form routes
@contact_bp.route('/basic-info')
def contact_basic_info():
    return render_template('contact/contact_form/contact_basic_info.html',
                           contact_form_nav_items=contact_form_nav_items())

@contact_bp.route('/address-info')
def contact_address_info():
    return render_template('contact/contact_form/contact_address_info.html',
                           contact_form_nav_items=contact_form_nav_items())

@contact_bp.route('/social-info')
def contact_social_info():
    return render_template('contact/contact_form/contact_social_info.html',
                           contact_form_nav_items=contact_form_nav_items())

# Other contact-related routes
@contact_bp.route('/details')
def contact_details():
    return render_template('contact/contact_detail.html')

@contact_bp.route('/activity')
def contact_activity():
    return render_template('contact/contact_activity.html')

@contact_bp.route('/opportunity')
def contact_opportunity():
    return render_template('contact/contact_opportunity.html')

@contact_bp.route('/history')
def contact_history():
    return render_template('contact/contact_history.html')

@contact_bp.route('/notes')
def contact_notes():
    return render_template('contact/contact_notes.html')

@contact_bp.route('/documents')
def contact_document():
    return render_template('contact/contact_document.html')

@contact_bp.route('/group')
def contact_group():
    return render_template('contact/contact_group.html')

@contact_bp.route('/company')
def contact_company():
    return render_template('contact/contact_company.html')