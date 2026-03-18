{
    'name': 'School Kardex',
    'version': '18.0.1.0.0',
    'summary': 'Academic kardex management',
    'depends': [
        'base_school',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/semester_views.xml',
        'views/teacher_subject_views.xml',
        'views/student_career_views.xml',
        'views/grade_views.xml',
        'report/report_kardex.xml',
        'report/report_kardex_template.xml',
    ],
    'installable': True,
    'application': False,
    "license": "LGPL-3",
}