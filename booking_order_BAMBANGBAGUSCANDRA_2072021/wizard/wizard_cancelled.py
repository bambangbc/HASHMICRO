import time
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api, exceptions, _

class cancelled(models.TransientModel):
	_name = "cancelled.wo"

	note = fields.Text('Note')

	@api.multi
	def cancelled(self):
		import pdb;pdb.set_trace()
		cancel = self.env['work.order'].browse(self.env.context['active_id'])
		cancel_create = cancel.update({'note': self.note, 'state': 'cancelled'})




