# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

"""adds functionally to partner beacuse a partner could have blocked prodlot, and the partner that be alerted and return prodlot"""

from osv import fields, osv

class res_partner(osv.osv):
    """adds functionally to partner beacuse a partner could have blocked prodlot, and the partner that be alerted and return prodlot"""
    _inherit = 'res.partner'
    
    _columns = {
        'property_stock_returns': fields.property(
          'stock.location',
          type='many2one',
          relation='stock.location',
          string="Returns Location",
          method=True,
          view_load=True,
          help="This stock location will be used, instead of the default one, as the source location for returning goods you receive from the current partner"),
    }
res_partner()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: