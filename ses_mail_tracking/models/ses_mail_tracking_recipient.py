# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SesMailTrackingRecipient(models.Model):
    _name = 'ses.mail.tracking.recipient'
    _description = 'SES Mail Tracking Recipient'

    ses_mail_tracking_id = fields.Many2one(
        comodel_name='ses.mail.tracking',
        string='SES Mail Tracking ID'
    )
    recipient = fields.Char(
        string='Recipient'
    )
