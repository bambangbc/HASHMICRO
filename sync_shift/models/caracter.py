from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class caracter(models.Model):

	_name ='caracter'

	input_1 = fields.Char(string="Input 1")
	input_2 = fields.Char(string="Input 2")
	hasil = fields.Char(string="hasil")

	def generate_caracter(self):
		input1 = list(self.input_1)
		input2 = list(self.input_2)

		jum_input1 = len(input1)
		nilai = 0

		for char1 in input1 :
			for char2 in input2 :
				if char1 == char2 :
					nilai_sementara = 100 / jum_input1
			nilai = nilai + nilai_sementara
			nilai_sementara = 0

		self.hasil = nilai


caracter()
