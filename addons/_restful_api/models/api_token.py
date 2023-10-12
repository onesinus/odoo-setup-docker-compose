from odoo import models, fields, api

class ApiToken(models.Model):
    _name = 'api.token'

    user_id = fields.Many2one('res.users', string='User')
    api_token = fields.Char(string='API Token', readonly=True)

    def generate_token(self):
        self.ensure_one()
        user = self.user_id
        if user:
            self.api_token = user.generate_api_token()
