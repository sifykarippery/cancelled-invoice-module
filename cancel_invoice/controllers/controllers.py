# -*- coding: utf-8 -*-
from odoo import http

# class CancelInvoice(http.Controller):
#     @http.route('/cancel_invoice/cancel_invoice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cancel_invoice/cancel_invoice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cancel_invoice.listing', {
#             'root': '/cancel_invoice/cancel_invoice',
#             'objects': http.request.env['cancel_invoice.cancel_invoice'].search([]),
#         })

#     @http.route('/cancel_invoice/cancel_invoice/objects/<model("cancel_invoice.cancel_invoice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cancel_invoice.object', {
#             'object': obj
#         })