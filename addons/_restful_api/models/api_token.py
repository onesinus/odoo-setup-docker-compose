from odoo import models, fields, api

class ApiToken(models.Model):
    _name = 'api.token'

    user_id = fields.Many2one('res.users', string='User')
    api_token = fields.Char(string='API Token', readonly=True, default=lambda self: self._generate_token())

    def _generate_token(self):
        return self.user_id.generate_api_token()
