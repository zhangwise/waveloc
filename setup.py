#!/usr/bin/env python

from distutils.core import setup

setup(name='Waveloc',
	version='0.1',
	description='Earthquake location by waveform migration',
	author='Alessia Maggi',
	author_email='alessia.maggi@unistra.fr',
	url='http://github.com/amaggi/waveloc',
	packages=['waveloc'],
	package_dir = {'waveloc' : 'PyProgs'},
	scripts=['scripts/grid2hdf5'],
        requires=[
		'numpy(>=1.6.1)',
		'obspy.core(>=0.7.1)',
	]
	classifiers=[
		'Development Status :: 2 - Pre-Alpha',
		'Environment :: Console',
		'Intended Audience :: Science/Research',
		'License :: OSI Approved :: GNU General Public License (GPL)',
		'Programming Language :: Python :: 2.7',
		'Topic :: Scientific/Engineering',
	],
)