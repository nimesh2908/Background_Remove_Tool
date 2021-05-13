from odoo import  fields, api, models

class Car(models.Model):
	_name = 'car'
	_description = "Car Details"

	name = fields.Char(string = "Car Name")
	image = fields.Binary(string ="image", attachment=True)
	m_date = fields.Date(string = "Manufecture Date")
	km = fields.Integer(string = "Kilometers")
	showroom_id = fields.Many2one('showroom', string ="Showroom Name")
	model = fields.Selection([('top','Top'),('bottem','Bottem')], default = 'top')
	price = fields.Integer(string ="Price")
	exhaust = fields.Integer(string="exhaust")
	sun_roof = fields.Integer(string="sun_roof")
	bass_tube = fields.Integer(string="bass_tube")
	total = fields.Integer(compute="compute_total",store=True)

	@api.depends('exhaust','sun_roof','bass_tube','price')
	def compute_total(self):
		for rec in self:
			rec.total=rec.exhaust + rec.sun_roof + rec.bass_tube + rec.price

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

	owner_name = fields.Char(string = "Owner Name")