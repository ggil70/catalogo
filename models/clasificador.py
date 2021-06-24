
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




class clasificador_bien(models.Model):
    """Registra la Clasificacion de Bienes Interna"""
    
    _name = 'clasificador_bien'
    #_rec_name = 'clasificador_codigo'
    _rec_name = 'clasificador_nombre'
    #_rec_name = 'grupo_bien_id '
    _order = 'grupo_bien_id, clasificador_nombre asc' 
    

    clasificador_codigo = fields.Char(string='Codigo de la Clase',
    size=3,
    required=True,
    default='New',
    help='Registra el Codigo de la Clase del Bien (Interna)')
    clasificador_nombre = fields.Char(string='Nombre del Clase',size=100,required=True, help='Registra el Nombre de la Clase del Bien(Interna)')
    grupo_bien_id = fields.Many2one('grupo_bien',string='Grupo de Bienes', required=True, help='Registra el Codigo de Vinculacion con el Grupo de Bienes')
    grupo_bien_codigo =  fields.Char(string='Codigo del Grupo',size=3,  required=True,help='Registra el Codigo del Grupo (Interna)')
    _sql_constraints = [('clasificador_nombre', 'unique(grupo_bien_id,clasificador_nombre)', 'El Nombre debe se único!')]  
    
    
   

    @api.model  
    def create(self,vals):
        if vals.get('clasificador_codigo', 'New') == 'New' or '':
            vals['clasificador_codigo'] = self.env['ir.sequence'].next_by_code(
            'self.grupo_bien_codigo') or 'New'
        result = super(grupo_bien, self).create(vals)
        return result        



 






    @api.onchange('grupo_bien_id')
    def onchange_grupo(self):
        codigo= ''
        codigo = self.grupo_bien_id.grupo_bien_codigo
        self.grupo_bien_codigo =  codigo
      
   


