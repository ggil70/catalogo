# -*- coding: utf-8 -*-

{
        'name': "Registro de Catalogo de Bienes Publicos",
        'version' : "13.1",
        'author' : "Beatriz Coronel",
        'website' : "",
        'category' : "Bienes Publicos",
        
        'description': """
               Catalogo Interno de Bienes Publicos
         """,
        'depends' : ['base',],
        'data' : ['security/groups.xml',
                  'security/ir.model.access.csv',
                  'views/grupo_view.xml',
                  'views/clasificador_view.xml',
                  'views/modelo_view.xml',
                  'views/detalle_modelo_view.xml',
                  'views/marcas_view.xml',
                  'views/modelo_fab_view.xml',
                  'views/color_view.xml',
                  'views/material_view.xml',
                  'views/ubicacion_fisica_view.xml',
                  'views/tipo_estatus_inventario_view.xml',
                  
                  'report/ubicacion_fisica_bien_template.xml',
                  'report/clase_bien_template.xml',
                  'report/grupo_bien_template.xml',
                  'report/modelo_bien_template.xml',
                  'report/color_bien_template.xml',
                  'report/material_bien_template.xml', 
                  'report/marca_bien_template.xml',
                  'report/modelo_fab_bien_template.xml', 
                  
                  


                  'data/grupo.xml',
                  'data/clasificador_bien.xml',
                  'data/modelo.xml',
                  'data/detalle_modelo.xml',
                  'data/marcas.xml',
                  'data/modelo_fab.xml',
                  'data/color.xml',
                  'data/material.xml',
                  'data/ir.sequence.xml',
                  
        # 'data/clasificador_bien.xml',
        # 'data/modelo.xml',
        # 'data/detalle_modelo.xml',
        # 'data/color.xml',
        # 'data/material.xml',
      
        # 'data/modelo_fab.xml',
        # 'data/tipo_estructura.xml',
        # 'data/tipo_pisos.xml',
        # 'data/tipo_estructura.xml',
        # 'data/tipo_paredes.xml',
        # 'data/tipo_techos.xml',
        # 'data/tipo_puertas.xml',
        # 'data/tipo_servicios.xml',
        # 'data/tipo_anexos.xml',
      
      


        ], 


       
        
        #'installable': True,
        #'auto_install': False
        
} 
