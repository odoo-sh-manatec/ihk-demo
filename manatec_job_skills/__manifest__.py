# -*- coding: utf-8 -*-
{
    'name': 'manaTec Job Skills',
    'version': '1.0',
    'category': 'HR',
    'summary': 'manaTec Job Skills Extension',
    'description': u"""manaTec Job Skills Extension""",
    'author': 'manaTec GmbH',
    'depends': ['hr', 'hr_recruitment', 'hr_skills'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_job_views.xml',
    ],
}
