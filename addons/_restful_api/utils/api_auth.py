from odoo.http import route, request
from odoo.exceptions import AccessDenied

def check_token(func):
    def wrapped(*args, **kwargs):
        api_token = request.httprequest.headers.get('Authorization')
        if not api_token:
            raise AccessDenied('You are not authorized to access this page')

        api_token = request.env['api.token'].sudo().search([('api_token', '=', api_token)])
        if api_token:
            kwargs['user'] = api_token.user_id 
            return func(*args, **kwargs)
        else:
            raise AccessDenied('Unauthorized')
    return wrapped
