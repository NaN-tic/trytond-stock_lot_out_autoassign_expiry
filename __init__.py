# This file is part of the stock_lot_out_autoassign_expiry module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .configuration import *


def register():
    Pool.register(
        Configuration,
        module='stock_lot_out_autoassign_expiry', type_='model')
