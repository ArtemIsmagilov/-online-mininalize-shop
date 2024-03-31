from sqlalchemy.orm import Session, load_only
import sqlalchemy as sa
from typing import Callable

from ..sql_app.models import Inventory, Product, Location


def read_counts_inventories(session: Session):
    return session.scalar(sa.select(sa.func.count(Inventory.id)))


def find_counts_inventories(session: Session, q: str):
    return session.scalar(
        sa.select(sa.func.count(Inventory.id))
        .join(Inventory.product)
        .where(Product.name.like(f"%{q}%"))
    )


def read_some_inventories_by(
    session: Session, by_: sa.Column, sort_: Callable, from_: int, to_: int
):
    cte_query = (
        sa.select(
            sa.func.row_number().over(order_by=Inventory.id).label("current_id"),
            Inventory.id.label("inventory_id"),
            Product.name.label("product_name"),
            Product.description.label("product_description"),
            Product.price.label("product_price"),
            Location.name.label("location_name"),
            Inventory.quantity.label("inventory_quantity"),
        )
        .join(Inventory.product)
        .join(Inventory.location)
        .order_by(sort_(by_))
        .cte(name="cte_table")
    )
    query = sa.select(
        cte_query.c[
            "inventory_id",
            "product_name",
            "product_description",
            "product_price",
            "location_name",
            "inventory_quantity",
        ]
    ).where(sa.between(cte_query.c.current_id, from_, to_))

    return session.execute(query).all()


def find_some_inventories_by(
    session: Session, q: str, by_: sa.Column, sort_: Callable, from_: int, to_: int
):
    cte_query = (
        sa.select(
            sa.func.row_number().over(order_by=Inventory.id).label("current_id"),
            Inventory.id.label("inventory_id"),
            Product.name.label("product_name"),
            Product.description.label("product_description"),
            Product.price.label("product_price"),
            Location.name.label("location_name"),
            Inventory.quantity.label("inventory_quantity"),
        )
        .join(Inventory.product)
        .join(Inventory.location)
        .where(Product.name.like(f"%{q}%"))
        .order_by(sort_(by_))
        .cte(name="cte_table")
    )
    query = sa.select(
        cte_query.c[
            "inventory_id",
            "product_name",
            "product_description",
            "product_price",
            "location_name",
            "inventory_quantity",
        ]
    ).where(sa.between(cte_query.c.current_id, from_, to_))

    return session.execute(query).all()


def read_all_products(session: Session):
    return session.scalars(
        sa.select(Product).options(load_only(Product.name, Product.price))
    ).all()


def create_location(session: Session, location_name: str):
    session.add(Location(name=location_name))


def create_product(
    session: Session, product_name: str, product_description: str, product_price: float
):
    session.add(
        Product(name=product_name, description=product_description, price=product_price)
    )
