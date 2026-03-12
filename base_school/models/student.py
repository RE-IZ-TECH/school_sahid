from odoo import models, fields

class Student(models.Model):
    _name = 'sh.student'
    _description = 'Student'

    code = fields.Char(string="Code")
    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")