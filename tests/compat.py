# Copyright (C) 2012 The Python Software Foundation.
# Copyright (c) 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022 Python Software Foundation; All Rights Reserved
#
# SPDX-License-Identifier: PSF-2.0

import sys

import unittest

_ver = sys.version_info[:2]

if _ver[0] < 3:
    import Queue as queue
    from SimpleXMLRPCServer import SimpleXMLRPCServer
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    from BaseHTTPServer import HTTPServer
    text_type = unicode
    from urllib import unquote
    from urllib2 import Request
    from urlparse import urlparse
else:
    import queue
    from xmlrpc.server import SimpleXMLRPCServer
    from http.server import HTTPServer, SimpleHTTPRequestHandler
    text_type = str
    from urllib.parse import urlparse, unquote
    from urllib.request import Request
