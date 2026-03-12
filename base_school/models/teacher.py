from odoo import models, fields

class Teacher(models.Model):
    _name = 'sh.teacher'
    _description = 'Teacher'

    code = fields.Char(string="Code")
    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")