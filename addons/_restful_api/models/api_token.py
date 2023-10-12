from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ApiToken(models.Model):
    _name = 'api.token'

    user_id = fields.Many2one('res.users', string='User')
    api_token = fields.Char(string='API Token', readonly=True, default=lambda self: self._generate_token())

    def _generate_token(self):
        return self.user_id.generate_api_token()

    def regenerate_token(self):
        self.api_token = self.user_id.generate_api_token()

    @api.constrains('user_id')
    def _check_unique_user_id(self):
        for token in self:
            existing_tokens = self.env['api.token'].search([('user_id', '=', token.user_id.id)])
            if len(existing_tokens) > 1:
                raise ValidationError('Each user can only have one API token.')
