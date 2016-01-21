#!/usr/bin/env python

from distutils.core import setup

setup(name='nanopipe',
      version='0.0',
      description='NANOGrav calibration and TOA pipeline',
      author='Paul Demorest',
      author_email='pdemores@nrao.edu',
      url='http://github.com/demorest/nanopipe',
      packages=['nanopipe'],
      package_dir={'nanopipe': 'src'},
      package_data={'nanopipe': ['data/psrjnames.dat','data/psrbnames.dat']},
      scripts=['scripts/make_psr_make']
     )