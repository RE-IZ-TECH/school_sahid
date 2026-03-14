from odoo import models, fields, api

class Career(models.Model):
    _name = 'sh.career'
    _description = 'Career'
    _order = 'code'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    code = fields.Char(string="Code",readonly=True,copy=False)
    name = fields.Char(string="Name", Tracking=True)
    description = fields.Text(string="Description")
    active = fields.Boolean(string="Active", default=True)
    color = fields.Integer(string="Color")

    _sql_constraints = [
    ('unique_code', 'unique(code)', 'Code must be unique')
]

    subjects_ids = fields.One2many(
        'sh.subject',
        'career_id',
        string="Subjects"
    )

    school_id = fields.Many2one(
        'res.company',
        string="School",
        default=lambda self:self.env.company,
        readonly=True
    )

    subjects_count = fields.Integer(
    string="Subjects Count",
    compute="_compute_subjects_count"
    )

    def _compute_subjects_count(self):
        for record in self:
            record.subjects_count = len(record.subjects_ids)

    def action_view_subjects(self):
        return {
        'type': 'ir.actions.act_window',
        'name': 'Subjects',
        'res_model': 'sh.subject',
        'view_mode': 'list,form',
        'domain': [('career_id', '=', self.id)],
    }

    @api.model
    def create(self, vals):
        if not vals.get('code'):
            vals['code'] = self.env['ir.sequence'].next_by_code('sh.career')
        return super(Career, self).create(vals)