from odoo import models, fields, api
import uuid

class ResUsers(models.Model):
    _inherit = 'res.users'

    def generate_api_token(self):
        return str(uuid.uuid4())
