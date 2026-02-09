{
    'name': 'IP Visitor Tracking',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Módulo para rastrear geolocalización de IPs vía ipgeolocation.io',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/ip_visitor_tracking_views.xml',
    ],
    'installable': True,
    'application': True,
    'icon': '/ip_visitor_tracking/static/description/icon.png',
}