from odoo import models, fields


class TeacherSubject(models.Model):
    _name = 'sh.teacher.subject'
    _description = 'Teacher Subject Assignment'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    teacher_id = fields.Many2one(
        'sh.teacher',
        string="Teacher",
        required=True,
        tracking=True
    )

    subject_id = fields.Many2one(
        'sh.subject',
        string="Subject",
        required=True,
        tracking=True
    )

    semester_id = fields.Many2one(
        'sh.semester',
        string="Semester",
        required=True,
        tracking=True
    )

    school_id = fields.Many2one(
        'res.company',
        string="School",
        default=lambda self: self.env.company,
        readonly=True
    )

    _sql_constraints = [
    (
        'unique_teacher_subject_semester',
        'unique(teacher_id, subject_id, semester_id)',
        'This assignment already exists'
    )
]