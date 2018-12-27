# -*- coding: utf-8 -*-
{
    'name': 'Supply Chain Owatrans',
    'version': '1.0',
    'category': 'SUPLLY',
    'depends': [
        'purchase',
    ],
    'author': 'Aliou Samba WELE',
    'website': 'www.owatrans.sn',
    'license': 'AGPL-3',
    'data': [
        'views/purchase_views.xml',
        'data/supply_owatrans_mail_template.xml',
        'report/purchase_quotation_templates.xml',
        'report/purchase_reports.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'application': True,
}
