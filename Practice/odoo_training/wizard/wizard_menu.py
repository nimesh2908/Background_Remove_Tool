from odoo import models, fields, api

class Wizard(models.TransientModel):
    _name = 'wizard'
    _description = "Wizard"

    showroom_id = fields.Many2one('showroom', string="Showroom Id")  

    def add_showroom(self):
    	self.env['car'].browse(self._context.get("active_ids")).update({"showroom_id":self.showroom_id})
    	return True
