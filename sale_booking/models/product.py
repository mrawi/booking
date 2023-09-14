
from odoo import models, fields, api, exceptions, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    booking_type = fields.Selection(string='Booking Type',
                                    selection=[('ticket', 'Ticket'),
                                               ('hotel', 'Hotel'),
                                               ('transport', 'Transport')],
                                    required=False)

    @api.onchange('booking_type')
    def _onchange_booking_type(self):
        for template in self:
            if template.sales_count > 0:
                raise exceptions.ValidationError(
                    _('You cannot change the booking type of a product that has already been sold.'))
