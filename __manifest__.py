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
#    Autor: Brayhan Andres Jaramillo Castaño
#    Correo: brayhanjaramillo@hotmail.com
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################


{
	'name': 'Doctor Col Data',
	'category': 'Doctor',
	'version': '12.0',
	'author': 'Brayhan Andres Jaramillo Castaño' ,
	'license': 'LGPL-3',
	'maintainer': 'brayhanjaramillo@hotmail.com',
	'website': '',
	'summary': '',
	'images': [],

	'description': """

	Módulo base que contiene la información para el control de historias clínicas

	""",
	'depends': [ 'doctor_col'],

	'data': [
	


		'data/doctor_data_physical_exam_data.xml',
		'data/doctor_type_antecedent_data.xml',
		'data/doctor_administration_route_data.xml',
		'data/doctor_pharmaceutical_form_data.xml',
		'data/doctor_product_drugs_data.xml',
		'data/doctor_product_drugs_inherit_data.xml',


		'data/doctor_diseases_data.xml',
		'data/doctor_health_procedures_data.xml',
	
		'data/doctor_profession_data.xml',
		'data/doctor_speciality_data.xml',
		'data/doctor_stratum_data.xml',


	],


	'installable': True,
	'application': True,
	'auto_install': False,


}


