from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Student(models.Model):
    _name = 'sh.student'
    _description = 'Student'
    _order = 'code' 
    _inherit = ['mail.thread', 'mail.activity.mixin']     

    code = fields.Char(string="Code",readonly=True,copy=False)
    name = fields.Char(string="Name", Tracking=True)
    age = fields.Integer(string="Age")

    _sql_constraints = [
    ('unique_code', 'unique(code)', 'Code must be unique')
]

    school_id = fields.Many2one(
        'res.company',
        string="School",
        default=lambda self:self.env.company,
        readonly=True
    )

    partner_id = fields.Many2one(
        'res.partner',
        string = "Contact",
        domain = [('is_company','=',False)]
    )

    @api.constrains('age')
    def _check_age(self):
        for record in self:
            if record.age > 99:
                raise ValidationError("Invalid age, age must be less than 99")


    @api.model
    def create(self, vals):
        if not vals.get('code'):
            vals['code'] = self.env['ir.sequence'].next_by_code('sh.student')
        return super(Student, self).create(vals)