# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
ERP+
"""
__author__ = 'António Anacleto'
__credits__ = []
__version__ = "1.0"
__maintainer__ = "António Anacleto"
__status__ = "Development"
__model_name__ = 'xml_anexo_reg_fornecedor_m106.XMLAnexoRegFornecedorM106'
import auth, base_models
from orm import *
from form import *


class XMLAnexoRegFornecedorM106(Model, View):
    def __init__(self, **kargs):
        #depois por aqui entre datas e só de um diario ou periodo, etc, etc.
        Model.__init__(self, **kargs)
        self.__name__ = 'xml_anexo_reg_fornecedor_m106'
        self.__title__ = 'Anexos Reg. Fornecedores - MOD 106'
        self.__model_name__ = __model_name__
        self.__list_edit_mode__ = 'edit'
        self.__get_options__ = ['nome']

        
        self.__workflow_auth__ = {
            'Visualizar':['All'],
            'Gerar':['All'],
            'Rascunho':['All'],
            'Confirmar':['All'],
            'full_access':['All']
            }        

        self.__auth__ = {
            'read':['All'],
            'write':['All'],
            'create':['All'],
            'delete':['All'],
            'full_access':['All']
            }

        
        self.nome = string_field(view_order = 1, name = 'Nome do documento', size = 60, args = 'readonly')

        self.xml_modelo_106 = parent_field(view_order = 2, name = 'Modelo 106', hidden=True, model_name = 'xml_modelo_106.XMLModelo106',nolabel=True, onlist = False)       

        self.nif_entidade = string_field(view_order=4, name='Nif', size=45, args = 'readonly')

        self.ano = string_field(view_order = 5, name ='Ano', size=45, args = 'readonly')

        self.mes = string_field(view_order = 6, name ='Mês', size=45, args = 'readonly')

        self.area_fiscal = string_field(view_order = 7, name = 'Área Fiscal', size = 50, args = 'readonly')

        # linhas do anexo
        self.xml_linha_anexo_reg_fornecedor_m106 = list_field(view_order = 8, name = 'Linhas', condition = "xml_anexo_reg_fornecedor_m106='{id}'", model_name = 'xml_linha_anexo_reg_fornecedor_m106.LinhaAnexoRegFornecedor', list_edit_mode = 'inline', onlist = False)
        
        self.data_entrega = string_field(view_order=9, name ='Data Entrega', args = 'readonly')
        
        self.total_factura = string_field(view_order = 10, name = 'Total Facturas', size = 45,args = 'readonly')
        
        self.total_base_incidencia = string_field(view_order = 11, name = 'Total Incidência', size = 45, args = 'readonly')

        self.total_suportado = string_field(view_order = 12, name = 'Total Suportado', size = 45, args = 'readonly')       

        self.total_dedutivel = string_field(view_order = 13, name = 'Total Dedutivel', size = 45, args = 'readonly')

        self.estado = info_field(view_order = 14, name ='Estado', default='Rascunho', args = 'readonly')

        self.xml_gerado = text_field(view_order = 15,name='Conteudo XML Gerado', size=100, args='readonly', onlist=False)