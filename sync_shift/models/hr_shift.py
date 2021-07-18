from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class hr_shift(models.Model):
	_name = 'hr.shift'

	number = fields.Char(string="Nomor Shift")
	employee_id = fields.Many2one(comodel_name='hr.employee', string='Karyawan')
	department_id = fields.Many2one(comodel_name='hr.department', string='Department')
	start_date = fields.Date(string='Date Start')
	end_date = fields.Date(string='Date End')
	shift_type = fields.Many2one(comodel_name='resource.calendar', string='Shift Type')
	status = fields.Selection([('draft','Draft'),('confirmed','Confirmed'),('cancel','Cancelled')], default="draft",string="State", track_visibility='onchange')

	def confirm_shift(self):
		if self.start_date and self.end_date :

			for rec in self :
				rec.status ="confirmed"
		else:
			raise ValidationError(_('Please Set Start Date And End Date'))

	def set_to_draft(self):
		for rec in self :
			rec.status = "draft"

	def unlink(self):
		for rec in self:
			if rec.status not in ('draft'):
				raise UserError(_('dokumen tidak bisa di delete, kembalikan status ke draft agar bisa di delete'))
		return super(hr_shift, self).unlink()

hr_shift()

class HRAttendance(models.Model):
	_inherit = 'hr.attendance'

	absen_id = fields.Char(string="ID Absen")
	no_mesin = fields.Char(string="No Mesin")
	check_in_working = fields.Datetime(string="Check In Working") 
	check_out_working = fields.Datetime(string="Check Out Working")
	terlambat = fields.Float(string="Terlambat", compute="_compute_terlambat", store=True)
	denda = fields.Integer(string="Jumlah Denda", compute="_compute_denda")

	@api.depends('check_in_working', 'check_out_working', 'check_in', 'check_out')
	def _compute_terlambat(self) :
		for attendance in self :
			if attendance.check_out:
				delta = (attendance.check_in - attendance.check_in_working).total_seconds()
				terlambat = delta / 3600.0
				if delta >= 0 :
					attendance.terlambat = terlambat
				else :
					attendance.terlambat = False


	@api.depends('check_in', 'check_out')
	def _compute_denda(self):
		for denda in self :
			if denda.check_out:
				delta = (denda.check_in - denda.check_in_working).total_seconds()
				terlambat = delta / 3600.0
				for status in self.env['hr.terlambat'].search([]) :
					if terlambat >= status.terlambat_dari and terlambat <= status.terlambat_sampai :
						denda.denda = status.denda

HRAttendance()

class terlambat(models.Model):
	_name = 'hr.terlambat'

	denda = fields.Integer(string="Jumlah Denda")
	terlambat_dari = fields.Float('Terlambat Dari')
	terlambat_sampai = fields.Float('Terlambat Sampai')

