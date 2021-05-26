# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError
import re


class Covid19Survey(models.Model):

    _name = 'covid19.partner.survey'
    _rec_name = "complete_name"
    _description = 'EXA Auto Parts & Solutions Biosecurity Protocol Survey'
    _order = "create_date desc"

    @api.model
    def _default_country(self):
        return self.env['res.country'].search([('code', '=', 'CO')], limit=1)

    partner_id = fields.Many2one('res.partner', string='Tercero')
    partner_ident_type_id = fields.Many2one(
        related='partner_id.document_type_id',
        store=False,
        string='Tipo Identificación')
    partner_identification = fields.Char(
        related='partner_id.identification_document',
        store=False,
        string='Identificación')
    partner_contact_phone = fields.Char(related='partner_id.mobile',
                                        store=False,
                                        string='Tel. Contacto')

    partner_person_id = fields.Many2one(
        'res.partner',
        string='Diligenciar con Persona Registrada',
        help=
        "Si el usuario no existe por favor deje este campo vacío y llene los campos obligatorios.\nEl usuario quedará registrado cuando pulse en el botón guardar.",
        required=False)
    first_name = fields.Char('Primer Nombre', required=True)
    last_name = fields.Char('Primer Apellido', required=True)
    complete_name = fields.Char(compute='_compute_name',
                                store=True,
                                string="Nombre Completo")
    document_type_id = fields.Many2one('res.partner.document.type',
                                       string="Tipo Identificación",
                                       required=True)
    identification_document = fields.Char(string='Identificación',
                                          required=True)
    contact_phone = fields.Char(string='Tel. Contacto', required=True)
    partner_country_id = fields.Many2one('res.country',
                                         string='País de Residencia',
                                         required=True,
                                         default=_default_country)

    temperature = fields.Float(
        '¿Cuál es su temperatura corporal el día de hoy? Use coma en vez de punto (Ej. 36,5)',
        required=True)
    mask = fields.Boolean(
        string="¿Lleva puesto de manera adecuada el tapabocas?", default=False)
    partner_type = fields.Char('Tipo de visitante', required=True)
    question_1 = fields.Boolean(
        default=False,
        string=
        "¿Presenta alguno de estos síntomas, está a la espera de realizarse una prueba de coronavirus o ha sido diagnosticado con coronavirus?: dificultad para respirar, fiebre, tos seca, dolor de cabeza, dolor de garganta, malestar general, pérdida del gusto, pérdida del olfato, escurrimiento nasal, dolor muscular, dolor articular, dolor toráxico."
    )
    question_2 = fields.Boolean(
        default=False,
        string=
        "¿Alguna de las personas que vive con usted presenta alguno de estos síntomas, está a la espera de realizarse una prueba de coronavirus o ha sido diagnosticado con coronavirus?: dificultad para respirar, fiebre, tos seca, dolor de cabeza, dolor de garganta, malestar general, pérdida del gusto, pérdida del olfato, escurrimiento nasal, dolor muscular, dolor articular, dolor toráxico."
    )
    question_3 = fields.Boolean(
        default=False,
        string=
        "La persona manifiesta que la información declarada es real y acepta las consecuencias de no reportar adecuadamente la información, además autoriza que la información consignada sea tratada conforme a lo establecido en la ley 1581 de 2012 con relación a la protección de datos personales."
    )

    @api.depends('first_name', 'last_name')
    def _compute_name(self):
        for partner in self:
            if partner.first_name and partner.last_name:
                complete_name = u' '.join(
                    [partner.first_name.upper(),
                     partner.last_name.upper()])
            partner.complete_name = complete_name

    @api.onchange('partner_id')
    def fillDetailsIfPerson(self):
        if self.partner_id:
            # person type { 1 juridical person, 2 natural person}
            if self.partner_id.person_type == '2':
                self.partner_person_id = self.partner_id
                self.first_name = self.partner_id.firstname
                self.last_name = self.partner_id.lastname
                self.document_type_id = self.partner_id.document_type_id
                self.identification_document = self.partner_id.identification_document
                self.contact_phone = self.partner_id.mobile
                self.partner_country_id = self.partner_id.country_id
            else:
                self.partner_person_id = ''
                self.first_name = ''
                self.last_name = ''
                self.document_type_id = ''
                self.identification_document = ''
                self.contact_phone = ''

    @api.onchange('partner_id')
    def partnerType(self):
        if self.partner_id:
            if self.partner_id.customer:
                self.partner_type = "CLIENTE"
            elif self.partner_id.prospect:
                self.partner_type = "PROSPECTO"
            elif self.partner_id.supplier:
                self.partner_type = "PROVEEDOR/CONTRATISTA"
            else:
                self.partner_type = "OTRO"
        else:
            self.partner_type = ""

    @api.onchange('partner_person_id')
    def partnerPerson(self):
        if self.partner_person_id:
            if self.partner_person_id.person_type:
                self.first_name = self.partner_person_id.firstname
                self.last_name = self.partner_person_id.lastname
                self.document_type_id = self.partner_person_id.document_type_id
                self.identification_document = self.partner_person_id.identification_document
                self.contact_phone = self.partner_person_id.mobile
                if self.partner_person_id.country_id:
                    self.partner_country_id = self.partner_person_id.country_id
            else:
                self.clearUI()
        else:
            self.clearUI()

    def clearUI(self):
        self.first_name = ''
        self.last_name = ''
        self.document_type_id = ''
        self.identification_document = ''
        self.contact_phone = ''

    def checkIdentificationDocument(self, identification_document):
        m = re.search('\.', str(identification_document))
        if m:  #check if
            return False
        return True

    def LongContactPhoneLen(self, contact_phone):
        return len(contact_phone) > 10

    def checkValidTemperature(self, temperature):
        return 35.0 <= temperature <= 38.0

    def createPartner(self, vals):
        obj = self.env['res.partner']
        partner_id = obj.create(vals)
        if partner_id:
            return True
        raise UserError(
            _("No se ha podido crear el nuevo contacto.\nSi ya existe por favor búsquelo como 'Persona Registrada'."
              ))

    @api.model
    def create(self, vals):
        vals['first_name'] = vals.get('first_name').upper()
        vals['last_name'] = vals.get('last_name').upper()

        data = {
            'firstname': vals.get('first_name').upper(),
            'lastname': vals.get('last_name').upper(),
            'person_type': '2',
            'document_type_id': vals.get('document_type_id'),
            'identification_document': vals.get('identification_document'),
            'mobile': vals.get('contact_phone'),
            'country_id': vals.get('partner_country_id'),
        }
        #let's create a partner if he/she doesn't exists
        if not vals.get('partner_person_id'):
            self.createPartner(data)

        if not self.checkIdentificationDocument(
                vals.get('identification_document')):
            raise UserError(
                _("El formato de \"Identificación\" no es válido. Por favor quite los puntos"
                  ))
        if self.LongContactPhoneLen(vals.get('contact_phone')):
            raise UserError(
                _("El Tel. de contacto de LA PERSONA no debe tener más de 10 dígitos."
                  ))
        if vals.get('temperature') == 0.0:
            raise UserError(
                _("El campo \"¿Cuál es su temperatura corporal...\" es obligatorio."
                  ))
        if not self.checkValidTemperature(vals.get('temperature')):
            raise UserError(
                _("Valor inválido, La temperatura debe ser un valor entre 35°C y 37°C "
                  ))
        if vals.get('temperature') >= 37.8:
            raise UserError(
                _("Como su temperatura es mayor a 37.8ºC, no es posible que ingrese a las instalaciones de la empresa y debe reportar su estado de salud a su EPS"
                  ))
        if not vals.get('mask'):
            raise UserError(
                _("Como no lleva el tapabocas de manera adecuada no es posible que ingrese a las instalaciones de la empresa."
                  ))
        if vals.get('question_1'):
            raise UserError(
                _("Lo sentimos!\nSi presenta alguno de estos síntomas o es positivo para Covid-19 no puede ingresar a las instalaciones de la empresa."
                  ))
        if vals.get('question_2'):
            raise UserError(
                _("Lo sentimos!\nSi alguna de las personas con las que vive presenta estos síntomas no puede ingresar a las instalaciones de la empresa."
                  ))
        if not vals.get('question_3'):
            raise UserError(
                _("Él último campo \"La persona manifiesta que la información declarada es real ...\" No fue diligenciado."
                  ))
        return super(Covid19Survey, self).create(vals)