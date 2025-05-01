
from flask import Flask, render_template
from blueprints import register_blueprints


app = Flask(__name__)
register_blueprints(app)


# Home route
@app.route('/')
def home():
    return render_template('dashboard/dashboard.html')

# Sidebar nav icons context processor
@app.context_processor
def inject_nav_items():
    nav_items = [
        {"name": "Dashboard", "endpoint": "home", "icon": "fi fi-rr-apps", "fixed": True},
        {"name": "Contacts", "endpoint": "contact.contact", "icon": "fi fi-rr-user"},
        {"name": "Group", "endpoint": "group.group", "icon": "fi fi-rr-users-alt"},
        {"name": "Companies", "endpoint": "company.company", "icon": "fi fi-rr-city"},
        {"name": "Calendar", "endpoint": None, "icon": "fa-solid fa-calendar"},
        {"name": "Activity", "endpoint": "activity.activity", "icon": "fi fi-rr-calendar-pen"},
        {"name": "History List", "endpoint": "history.history", "icon": "fa-solid fa-history"},
        {"name": "Opportunities", "endpoint": "opportunity.opportunity", "icon": "fi fi-rr-lightbulb-on"},
        {"name": "Products", "endpoint": "products.products", "icon": "fi fi-rr-box-open-full"},
        {"name": "Insight", "endpoint": None, "icon": "fa-solid fa-eye"},
        {"name": "Marketing", "endpoint": None, "icon": "fa-solid fa-bullhorn"},
        {"name": "Email", "endpoint": None, "icon": "fa-solid fa-envelope"},
        {"name": "Reports", "endpoint": None, "icon": "fa-solid fa-chart-bar"},
        {"name": "Help & Support", "endpoint": None, "icon": "fa-solid fa-headset"},
        {"name": "Setting", "endpoint": None, "icon": "fa-solid fa-cog"},
    ]
    return dict(nav_items=nav_items)

# Upper header nav icons context processor
@app.context_processor
def inject_icons():
    icons = [
        {"class": "fa-solid fa-moon toggle-theme", "link": "#", "title": "Toggle Theme"},
        {"class": "fi fi-rr-call-outgoing", "link": "#", "title": "Phone"},
        {"class": "fi fi-rr-calendar-day", "link": "#", "title": "Calendar"},
        {"class": "fi fi-rr-envelope", "link": "#", "title": "Email"},
        {"class": "fa-solid fa-plus", "link": "#", "title": "Add New"},
        {"class": "fi fi-rr-time-past", "link": "#", "title": "Refresh"},
        {"class": "fi fi-rr-calendar-plus", "link": "#", "title": "Edit"},
        {"class": "fi fi-rr-question", "link": "#", "title": "Help"},
        {"class": "fi fi-rr-bell", "link": "#", "title": "Notifications"},
        {"class": "fa-solid fa-user-circle", "link": "#", "title": "Profile"},
    ]
    return dict(icons=icons)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)