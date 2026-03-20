# -*- encoding: utf-8 -*-
from odoo import api, fields, models  #Ordenar import en orden alfabetico
# 2 espacios entre imports de Odoo y la clase y 1 espacio entre otros imports

class ShCareer(models.Model):
    _name = 'sh.career'
    _description = 'Career'
    _order = 'code'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    code = fields.Char(
        string="Code",
        readonly=True,
        copy=False
    )

    name = fields.Char(
        string="Name",
        tracking=True
    )

    description = fields.Text(
        string="Description"
    )

    active = fields.Boolean(
        string="Active",
        default=True
    )

    color = fields.Integer(
        string="Color"
    )

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

    # Constraints al final
    _sql_constraints=[
        ('unique_code', 'unique(code)', 'Code must be unique')
    ]

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
        return super().create(vals)
