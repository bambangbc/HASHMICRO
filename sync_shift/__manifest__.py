# -*- coding: utf-8 -*-
###################################################################################
#    A part of Open HRMS Project <https://www.openhrms.com>
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2020-TODAY Cybrosys Technologies (<https://www.cybrosys.com>).
#    Author: Jesni Banu (<https://www.cybrosys.com>)
#
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
###################################################################################
{
    'name': 'HRMS Shift data Karyawan',
    'version': '14.1.',
    'summary': """Update filed data Shift""",
    'description': 'data ini berisi master jadwal dan shift karyawan.',
    'category': 'Generic Modules/Human Resources',
    'author': 'Hashmicro - bambang bagus candra',
    'company': 'PT Hashmicro Solusi Indonesia',
    'website': "https://www.syncpayou.com",
    'depends': ['base', 'hr', 'mail', 'hr_attendance','hr_contract'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_shift_view.xml',
        'views/caracter_view.xml'
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
