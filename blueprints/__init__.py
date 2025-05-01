import os
import importlib
from flask import Flask

def register_blueprints(app: Flask, base_path='blueprints'):
    for filename in os.listdir(base_path):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]  
            module_path = f"{base_path.replace('/', '.')}.{module_name}"

            module = importlib.import_module(module_path)

            blueprint = getattr(module, f"{module_name}_bp", None)

            if blueprint:
                app.register_blueprint(blueprint, url_prefix=f'/{module_name}')