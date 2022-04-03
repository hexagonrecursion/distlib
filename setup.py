# Copyright (C) 2021 Vinay Sajip.
# Copyright (c) 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022 Python Software Foundation; All Rights Reserved
#
# SPDX-License-Identifier: PSF-2.0

import distutils.core
from os.path import join, dirname

import distlib


class TestCommand(distutils.core.Command):
    user_options = []

    def run(self):
        import sys

        sys.path.append(join(dirname(__file__), 'tests'))
        import test_all
        sys.exit(test_all.main())

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass


distutils.core.setup(
    name='distlib',
    version=distlib.__version__,
    author='Vinay Sajip',
    author_email='vinay_sajip@red-dove.com',
    url='https://github.com/pypa/distlib',
    download_url=('https://github.com/pypa/distlib/releases/download/' +
                  distlib.__version__ + '/distlib-' + distlib.__version__ + '.zip'),
    description='Distribution utilities',
    long_description=('Low-level components of distutils2/packaging, '
                      'augmented with higher-level APIs for making packaging easier.'),
    license='Python license',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development',
    ],
    platforms='any',
    packages=[
        'distlib'
    ],
    package_data={
        'distlib': ['t32.exe', 't64.exe', 'w32.exe', 'w64.exe',
                    't64-arm.exe', 'w64-arm.exe'],
    },
    cmdclass={
        'test': TestCommand,
    },
)
