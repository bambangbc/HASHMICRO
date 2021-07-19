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
    'name': 'Booking Order',
    'version': '10.1.',
    'description': 'booking Order, Bambang Bagus Candra, 20072021',
    'category': 'Sales',
    'author': 'Hashmicro - bambang bagus candra',
    'company': 'PT Hashmicro Solusi Indonesia',
    'website': "https://www.hasmicro.com",
    'depends': ['base', 'mail', 'sale', 'sales_team'],
    'data': [
        'wizard/wizard_cancelled.xml',
        'views/booking_order.xml',
        'report/report_work_order.xml',
        'report/report.xml',
        'data/data.xml'
    ],
    'installable': True,
    'auto_install': False,
}
