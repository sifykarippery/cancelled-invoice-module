# -*- coding: utf-8 -*-

from odoo import models, fields, api

class vendor_partail_invoicing(models.Model):
    _inherit= 'account.invoice'
    cancel_invoice = fields.Boolean(string="cancel invoice")
    new_state = fields.Selection([
        ('head_section', 'Head_section'),
        ], string='Status', index=True,
        track_visibility='onchange', copy=False,
        )


    @api.one
    def update_quantity(self):
        if self.cancel_invoice == 1:
            self.write({
            'new_state': 'head_section',
            })





    @api.multi
    def write(self ,vals):
        for line in self:
            qty = 0.0
            for line_inv in line.invoice_line_ids:
                if line_inv.invoice_id.state not in ['cancel']:
                    if line_inv.invoice_id.new_state == 'head_section':
                        qty -= line_inv.uom_id._compute_quantity(line_inv.quantity,line.uom)
            line.quantity = qty
            vals['quantity']=line.quantity
        return super(AccountInvoice,self).write(vals)






    # @api.multi
    # def cancelled_invoice(self):
    #
    #     form_view = self.env.ref('account.invoice_supplier_form')
    #     new_id = self.env['account.invoice']
    #     vals = {
    #         'name': self.name,
    #         'reference': self.number,
    #         'partner_id': self.partner_id.id,
    #         'date_invoice':self.date_invoice,
    #         'vendor_bill_purchase_id':self.name,
    #          }
    #
    #     view_id = new_id.create(vals)
    #     return {
    #     'name': "Cancel Invoice",
    #     'view_mode': 'form',
    #     'view_id': form_view.id,
    #     'res_id': view_id.id,
    #     'view_type': 'form',
    #     'res_model': 'account.invoice',
    #     'type': 'ir.actions.act_window',
    #     'target': 'new',
    #
    # }