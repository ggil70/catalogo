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




class marcas(models.Model):
    """Registra las Marcas de los Bienes"""
    _name = 'marcas'
    #_rec_name = 'marcas_codigo'
    _rec_name = 'marcas_nombre'
    

    marcas_codigo = fields.Char(string='Codigo de la Marca',
    				size=3,
    				default='New',
                    required=True,
    				help='Registra el Codigo de la Marca')
    marcas_nombre = fields.Char(string='Nombre de la Marca',size=40,required=True, help='Registra el Nombre de la Marca')
    marcas_fabricante = fields.Char(string='Nombre del Fabricante',
    					size=40, 
    					default='XXX',
    					help='Registra el Nombre del Fabricante')

    

    _sql_constraints = [('marcas_nombre', 'unique(marcas_nombre)', 'El Nombre debe se único!')]    
    

    @api.model  
    def create(self,vals):
       if vals.get('marcas_codigo',  'New') == 'New' or '':
          vals['marcas_codigo'] = self.env['ir.sequence'].next_by_code(
           'self.marcas_codigo')  or 'New'
          
       result = super(marcas, self).create(vals)
       return result 