# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MaintenanceEquipmentTechInfo(models.Model):
    _inherit = 'maintenance.equipment'

    x_brand = fields.Char('Marca')
    x_deviceName = fields.Char('Nombre Equipo')
    x_licenseNum = fields.Char('Número licencia')
    x_licenseExpiration= fields.Date('Vigencia Licencia')
    x_os = fields.Char('Sistema Operativo')
    x_osUpdate = fields.Char('Actualización S.O')
    x_model = fields.Char('Modelo')
    x_serviceTagSerial = fields.Char('Service Tag / Serial')
    x_processor = fields.Char('Procesador')
    x_ram = fields.Char('RAM')
    x_hdd = fields.Char('HDD (GB)')
    x_ssd = fields.Char('SDD (GB')
    x_dvd = fields.Boolean('DVD')
    x_macNic = fields.Char('MAC NIC')
    x_macWifi = fields.Char('MAC WiFi')
    x_anydeskUser = fields.Char('Anydesk Usuario')
    x_anydeskPassword = fields.Char('Anydesk Contraseña')
    x_telegram = fields.Boolean('Telegram')
    x_nextcloud = fields.Boolean('NextCloud')
    x_zoom = fields.Boolean('Zoom')
    x_notes = fields.Text('Notas')
    x_deployment_env = fields.Selection([
        ('testing', 'Pruebas'),
        ('production', 'Producción')],'Ambiente')
    x_cpu_cores = fields.Integer('CPU Cores')
    x_raid_hw = fields.Integer('Raid HW')
    x_monitoring = fields.Boolean('Monitoreo')
    x_function = fields.Char('Función')
    x_backup = fields.Boolean('Backup')
    x_status = fields.Selection([
        ('on', 'Encendido'),
        ('off', 'Apagado')],'Estado')
    # x_field_21 = fields.Char('Campo 21')
    # x_field_22 = fields.Char('Campo 22')
    # x_field_23 = fields.Char('Campo 23')
    # x_field_24 = fields.Char('Campo 24')
    # x_field_25 = fields.Char('Campo 25')
    # x_field_26 = fields.Char('Campo 26')
    # x_field_27 = fields.Char('Campo 27')
    # x_field_28 = fields.Char('Campo 28')
    # x_field_29 = fields.Char('Campo 29')
    # x_field_30 = fields.Char('Campo 30')
    
    # x_field_31 = fields.Text('Campo 31')
    # x_field_32 = fields.Text('Campo 32')
    # x_field_33 = fields.Text('Campo 33')
    # x_field_34 = fields.Text('Campo 34')
    # x_field_35 = fields.Text('Campo 35')
