from flask import Blueprint
import sqlalchemy as sa

from ..inventories_app import inventories_handlers
from ..sql_app.models import Inventory, Product, Location

bp = Blueprint("inventories", __name__, url_prefix="/inventories")


@bp.route("id_asc", methods=("GET", "POST"))
def id_asc():
    return inventories_handlers.show_all_inventories(sa.asc, Inventory.id)


@bp.route("id_desc", methods=("GET", "POST"))
def id_desc():
    return inventories_handlers.show_all_inventories(sa.desc, Inventory.id)


@bp.route("name_asc", methods=("GET", "POST"))
def name_asc():
    return inventories_handlers.show_all_inventories(sa.asc, Product.name)


@bp.route("name_desc", methods=("GET", "POST"))
def name_desc():
    return inventories_handlers.show_all_inventories(sa.desc, Product.name)


@bp.route("description_asc", methods=("GET", "POST"))
def description_asc():
    return inventories_handlers.show_all_inventories(sa.asc, Product.description)


@bp.route("description_desc", methods=("GET", "POST"))
def description_desc():
    return inventories_handlers.show_all_inventories(sa.desc, Product.description)


@bp.route("price_asc", methods=("GET", "POST"))
def price_asc():
    return inventories_handlers.show_all_inventories(sa.asc, Product.price)


@bp.route("price_desc", methods=("GET", "POST"))
def price_desc():
    return inventories_handlers.show_all_inventories(sa.desc, Product.price)


@bp.route("location_asc", methods=("GET", "POST"))
def location_asc():
    return inventories_handlers.show_all_inventories(sa.asc, Location.name)


@bp.route("location_desc", methods=("GET", "POST"))
def location_desc():
    return inventories_handlers.show_all_inventories(sa.desc, Location.name)


@bp.route("quantity_asc", methods=("GET", "POST"))
def quantity_asc():
    return inventories_handlers.show_all_inventories(sa.asc, Inventory.quantity)


@bp.route("quantity_desc", methods=("GET", "POST"))
def quantity_desc():
    return inventories_handlers.show_all_inventories(sa.desc, Inventory.quantity)
