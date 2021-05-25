# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
import datetime
from odoo import models, api
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT, DEFAULT_SERVER_DATE_FORMAT


class WebsiteSupportTicketCompose(models.TransientModel):
    _inherit = "website.support.ticket.close"

    @api.multi
    def close_ticket(self):

        self.ticket_id.close_time = datetime.datetime.now()

        #Also set the date for gamification
        self.ticket_id.close_date = datetime.date.today()

        diff_time = datetime.datetime.strptime(
            self.ticket_id.close_time,
            DEFAULT_SERVER_DATETIME_FORMAT) - datetime.datetime.strptime(
                self.ticket_id.create_date, DEFAULT_SERVER_DATETIME_FORMAT)

        self.ticket_id.time_to_close = diff_time.seconds
        if diff_time.days > 0:
            self.ticket_id.time_to_close_days = diff_time.days
            self.ticket_id.time_to_close_hors = diff_time.days * 24
        else:
            self.ticket_id.time_to_close_hors = (diff_time.seconds / 3600)

        closed_state = self.env['ir.model.data'].sudo().get_object(
            'website_support', 'website_ticket_state_staff_closed')

        #We record state change manually since it would spam the chatter if every 'Staff Replied' and 'Customer Replied' gets recorded
        message = "<ul class=\"o_mail_thread_message_tracking\">\n<li>State:<span> " + self.ticket_id.state.name + " </span><b>-></b> " + closed_state.name + " </span></li></ul>"
        self.ticket_id.message_post(body=message,
                                    subject="Ticket Closed by Staff")

        self.ticket_id.close_comment = self.message
        self.ticket_id.closed_by_id = self.env.user.id
        self.ticket_id.state = closed_state.id

        #Auto send out survey
        setting_auto_send_survey = self.env['ir.values'].get_default(
            'website.support.settings', 'auto_send_survey')
        if setting_auto_send_survey:
            self.ticket_id.send_survey()

        #(BACK COMPATABILITY) Fail safe if no template is selected
        closed_state_mail_template = self.env['ir.model.data'].get_object(
            'website_support',
            'website_ticket_state_staff_closed').mail_template_id

        if closed_state_mail_template == False:
            closed_state_mail_template = self.env['ir.model.data'].sudo(
            ).get_object('website_support', 'support_ticket_closed')
            closed_state_mail_template.send_mail(self.ticket_id.id, True)
