from odoo import models, fields

class Subject(models.Model):
    _name = 'sh.subject'
    _description = 'Subject'

    code = fields.Char(string="Code")
    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    active = fields.Boolean(string="Active", default=True)

    career_id = fields.Many2one(
        'sh.career',
        string="Career"
    )