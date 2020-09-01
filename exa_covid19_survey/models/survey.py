# -*- coding: utf-8 -*-

from datetime import date, datetime, timedelta
from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError
import re
import logging

class Covid19Survey(models.Model):

    _name = 'covid19.partner.survey'
    _rec_name = "complete_name"
    _description = 'EXA Auto Parts & Solutions Biosecurity Protocol Survey'
    _order = "create_date desc"

    partner_id = fields.Many2one('res.partner', string='Tercero')
    partner_ident_type_id = fields.Many2one(related='partner_id.document_type_id', store=False, string='Tipo Identificación')
    partner_identification = fields.Char(related='partner_id.identification_document', store=False, string='Identificación')
    partner_contact_phone = fields.Char(related='partner_id.mobile', store=False, string='Tel. Contacto')

    first_name = fields.Char('Primer Nombre', required=True)
    last_name = fields.Char('Primer Apellido', required=True)
    complete_name = fields.Char(compute='_compute_name', store=True, string="Nombre Completo")
    document_type_id = fields.Many2one('res.partner.document.type', string="Tipo Identificación", required=True)
    identification_document = fields.Char(string='Identificación', required=True)
    contact_phone = fields.Char(string='Tel. Contacto', required=True)

    temperature = fields.Float('¿Cuál es su temperatura corporal el día de hoy? Use coma en vez de punto (Ej. 36,5)',required=True)
    mask = fields.Boolean(string="¿Lleva puesto de manera adecuada el tapabocas?", default=False)
    partner_type = fields.Char('Tipo de visitante', required=True)
    question_1 = fields.Boolean(default=False, string="¿Presenta alguno de estos síntomas, está a la espera de realizarse una prueba de coronavirus o ha sido diagnosticado con coronavirus?: dificultad para respirar, fiebre, tos seca, dolor de cabeza, dolor de garganta, malestar general, pérdida del gusto, pérdida del olfato, escurrimiento nasal, dolor muscular, dolor articular, dolor toráxico.")
    question_2 = fields.Boolean(default=False, string="¿Alguna de las personas que vive con usted presenta alguno de estos síntomas, está a la espera de realizarse una prueba de coronavirus o ha sido diagnosticado con coronavirus?: dificultad para respirar, fiebre, tos seca, dolor de cabeza, dolor de garganta, malestar general, pérdida del gusto, pérdida del olfato, escurrimiento nasal, dolor muscular, dolor articular, dolor toráxico.")
    question_3 = fields.Boolean(default=False, string="La persona manifiesta que la información declarada es real y acepto las consecuencias de no reportar adecuadamente la información, además autorizo que la información consignada sea tratada conforme a lo establecido en la ley 1581 de 2012 con relación a la protección de datos personales.")

    @api.depends('first_name', 'last_name')
    def _compute_name(self):
        for partner in self:
            if partner.first_name and partner.last_name:
                complete_name = u' '.join([partner.first_name, partner.last_name])
            partner.complete_name = complete_name

    @api.onchange('partner_id')
    def fillDetailsIfPerson(self):
        if self.partner_id:
            # person type { 1 juridical person, 2 natural person}
            if  self.partner_id.person_type == '2':
                self.first_name = self.partner_id.firstname
                self.last_name = self.partner_id.lastname
                self.document_type_id = self.partner_id.document_type_id
                self.identification_document = self.partner_id.identification_document
                self.contact_phone = self.partner_id.mobile
            else:
                self.first_name = ''
                self.last_name = ''
                self.document_type_id = ''
                self.identification_document = ''
                self.contact_phone = ''

    @api.onchange('partner_id')
    def partnerType(self):
        if self.partner_id:
            if self.partner_id.customer:
                self.partner_type = "Cliente"
            elif self.partner_id.prospect:
                self.partner_type = "Prospecto"
            elif self.partner_id.supplier:
                self.partner_type = "Proveedor/Contratista"
            else:
                self.partner_type = "Otro"
        
    
    def checkIdentificationDocument(self,identification_document):
        m = re.search('\.', str(identification_document))
        if m:
            return False
        return True

    def LongContactPhoneLen(self,contact_phone):
        return len(contact_phone) > 10

    def checkValidTemperature(self,temperature):
        return 35.0 <= temperature <= 38.0      

    @api.model
    def create(self, vals):
        if not self.checkIdentificationDocument(vals.get('identification_document')):
            raise UserError(_("El formato de \"Identificación\" no es válido. Por favor quite los puntos"))
        if self.LongContactPhoneLen(vals.get('contact_phone')):
            raise UserError(_("El Tel. de contacto de LA PERSONA no debe tener más de 10 dígitos."))  
        if vals.get('temperature') == 0.0:
            raise UserError(_("El campo \"¿Cuál es su temperatura corporal...\" es obligatorio."))
        if not self.checkValidTemperature(vals.get('temperature')):
            raise UserError(_("Valor inválido, La temperatura debe ser un valor entre 35°C y 37°C "))    
        if vals.get('temperature') >= 37.8:
            raise UserError(_("Como su temperatura es mayor a 37.8ºC, no es posible que ingrese a las instalaciones de la empresa y debe reportar su estado de salud a su EPS"))
        if not vals.get('mask'):
            raise UserError(_("Como no lleva el tapabocas de manera adecuada no es posible que ingrese a las instalaciones de la empresa."))
        if vals.get('question_1'):
            raise UserError(_("Lo sentimos!\nSi presenta alguno de estos síntomas o es positivo para Covid-19 no puede ingresar a las instalaciones de la empresa."))
        if vals.get('question_2'):
            raise UserError(_("Lo sentimos!\nSi alguna de las personas con las que vive presenta estos síntomas no puede ingresar a las instalaciones de la empresa."))
        if not vals.get('question_3'):
            raise UserError(_("Él último campo \"La persona manifiesta que la información declarada es real ...\" No fue diligenciado."))
        return super(Covid19Survey, self).create(vals)