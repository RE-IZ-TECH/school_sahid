{
    'name': 'School',
    'version': '18.0.1.0',
    'author': 'Josué Sahid Hernández Díaz',
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_view.xml',
        'views/teacher_view.xml',
        'views/career_view.xml',
        'views/subject_view.xml',
        'views/school_menu.xml',
    ],
    'installable': True,
    'application': True,
    "license": "LGPL-3",
}