from odoo import models, fields


class StudentCareer(models.Model):
    _name = 'sh.student.career'
    _description = 'Student Career'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    student_id = fields.Many2one(
        'sh.student',
        string="Student",
        required=True,
        tracking=True
    )

    career_id = fields.Many2one(
        'sh.career',
        string="Career",
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
        'unique_student_career_semester',
        'unique(student_id, career_id, semester_id)',
        'This student is already registered in this career for this semester'
    )
]