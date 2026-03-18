from odoo import models, fields, api

class Grade(models.Model):
    _name='sh.grade'
    _description='Grade'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    student_id = fields.Many2one(
        'sh.student',
        string='Student',
        required=True,
        tracking=True
    )

    career_id = fields.Many2one(
        'sh.career',
        string='Career',
        required=True,
        tracking=True
    )

    subject_id = fields.Many2one(
        'sh.subject',
        string='Subject',
        required=True,
        tracking=True
    )

    teacher_id = fields.Many2one(
        'sh.teacher',
        string = 'Teacher',
        required = True,
        tracking = True
    )

    semester_id = fields.Many2one (
        'sh.semester',
        string = 'Semester',
        required = True,
        tracking = True
    )

    grade = fields.Float(
        string=("Input the grade")
    )

    approved = fields.Boolean(
        string = "Approved",
        compute="_compute_approved",
        store=True
    )

    school_id = fields.Many2one (
        'res.company',
        string='School',
        default=lambda self: self.env.company,
        readonly=True
    )

    @api.depends('grade')
    def _compute_approved(self):
        for record in self:
            if record.grade >= 6:
                record.approved = True
            else:
                record.approved = False

    _sql_constraints = [
        (
            'unique_student_subject_semester',
            'unique(student_id, subject_id, semester_id)',
            'The student already has a grade for this subject in this semester'
        )
    ]