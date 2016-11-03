from setuptools import Command, find_packages, setup

from os.path import abspath, dirname, join
from codecs import open

from triad import __version__

curr_dir = abspath(dirname(__file__))
with open(join(curr_dir, 'README.md'), encoding='utf-8') as readme:
	long_description = readme.read()

setup(
	name = 'triad',
	version = __version__,
	description = 'An experimental command line program",
	long_description = long_description
)
