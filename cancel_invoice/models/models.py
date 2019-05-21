# -*- coding: utf-8 -*-

from odoo import models, fields, api
class vendor_partail_invoicing(models.Model):
    _inherit ='account.invoice'

    @api.multi
    def cancelled_invoice(self):

        form_view = self.env.ref('account.invoice_supplier_form')
        new_id = self.env['account.invoice']
        vals = {
            'name': self.name,
            'reference': self.number,
            'partner_id': self.partner_id.id,
            'date_invoice':self.date_invoice,
            'vendor_bill_purchase_id':self.name,
             }

        view_id = new_id.create(vals)
        return {
        'name': "Cancel Invoice",
        'view_mode': 'form',
        'view_id': form_view.id,
        'res_id': view_id.id,
        'view_type': 'form',
        'res_model': 'account.invoice',
        'type': 'ir.actions.act_window',
        'target': 'new',

    }