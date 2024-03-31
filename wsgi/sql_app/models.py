import sqlalchemy as sa
from sqlalchemy.orm import mapped_column, relationship, Mapped, column_property

from ..sql_app.databse import Base


class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(sa.String(30))
    last_name: Mapped[str] = mapped_column(sa.String(30))

    def __repr__(self) -> str:
        return f"User(id={self.id}, first_name={self.first_name}, last_name={self.last_name})"


class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(sa.String(50))
    description: Mapped[str] = mapped_column(sa.Text)
    kop: Mapped[int] = mapped_column(sa.Integer)

    inventories: Mapped[list["Inventory"]] = relationship(back_populates="product")

    price: Mapped[float] = column_property(sa.func.round(kop / 100, 2))

    def __repr__(self) -> str:
        return f"Product(id={self.id}, name={self.name}, description={self.description}, price={self.price})"


class Location(Base):
    __tablename__ = "locations"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(sa.String(50))

    inventories: Mapped[list["Inventory"]] = relationship(back_populates="location")

    def __repr__(self) -> str:
        return f"Location(id={self.id=}, name={self.name})"


class Inventory(Base):
    __tablename__ = "inventories"
    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(sa.ForeignKey("products.id"))
    location_id: Mapped[int] = mapped_column(sa.ForeignKey("locations.id"))
    quantity: Mapped[int]

    product: Mapped["Product"] = relationship(back_populates="inventories")
    location: Mapped["Location"] = relationship(back_populates="inventories")

    def __repr__(self) -> str:
        return f"Inventory(id={self.id}, product_id={self.product_id}, location_id={self.location_id}, quantity={self.quantity})"
