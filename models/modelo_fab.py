
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


class modelo_fab(models.Model):
    """Registra el Modelo de Fabrica del Bien"""
    _name = 'modelo_fab'
    #_rec_name = 'modelo_fab_codigo'
    _rec_name = 'modelo_fab_nombre'
    #_rec_name = 'marcas_id'
    _order = 'marcas_id, modelo_fab_nombre'
    
   
    modelo_fab_codigo = fields.Char(string='Codigo del Modelo',
    					 size=3,
                         required=True,
                         default='New',
    					 help='Registra el Codigo del Modelo de Fabrica')
    modelo_fab_nombre = fields.Char(string='Nombre del Modelo',size=100,required=True, help='Registra el Nombre del Modelo de Fabrica')
    marcas_id         = fields.Many2one('marcas',string='Marcas del Modelo',required=True, help='Registra el Codigo de Vinculacion con la Marca del Bien')
    marcas_codigo     = fields.Char(string='Codigo de la Marca',
    				    size=3,required=True,
    				    help='Registra el Codigo de la Marca')


    _sql_constraints = [('modelo_fab_nombre', 'unique( marcas_id,modelo_fab_nombre)', 'El Nombre debe se único!')]    




    @api.model  
    def create(self,vals):
       if vals.get('modelo_fab_codigo',  'New') == 'New' or '':
          vals['modelo_fab_codigo'] = self.env['ir.sequence'].next_by_code(
           'self.modelo_fab_codigo')  or 'New'
          
       result = super(modelo_fab, self).create(vals)
       return result 


    @api.onchange('marcas_id')
    def onchange_marcas(self):
        codigo= ''
        codigo = self.marcas_id.marcas_codigo 
        self.marcas_codigo  =  codigo
      
