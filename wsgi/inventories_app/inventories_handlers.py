import sqlalchemy as sa, re
from typing import Callable
from flask import request, flash, current_app, render_template
from flask_paginate import get_page_args, Pagination

from ..sql_app.databse import LocalSession
from ..sql_app import crud


def get_css_framework():
    css = request.args.get("bs")
    if css:
        return css

    return current_app.config.get("CSS_FRAMEWORK", "bootstrap5")


def get_link_size():
    return current_app.config.get("LINK_SIZE", "")


def get_alignment():
    return current_app.config.get("LINK_ALIGNMENT", "")


def show_single_page_or_not():
    return current_app.config.get("SHOW_SINGLE_PAGE", False)


def get_pagination(**kwargs):
    kwargs.setdefault("record_name", "records")
    return Pagination(
        css_framework=get_css_framework(),
        link_size=get_link_size(),
        alignment=get_alignment(),
        show_single_page=show_single_page_or_not(),
        prev_rel="prev",
        next_rel="next prefetch",
        **kwargs,
    )


def load_form_inventories(session: sa.orm.Session):
    if request.form.get("location_name"):
        location_name = request.form["location_name"]
        crud.create_location(session, location_name)
        flash("Вы успешно создали локацию", "success")
    else:
        product_name = request.form["product_name"]
        product_description = request.form["product_description"]
        product_price = request.form["product_price"]
        crud.create_product(
            session, product_name, product_description, float(product_price)
        )
        flash("Вы успешно создали продукт", "success")


def show_all_inventories(sorting: Callable, by_column: sa.Column):
    with LocalSession.begin() as session:
        if request.method == "POST":
            load_form_inventories(session)
        q = request.args.get("q", "").strip()
        if q:
            search = True
            total = (
                crud.find_counts_inventories(session, q)
                if re.match(r"[а-яА-Я0-9 ]", q)
                else 0
            )

        else:
            search = False
            total = crud.read_counts_inventories(session)

        page, per_page, offset = get_page_args()

        pagination = get_pagination(
            page=page,
            per_page=per_page,
            total=total,
            record_name="inventories",
        )

        if search:
            all_inventories = crud.find_some_inventories_by(
                session, q, by_column, sorting, offset + 1, per_page + offset
            )
        else:
            all_inventories = crud.read_some_inventories_by(
                session, by_column, sorting, offset + 1, per_page + offset
            )

        result = render_template(
            "inventories.html",
            inventories=all_inventories,
            pagination=pagination,
            q=q,
        )

    return result
