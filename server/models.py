from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    reviews = db.relationship("Review" , back_populates='customer')

    items = association_proxy("reviews", "item")

    def __repr__(self):
        return f'<Customer {self.id}, {self.name}>'


class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)

    reviews = db.relationship("Review", back_populates="item")

    def __repr__(self):
        return f'<Item {self.id}, {self.name}, {self.price}>'


class Review(db.Model):
    __tablename__ ='reviews'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"))
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))

    customer = db.relationship ("Customer", back_populates= 'reviews')
    item = db.relationship ("Item", back_populates='reviews')


# -----------------------
# Schemas
# -----------------------
   

# class CustomerSchema(SQLAlchemyAutoSchema):

#     class Meta:
#         model = Customer
#         load_instance = True
#         include_relationships = True

#     id = fields.Int()
#     name = fields.Str()
#     reviews = fields.Nested("ReviewSchema", many=True, exclude=("customer","item"))

# class ItemSchema(SQLAlchemyAutoSchema):

#     class Meta:
#         model = Item
#         load_instance = True
#         include_relationships =True

#     id = fields.Int()
#     name = fields.Str()
#     price = fields.Float()
#     reviews = fields.Nested("ReviewSchema", many=True, exclude=("item","customer"))

# class ReviewSchema(SQLAlchemyAutoSchema):

#     class Meta:
#         model = Review
#         load_instance = True
#         include_relationships =True

#     id = fields.Int()
#     comment = fields.Str()
#     customer = fields.Nested("CustomerSchema", exclude=("reviews",))
#     item = fields.Nested("ItemSchema", exclude=("reviews",))    