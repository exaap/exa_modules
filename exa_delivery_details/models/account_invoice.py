# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import datetime
from odoo import models, fields, api
import unicodedata
import logging


class DeliveryAddress(models.Model):
    _inherit = 'account.invoice'

    def show_delivery_address(self):
        partner_id = self.partner_id.id
        delivery_addresses = self.env['res.partner'].search([
            ('parent_id', '=', partner_id), ('type', '=', 'delivery')
        ])
        if delivery_addresses and len(delivery_addresses) == 1:
            return True
        if len(delivery_addresses) > 1 and not self.partner_shipping_id:
            return False
        if len(
                delivery_addresses
        ) > 1 and not self.invoice_delivery_address_same_partner_address():
            return True
        return False

    def invoice_delivery_address_same_partner_address(self):
        partner_address = self.partner_id.street
        invoice_delivery_addresses = self.partner_shipping_id.street
        if partner_address == invoice_delivery_addresses:
            return True
        return False

    def get_childs(self):
        childs = {}
        partner_id = self.partner_id.id
        # we get the childs of the partner
        child_ids = self.env['res.partner'].search([('parent_id', '=',
                                                     partner_id),
                                                    ('type', '=', 'delivery')])
        if child_ids:
            if len(child_ids) == 1:
                childs = child_ids
            elif len(child_ids) > 1:
                if self.get_invoice_delivery_address_if_diff_partner_address():
                    childs = self.get_invoice_delivery_address_if_diff_partner_address(
                    )
        return childs

    def get_invoice_delivery_address_if_diff_partner_address(self):
        partner_address = self.partner_id.street
        invoice_delivery_addresses = self.partner_shipping_id.street
        if partner_address != invoice_delivery_addresses:
            return self.partner_shipping_id
        return False

    def street(self):
        if self.show_delivery_address():
            if self.get_childs():
                for child in self.get_childs():
                    if child.street:
                        return child.street

    def street2(self):
        if self.show_delivery_address():
            if self.get_childs():
                for child in self.get_childs():
                    if child.street2:
                        return child.street2

    def district(self):
        if self.show_delivery_address():
            if self.get_childs():
                for child in self.get_childs():
                    if child.district_id:
                        return child.district_id.name

    def zip(self):
        if self.show_delivery_address():
            if self.get_childs():
                for child in self.get_childs():
                    if child.zip:
                        return child.zip

    def city(self):
        if self.show_delivery_address():
            if self.get_childs():
                for child in self.get_childs():
                    if child.city:
                        return child.city

    def state_id(self):
        if self.show_delivery_address():
            if self.get_childs():
                for child in self.get_childs():
                    if child.state_id:
                        return child.state_id.name

    def zone_id(self):
        if self.show_delivery_address():
            if self.get_childs():
                for child in self.get_childs():
                    if child.zone_id:
                        return child.zone_id.name

    def has_zone(self):
        if self.get_childs():
            for child in self.get_childs():
                if child.zone_id:
                    return True
        return False
