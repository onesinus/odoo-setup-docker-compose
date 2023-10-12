from odoo.http import route, request
from odoo.exceptions import AccessDenied

def custom_auth(func):
    def wrapped(*args, **kwargs):
        api_token = request.httprequest.headers.get('Authorization')
        if not api_token:
            raise AccessDenied('You are not authorized to access this page')

        user = request.env['res.users'].sudo().search([('api_token', '=', api_token)])
        if user:
            return func(*args, **kwargs)
        else:
            raise AccessDenied('Unauthorized')
    return wrapped
