from odoo import models, fields, api

class Subject(models.Model):
    _name = 'sh.subject'
    _description = 'Subject'
    _order = 'code'

    code = fields.Char(string="Code",readonly=True,copy=False)
    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    active = fields.Boolean(string="Active", default=True)

    _sql_constraints = [
    ('unique_code', 'unique(code)', 'Code must be unique')
]

    career_id = fields.Many2one(
        'sh.career',
        string="Career"
    )

    school_id = fields.Many2one(
        'res.company',
        string="School",
        default=lambda self:self.env.company,
        readonly=True
    )

    @api.model
    def create(self, vals):
        if not vals.get('code'):
            vals['code'] = self.env['ir.sequence'].next_by_code('sh.subject')
        return super(Subject, self).create(vals)