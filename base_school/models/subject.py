from odoo import models, fields, api


class ShSubject(models.Model):
    _name = 'sh.subject'
    _description = 'Subject'
    _order = 'code'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    code = fields.Char(string="Code",readonly=True,copy=False)
    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    active = fields.Boolean(string="Active", default=True)

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

    _sql_constraints = [
    ('unique_code', 'unique(code)', 'Code must be unique')
    ]

    @api.model
    def create(self, vals):
        if not vals.get('code'):
            vals['code'] = self.env['ir.sequence'].next_by_code('sh.subject')
        return super(ShSubject, self).create(vals)
