
from odoo import models, fields, api, exceptions, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    booking_start = fields.Datetime(string='Booking Start', required=False,
                                    help='Start date of hotel booking, flight departure, limousine rent, etc.')
    booking_end = fields.Datetime(string='Booking End', required=False,
                                  help='End date of hotel booking, flight arrival, limousine rent, etc.')
    booking_type = fields.Selection(related='product_id.booking_type', readonly=True, store=True)

    @api.onchange('booking_start', 'booking_end')
    def _compute_booking_qty(self):
        """
        Compute line quantity from hotel or limousine booking or renting dates
        if booking type is a hotel or a limousine. All other types, including null, are ignored.
        :rtype: None
        """
        for line in self.filtered(lambda l: l.booking_type in ['hotel', 'transport']):
            if line.booking_start and line.booking_end:
                line.product_uom_qty = (line.booking_end - line.booking_start).days
            else:
                line.product_uom_qty = 0.0

    @api.onchange('booking_type')
    def _onchange_booking_type(self):
        """
        Since related field implies the product is changed, check the product type and remove dates.
        :rtype: None
        """
        for line in self:
            if not line.booking_type:
                line.update({
                    'booking_start': False,
                    'booking_end': False,
                })

    @api.constrains('booking_end', 'booking_end', 'booking_type')
    def _validate_booking_dates(self):
        for line in self:
            if line.booking_type:
                if not line.booking_start or not line.booking_end:
                    raise exceptions.UserError(
                        _('Booking start and end dates must be set when the product has a booking type set.\n'
                          'Booking line: %s' % line.name))
                elif line.booking_start > line.booking_end:
                    raise exceptions.UserError(
                        _('Booking start date cannot be after booking end date.\n'
                          'Booking line: %s' % line.name))
