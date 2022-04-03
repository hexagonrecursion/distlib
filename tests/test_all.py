# Copyright (C) 2012-2013 Vinay Sajip.
# Copyright (c) 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022 Python Software Foundation; All Rights Reserved
#
# SPDX-License-Identifier: PSF-2.0

import logging
import os
import sys

from compat import unittest

# Always find our sources first
sys.path.insert(0, '..')
import distlib_tests
sys.path.pop(0)

def main():
    verbosity = 1
    if '-v' in sys.argv:
        verbosity = 2
    loader = unittest.TestLoader()
    failfast = 'FAILFAST' in os.environ
    runner = unittest.TextTestRunner(verbosity=verbosity, failfast=failfast)
    results = runner.run(loader.loadTestsFromModule(distlib_tests))
    return not results.wasSuccessful()

if __name__ == '__main__':
    here = os.path.dirname(os.path.abspath(__file__))
    rundir = os.path.join(here, 'run')
    if not os.path.exists(rundir):
        os.mkdir(rundir)
    elif not os.path.isdir(rundir):
        raise ValueError('Not a directory: %r' % rundir)
    fn = os.path.join(rundir, 'test_all_%d.%d.log' % sys.version_info[:2])
    logging.basicConfig(level=logging.DEBUG, filename=fn, filemode='w',
                        format='%(levelname)-8s %(name)-20s %(message)s')
    sys.exit(main())
