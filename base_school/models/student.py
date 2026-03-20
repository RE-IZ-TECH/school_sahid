# -*- encoding: utf-8 -*-
from odoo import api, fields, models  #Ordernar import en orden alfabetico
from odoo.exceptions import ValidationError
# 2 espacios entre imports de Odoo y la clase y 1 espacio entre otros imports


class ShStudent(models.Model):
    _name = 'sh.student'
    _description = 'Student'
    _order = 'code' 
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # Ubicación ideal para comentarios (arriba del bloque de codigo)
    code = fields.Char( 
        string="Code",
        readonly=True,
        copy=False,
        help = "This space is for the student's code"
    )

    name=fields.Char(
        string="Name", 
        Tracking=True,
        help = "This space is for the student's name"
    )
    age=fields.Integer(
        string="Age",
        help = "This space is for the student's age"
    )

    school_id=fields.Many2one(
        'res.company',
        string="School",
        default=lambda self:self.env.company,
        readonly=True
    )

    partner_id=fields.Many2one(
        'res.partner',
        string = "Contact",
        domain = [('is_company','=',False)]
    )

    # Historial academico
    grade_ids=fields.One2many(
        'sh.grade',
        'student_id',
        string="Grades",
        help="Academic record of the student"
    )

    # Promedio de todas las calificaciones registradas del alumno
    average_grade=fields.Float(
        string="Average Grade",
        compute="_compute_average_grade",
        store=True,
        help="Average of the students"
    )

    # De preferencia poner los constraints al final
    _sql_constraints=[
        ('unique_code', 'unique(code)', 'Code must be unique')
    ]

    @api.constrains('age')
    def _check_age(self):
        for record in self:
            if record.age > 99:
                raise ValidationError("Invalid age, age must be less than 99")# Sin espacios despues de terminar la línea

    # Método computado para promedio
    @api.depends('grade_ids.grade')
    def _compute_average_grade(self):
        for record in self:
            if record.grade_ids:
                total = sum(record.grade_ids.mapped('grade'))
                record.average_grade = total / len(record.grade_ids)
            else:
                record.average_grade = 0.0

    @api.model
    def create(self, vals):
        if not vals.get('code'):
            vals['code'] = self.env['ir.sequence'].next_by_code('sh.student')
        return super(ShStudent, self).create(vals)

    # Una linea vacía al final de cada archivo .py
