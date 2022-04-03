# Copyright (C) 2012-2019 Vinay Sajip.
# Copyright (c) 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022 Python Software Foundation; All Rights Reserved
#
# SPDX-License-Identifier: PSF-2.0

import logging

__version__ = '0.3.5.dev0'

class DistlibException(Exception):
    pass

try:
    from logging import NullHandler
except ImportError: # pragma: no cover
    class NullHandler(logging.Handler):
        def handle(self, record): pass
        def emit(self, record): pass
        def createLock(self): self.lock = None

logger = logging.getLogger(__name__)
logger.addHandler(NullHandler())
