# Copyright (c) 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022 Python Software Foundation; All Rights Reserved
#
# SPDX-License-Identifier: PSF-2.0

# -*- coding: utf-8 -*-

class Towel(object):
    """A towel, that one should never be without."""

    def __init__(self, color='tie-dye'):
        self.color = color
        self.wrapped_obj = None

    def wrap(self, obj):
        """Wrap an object up in our towel."""
        self.wrapped_obj = obj

    def unwrap(self):
        """Unwrap whatever is in our towel and return whatever it is."""
        obj = self.wrapped_obj
        self.wrapped_obj = None
        return obj
