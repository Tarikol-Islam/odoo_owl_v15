from odoo import models, fields, api


class Vehicle(models.Model):
    _name = "vehicle"
    _rec_name = 'car_name'

    car_name = fields.Char()
    car_description = fields.Text()
    car_brand = fields.Char()
    car_model = fields.Char()
    model_year = fields.Char()
    previous_model = fields.Many2one('vehicle')
    is_fwd = fields.Boolean()
