from flask import Blueprint, render_template

products_bp = Blueprint('products', __name__, template_folder='templates/products')

@products_bp.route('/')
def products():
    products_buttons = [
        {"text": "Filter", "icon": "fi fi-rr-filter"},
        {"text": "03/02/2025 - 03/03/2025", "icon": "fi fi-rr-calendar-lines"},
        {"text": "Attach", "icon": "fi fi-rr-clip"},
        {"text": "Export", "icon": "fi fi-rr-download", "dropdown": True},
        {"text": "Add Products", "icon": "fa-solid fa-plus", "primary": True}
    ]
    product_table_headers = [
        {"name": "", "checkbox": True},
        {"name": ""},
        {"name": "Product Name"},
        {"name": "Items"},
        {"name": "Quantity"},
        {"name": "Price"},
        {"name": "Adjusted Price"},
        {"name": "Discount"},
        {"name": "Sub Total"},
        {"name": "Created Date"},
        {"name": "Status"},
        {"name": ""}
    ]
    return render_template('products/product.html',
                           products_buttons=products_buttons,
                           product_table_headers=product_table_headers)

@products_bp.route('/add')
def add_products():
    return render_template('products/add_product_form.html')