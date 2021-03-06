
# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
# Generated by the OpenERP plugin for Dia !
# from osv import fields,osv --- <8.0.X
from odoo import api, fields, models
from odoo.exceptions import ValidationError
from datetime import date, datetime,timedelta
#from odoo.addons.jasper_reports import jasper_report
#from odoo import pooler
from datetime import  datetime
from time import time
formatter_string = "%d-%m-%y" 
#from tools.translate import_
#from odoo import tools
import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")
#Importamos la libreria logger
import logging
#Definimos la Variable Global
_logger = logging.getLogger(__name__)


       


   #****************Tipos de Estatus de Inventario*******************#
class tipo_estatus_inventario(models.Model):
    """Registra los Tipos de estatus de inventario de bienes"""
    _name = 'tipo_estatus_inventario'
    _rec_name = 'nom_estatus'
    nom_estatus = fields.Char('Nombre del Estatus del Inventario',size=100,required=True, help='Registra el Nombre del Movimiento')
    cod_estatus = fields.Char('Codigo del Estatus del Inventario',size=100, required=True, help='Registra el Codigo del Estatus de Inventario')
    _sql_constraints = [('nom_estatus', 'unique(nom_estatus)', 'El Nombre del Estatus del Inventario debe ser Unico!')]  

