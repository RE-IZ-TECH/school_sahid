from odoo import models, fields


class Semester(models.Model):
    _name = 'sh.semester'
    _description = 'Semester'
    _order = 'code'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    code = fields.Char(string="Code",required=True,tracking=True)
    name = fields.Char(string="Name",required=True,tracking=True)
    date_start = fields.Date(string="Start Date")
    date_end = fields.Date(string="End Date")
    active = fields.Boolean(string="Active",default=True)
    school_id = fields.Many2one('res.company',string="School",default=lambda self: self.env.company,readonly=True)

    _sql_constraints = [
    ('unique_code', 'unique(code)', 'Code must be unique')
]