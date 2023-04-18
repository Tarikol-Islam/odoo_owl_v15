{
    'name': 'Odoo Owl V15',
    'version': '15.0.0.1',
    'category': '',
    'summary': '',
    'author': 'Tarikol-Islam',
    'company': '',
    'website': "",
    'live_test_url': "",
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/vehicle_view.xml',
        "views/template.xml",
    ],
    "assets": {
        "web.assets_common": [
            "odoo_owl_v15/static/src/js/popup.js",
            # "odoo_owl_v15/views/template.xml",
        ]
    },
    'images': [],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}