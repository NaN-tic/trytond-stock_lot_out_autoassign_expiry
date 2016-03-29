# This file is part of the stock_lot_out_autoassign_expiry module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta

__all__ = ['Configuration']


class Configuration:
    __metaclass__ = PoolMeta
    __name__ = 'stock.configuration'

    @classmethod
    def __setup__(cls):
        super(Configuration, cls).__setup__()
        selection = [
            ('life_date', 'End of Life Date'),
            ('expiry_date', 'Expiry Date'),
            ('removal_date', 'Removal Date'),
            ('alert_date', 'Alert Date'),
            ]
        for option in selection:
            if option not in cls.lot_priority.selection:
                cls.lot_priority.selection.append(option)
