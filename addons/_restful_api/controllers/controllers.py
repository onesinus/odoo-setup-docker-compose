import json
# import base64

from io import BytesIO
from reportlab.pdfgen import canvas

from odoo import http
from odoo.http import request

from ..utils import api_auth

class CustomAPI(http.Controller):

    @http.route('/api/custom/model', auth='public', methods=['GET'], type='http', csrf=False, cors='*')
    @api_auth.custom_auth
    def get_custom_models(self):
        custom_models = request.env['custom.model'].sudo().search([])
        data = [{'id': rec.id, 'name': rec.name, 'description': rec.description} for rec in custom_models]
        return request.make_response(json.dumps(data), headers=[('Content-Type', 'application/json')])


    # @http.route('/api/custom/model/<int:model_id>/download', auth='user', methods=['GET'], type='http', csrf=False, cors='*')
    # def download_pdf(self, model_id):
    #     custom_model = request.env['custom.model'].sudo().browse(model_id)
    #     if custom_model:
    #         pdf_data = custom_model.pdf_field  # Gantilah 'pdf_field' dengan nama field yang sesuai di model Anda
    #         if pdf_data:
    #             pdf_binary = base64.b64decode(pdf_data)
    #             response = request.make_response(pdf_binary)
    #             response.headers.set('Content-Disposition', 'attachment; filename="document.pdf"')
    #             response.headers.set('Content-Type', 'application/pdf')
    #             return response
    #     return request.not_found()

    @http.route('/api/custom/model/<int:model_id>/download', auth='user', methods=['GET'], type='http', csrf=False, cors='*')
    @api_auth.custom_auth
    def download_pdf(self, model_id):
        # Buat PDF kosong
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        pdf.drawString(100, 750, "PDF Kosong")
        pdf.save()
        pdf_binary = buffer.getvalue()
        buffer.close()

        response = request.make_response(pdf_binary)
        response.headers.set('Content-Disposition', 'attachment; filename="empty.pdf"')
        response.headers.set('Content-Type', 'application/pdf')
        return response
