from marshmallow import fields, validate, validates, ValidationError
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from app import db
from app.models import Customer , Item , Review

class CustomerSchema(SQLAlchemyAutoSchema):
    id = fields.Int()
    name = fields.Str()
    reviews = fields.Nested("ReviewSchema", many=True, exclude=("customer","item"))

class ItemSchema(SQLAlchemyAutoSchema):
    id = fields.Int()
    name = fields.Str()
    price = fields.Float()
    reviews = fields.Nested("ReviewSchema", many=True, exclude=("item","customer"))

class ReviewSchema(SQLAlchemyAutoSchema):
    id = fields.Int()
    comment = fields.Str()
    customer = fields.Nested("CustomerSchema", exclude=("reviews","items"))
    item = fields.Nested("ItemSchema", exclude=("reviews",))     