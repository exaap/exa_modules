# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.depends("firstname", "othernames", "lastname", "lastname2")
    def _compute_name(self):
        for partner in self:
            names = self._get_computed_name(partner.firstname,
                                            partner.othernames,
                                            partner.lastname,
                                            partner.lastname2)
            partner.name = names.upper()

    @api.model
    def create(self, vals):
        res = super(ResPartner, self).create(vals)
        related_vals = {}
        if vals.get("name"):
            name = vals.get("name")
            related_vals["name"] = name.lower()
        if vals.get("firstname"):
            firstname = vals.get("firstname")
            related_vals["firstname"] = firstname.upper()
        if vals.get("othernames"):
            othernames = vals.get("othernames")
            related_vals["othernames"] = othernames.upper()
        if vals.get("lastname"):
            lastname = vals.get("lastname")
            related_vals["lastname"] = lastname.upper()
        if vals.get("lastname2"):
            lastname2 = vals.get("lastname2")
            related_vals["lastname2"] = lastname2.upper()
        if vals.get("email"):
            email = vals.get("email")
            related_vals["email"] = email.lower()
        if vals.get("einvoicing_email"):
            einvoicing_email = vals.get("einvoicing_email")
            related_vals["einvoicing_email"] = einvoicing_email.lower()
        if vals.get("street"):
            street = vals.get("street")
            related_vals["street"] = street.upper()
        if vals.get("street2"):
            street2 = vals.get("street2")
            related_vals["street2"] = street2.upper()
        if related_vals:
            res.write(related_vals)
        return res

    @api.multi
    def write(self, vals):
        if vals.get("name"):
            name = vals.get("name")
            vals["name"] = name.upper()
        if vals.get("firstname"):
            firstname = vals.get("firstname")
            vals["firstname"] = firstname.upper()
        if vals.get("othernames"):
            othernames = vals.get("othernames")
            vals["othernames"] = othernames.upper()
        if vals.get("lastname"):
            lastname = vals.get("lastname")
            vals["lastname"] = lastname.upper()
        if vals.get("lastname2"):
            lastname2 = vals.get("lastname2")
            vals["lastname2"] = lastname2.upper()
        if vals.get("email"):
            email = vals.get("email")
            vals["email"] = email.lower()
        if vals.get("einvoicing_email"):
            einvoicing_email = vals.get("einvoicing_email")
            vals["einvoicing_email"] = einvoicing_email.lower()
        if vals.get("street"):
            street = vals.get("street")
            vals["street"] = street.upper()
        if vals.get("street2"):
            street2 = vals.get("street2")
            vals["street2"] = street2.upper()
        return super(ResPartner, self).write(vals)
