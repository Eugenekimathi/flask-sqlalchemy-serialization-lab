# from marshmallow import fields
# from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

# from app import db
# from models import *

# class CustomerSchema(SQLAlchemyAutoSchema):

#     class Meta:
#         model = Customer
#         load_instance = True

#     id = fields.Int()
#     name = fields.Str()
#     reviews = fields.Nested("ReviewSchema", many=True, exclude=("customer","item"))

# class ItemSchema(SQLAlchemyAutoSchema):

#     class Meta:
#         model = Item
#         load_instance = True

#     id = fields.Int()
#     name = fields.Str()
#     price = fields.Float()
#     reviews = fields.Nested("ReviewSchema", many=True, exclude=("item","customer"))

# class ReviewSchema(SQLAlchemyAutoSchema):

#     class Meta:
#         model = Review
#         load_instance = True

#     id = fields.Int()
#     comment = fields.Str()
#     customer = fields.Nested("CustomerSchema", exclude=("reviews","items"))
#     item = fields.Nested("ItemSchema", exclude=("reviews",))     