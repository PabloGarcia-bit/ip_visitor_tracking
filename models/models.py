import requests
from odoo import models, fields, api
from odoo.exceptions import UserError

class IpVisitor(models.Model):
    _name = 'ip.visitor.tracking'
    _description = 'Registro de Geolocalización de Visitantes'

    api_key = fields.Char(string='API Key', required=True)
    ip_address = fields.Char(string='Dirección IP', readonly=True)
    country = fields.Char(string='País', readonly=True)
    city = fields.Char(string='Ciudad', readonly=True)
    latitude = fields.Float(string='Latitud', digits=(10, 7), readonly=True)
    longitude = fields.Float(string='Longitud', digits=(10, 7), readonly=True)
    isp = fields.Char(string='Proveedor (ISP)', readonly=True)
    organization = fields.Char(string='Organización', readonly=True)
    visit_time = fields.Datetime(string='Hora de la visita', readonly=True)

    def action_get_geolocation(self):
        """Lógica para consultar la API de ipgeolocation.io"""
        url = f"https://api.ipgeolocation.io/ipgeo?apiKey={self.api_key}"
        
        try:
            response = requests.get(url)
            data = response.json()
            
            if response.status_code == 200:
                self.write({
                    'ip_address': data.get('ip'),
                    'country': data.get('country_name'),
                    'city': data.get('city'),
                    'latitude': float(data.get('latitude')),
                    'longitude': float(data.get('longitude')),
                    'isp': data.get('isp'),
                    'organization': data.get('organization'),
                    'visit_time': fields.Datetime.now(),
                })
            else:
                raise UserError(f"Error de API: {data.get('message', 'Desconocido')}")
        except Exception as e:
            raise UserError(f"Error de conexión: {str(e)}")