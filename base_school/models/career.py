from odoo import models, fields

class Career(models.Model):
    _name = 'sh.career'
    _description = 'Career'

    code = fields.Char(string="Code")
    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    active = fields.Boolean(string="Active", default=True)

    subjects_ids = fields.One2many(
        'sh.subject',
        'career_id',
        string="Subjects"
    )