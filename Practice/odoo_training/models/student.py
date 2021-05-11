from odoo import  fields, models

class Car(models.Model):
	_name = 'car'
	_description = "Car Details"

	name = fields.Char(string = "Car Name")
	image = fields.Binary(string ="image", attachment=True)
	m_date = fields.Date(string = "Manufecture Date")
	km = fields.Integer(string = "Kilometers")
	showroom_id = fields.Many2one('showroom', string ="Showroom Name")
	model = fields.Selection([('top','Top'),('bottem','Bottem')], default = 'top')

class Showroom(models.Model):
	_name = 'showroom'
	_description = "Showroom Details"

	name = fields.Char(string = "Showroom Name")
	city = fields.Char(string = "City")
	car_id = fields.One2many('car','showroom_id')

class Owner(models.Model):
	_inherit = 'car'
	_name = 'inherit.car'
	_description = "Inherit Class"