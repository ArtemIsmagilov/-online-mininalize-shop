from flask import render_template

from .sql_app.databse import LocalSession
from .sql_app import crud


def show_home():
    with LocalSession.begin() as session:
        all_products = crud.read_all_products(session)
        result = render_template("index.html", products=all_products)
    return result
