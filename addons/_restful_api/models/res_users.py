from odoo import models, fields, api
import uuid

class ResUsers(models.Model):
    _inherit = 'res.users'

    api_token = fields.Char(string='API Token')

    def generate_api_token(self):
        api_token = str(uuid.uuid4())
        self.write({'api_token': api_token})
        return api_token
