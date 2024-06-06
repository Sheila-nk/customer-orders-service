from marshmallow import Schema, fields, validate


class CreateAddOrderSchema(Schema):
    item_name = fields.Str(required=True, validate=validate.Length(min=2))
    num_of_items = fields.Integer(required=True, validate=validate.Range(min=1))
    phonenumber = fields.String(required=True, validate=validate.Regexp("^\+254\d{9}$"))


class CreateUpdateOrderSchema(Schema):
    item_name = fields.Str(validate=validate.Length(min=2))
    num_of_items = fields.Integer(validate=validate.Range(min=1))
    phonenumber = fields.String(validate=validate.Regexp("^\+254\d{9}$"))
